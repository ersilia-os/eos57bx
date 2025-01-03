# imports
import sys
import os
import csv
import json

import click
from reinvent.config_parse import read_smiles_csv_file

from mol2mol_scaffold_sampler import Mol2MolScaffoldSampler

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# This arguments is reserved for testing or
# running model locally or in notebook.
is_debug = sys.argv[3] == "True" if len(sys.argv) > 3 else False

# Name of the log file.
# Only write if `is_debug` is True.
log_file = output_file + ".json"


batch_size = 250
num_input_smiles = 0
input_smiles = None


if os.path.exists(input_file):
    input_smiles = read_smiles_csv_file(input_file, columns=0, header=True)
    num_input_smiles = len(input_smiles)

else:
    click.echo(click.style(f"[INPUT_FILE]: {input_file} doesn't exist.", fg="red"))


if not os.path.exists(os.path.dirname(os.path.abspath(output_file))):
    click.echo(
        click.style(
            f"[OUTPUT_DIR]: {os.path.dirname(output_file)} doesn't exist.", fg="red"
        )
    )

mol2mol_similarity = Mol2MolScaffoldSampler(batch_size=batch_size)

if is_debug:
    click.echo(click.style("Running scaffold prior", fg="white", bg="green"))

outputs, _, log_scaffold = mol2mol_similarity.generate(
    input_smiles=input_smiles,
    sampler=mol2mol_similarity.scaffold_sampler,
    is_debug=is_debug,
)

if is_debug:
    click.echo(click.style("Running scaffold generic prior", fg="white", bg="green"))

scaffold_generic_output, _, log_scaffold_generic = mol2mol_similarity.generate(
    input_smiles=input_smiles,
    sampler=mol2mol_similarity.scaffold_generic_sampler,
    is_debug=is_debug,
)


log = {
    "start": log_scaffold["start"],
    "end": log_scaffold_generic["end"],
    "input_smiles": log_scaffold["input_smiles"],
    "total": log_scaffold["total"] + log_scaffold_generic["total"],
    "expected": batch_size * num_input_smiles * 2,
}

assert len(outputs) == len(scaffold_generic_output)

for idx, output in enumerate(outputs):
    output.extend(scaffold_generic_output[idx])

input_len = len(input_smiles)
output_len = len(outputs)
assert input_len == output_len


HEADER = ["smiles_{0}".format(str(x).zfill(3)) for x in range(batch_size * 2)]

with open(output_file, "w", newline="") as fp:
    csv_writer = csv.writer(fp)
    # First Row: Header
    # Second Row: Generated Smiles (Output)
    csv_writer.writerows([HEADER])
    csv_writer.writerows(outputs)


if is_debug:
    with open(os.path.abspath(log_file), "w", newline="\n") as fp:
        json.dump(log, fp)
