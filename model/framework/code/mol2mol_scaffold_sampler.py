import os
import sys
import time

import torch
from rdkit import Chem
from reinvent.runmodes import samplers, create_adapter
from reinvent.runmodes.dtos import ChemistryHelpers
from reinvent.chemistry import TransformationTokens, Conversions
from reinvent.chemistry.library_design import BondMaker, AttachmentPoints
from reinvent.runmodes.samplers.run_sampling import filter_valid

from utils import is_same_2d_structure

N_OUTPUTS = 100  # columns of run_columns.csv
DRAWS_PER_ROUND = 150  # sequences drawn by one call of a sampler
MAX_ROUNDS = 5  # per prior: give up on an input after this many rounds
TEMPERATURE = 1.0  # REINVENT 4's default for sampling


class Mol2MolScaffoldSampler:
    """Samples analogues of a molecule with REINVENT 4's two Mol2Mol scaffold priors.

    The first prior was trained on pairs that share the Murcko scaffold, the second on pairs that share
    the generic scaffold. Each round draws DRAWS_PER_ROUND sequences by multinomial sampling (unseeded,
    so every call gives a different set). Rounds of the scaffold prior are repeated until N_OUTPUTS
    distinct molecules that are not the input (stereochemistry ignored) are collected, or MAX_ROUNDS is
    reached; only then are rounds of the generic-scaffold prior used, to fill what is left. The row is
    padded with empty cells. Nothing is ranked: the molecules stay in draw order.
    """

    ROOT = os.path.dirname(os.path.abspath(__file__))
    CHECKPOINT = os.path.join(ROOT, "..", "..", "checkpoints")
    SCAFFOLD_MODEL = os.path.realpath(
        os.path.join(CHECKPOINT, "mol2mol_scaffold.prior")
    )
    SCAFFOLD_GENERIC_MODEL = os.path.realpath(
        os.path.join(CHECKPOINT, "mol2mol_scaffold_generic.prior")
    )

    def __init__(self):
        self.chemistry = ChemistryHelpers(
            Conversions(), BondMaker(), AttachmentPoints()
        )
        self.scaffold_sampler = self._make_sampler(self.SCAFFOLD_MODEL)
        self._generic_sampler = None  # loaded only if an input needs it

    @property
    def scaffold_generic_sampler(self):
        if self._generic_sampler is None:
            self._generic_sampler = self._make_sampler(self.SCAFFOLD_GENERIC_MODEL)
        return self._generic_sampler

    def _make_sampler(self, model_path: str) -> samplers.Mol2MolSampler:
        agent, _, _ = create_adapter(model_path, "inference", torch.device("cpu"))
        return samplers.Mol2MolSampler(
            agent,
            batch_size=DRAWS_PER_ROUND,
            sample_strategy="multinomial",
            isomeric=True,
            randomize_smiles=False,  # REINVENT 4 sets it to False for Mol2Mol
            unique_sequences=True,
            chemistry=self.chemistry,
            temperature=TEMPERATURE,
            tokens=TransformationTokens(),
        )

    @staticmethod
    def _collect(sampler, smiles: str, pool: dict) -> None:
        """Rounds of sampling with `sampler` into `pool` until it holds N_OUTPUTS molecules."""
        for _ in range(MAX_ROUNDS):
            if len(pool) >= N_OUTPUTS:
                return
            with torch.no_grad():
                sampled = filter_valid(sampler.sample([smiles]))
            for smile in sampled.smilies:
                mol = Chem.MolFromSmiles(smile)
                if mol is None or is_same_2d_structure(smile, smiles):
                    continue
                # canonical isomeric SMILES as the key keeps one entry per molecule
                pool.setdefault(Chem.MolToSmiles(mol), None)

    def sample_one(self, smiles: str) -> "list[str]":
        """Up to N_OUTPUTS distinct analogues of `smiles`, in draw order."""
        pool = {}
        self._collect(self.scaffold_sampler, smiles, pool)
        if len(pool) < N_OUTPUTS:
            self._collect(self.scaffold_generic_sampler, smiles, pool)
        return list(pool)[:N_OUTPUTS]

    def generate(
        self, input_smiles: "list[str]", is_debug: bool
    ) -> "tuple[list[list[str]], list[str], dict]":
        start_time = time.time()
        output_smiles = []
        total_smiles = 0
        for smi in input_smiles:
            try:
                row = self.sample_one(smi)
            except Exception as exc:  # one failing molecule must not sink the batch
                print(f"Mol2Mol failed on {smi!r}: {exc}", file=sys.stderr)
                row = []
            total_smiles += len(row)
            output_smiles.append(row + [""] * (N_OUTPUTS - len(row)))
        log = {
            "start": start_time,
            "end": time.time(),
            "input_smiles": input_smiles,
            "total": total_smiles,
            "expected": N_OUTPUTS * len(input_smiles),
        }
        if is_debug:
            print(
                f"Time taken in seconds: {int(log['end'] - start_time)}, molecules: {total_smiles}"
            )
        return (output_smiles, [], log)
