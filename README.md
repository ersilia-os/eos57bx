# REINVENT 4 Mol2MolScaffold

Generates roughly 500 analogues that preserve the scaffold of an input molecule, using the scaffold and generic-scaffold priors shipped with REINVENT 4. Loeffler and colleagues at AstraZeneca released the framework as an open reference implementation of generative design, combining recurrent and transformer architectures with reinforcement, transfer and curriculum learning. Sampling is stochastic, so repeated runs return different sets, and generated structures carry no guarantee of synthetic accessibility.

This model was incorporated on 2024-03-08.Last packaged on 2026-03-20.

## Information
### Identifiers
- **Ersilia Identifier:** `eos57bx`
- **Slug:** `reinvent4-mol2mol-scaffold`

### Domain
- **Task:** `Sampling`
- **Subtask:** `Generation`
- **Biomedical Area:** `Any`
- **Target Organism:** `Any`
- **Tags:** `Similarity`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `500`
- **Output Consistency:** `Variable`
- **Interpretation:** Up to 500 generated molecules sharing the scaffold of the input compound.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| smi_000 | string |  | Generated molecule index 0. The mol2mol or the scaffold priors from REINVENT were used |
| smi_001 | string |  | Generated molecule index 1. The mol2mol or the scaffold priors from REINVENT were used |
| smi_002 | string |  | Generated molecule index 2. The mol2mol or the scaffold priors from REINVENT were used |
| smi_003 | string |  | Generated molecule index 3. The mol2mol or the scaffold priors from REINVENT were used |
| smi_004 | string |  | Generated molecule index 4. The mol2mol or the scaffold priors from REINVENT were used |
| smi_005 | string |  | Generated molecule index 5. The mol2mol or the scaffold priors from REINVENT were used |
| smi_006 | string |  | Generated molecule index 6. The mol2mol or the scaffold priors from REINVENT were used |
| smi_007 | string |  | Generated molecule index 7. The mol2mol or the scaffold priors from REINVENT were used |
| smi_008 | string |  | Generated molecule index 8. The mol2mol or the scaffold priors from REINVENT were used |
| smi_009 | string |  | Generated molecule index 9. The mol2mol or the scaffold priors from REINVENT were used |

_10 of 500 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos57bx](https://hub.docker.com/r/ersiliaos/eos57bx)
- **Docker Architecture:** `AMD64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos57bx.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos57bx.zip)

### Resource Consumption
- **Model Size (Mb):** `296`
- **Environment Size (Mb):** `2368`
- **Image Size (Mb):** `2779.31`

**Computational Performance (seconds):**
- 10 inputs: `316.03`
- 100 inputs: `-1`
- 10000 inputs: `-1`

### References
- **Source Code**: [https://github.com/MolecularAI/REINVENT4](https://github.com/MolecularAI/REINVENT4)
- **Publication**: [https://doi.org/10.1186/s13321-024-00812-5](https://doi.org/10.1186/s13321-024-00812-5)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2024`
- **Ersilia Contributor:** [ankitskvmdam](https://github.com/ankitskvmdam)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [Apache-2.0](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos57bx
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos57bx
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
