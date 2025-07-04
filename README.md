# REINVENT 4 Mol2MolScaffold

Mol2MolScaffold uses REINVENT4's mol2mol scaffold prior and mol2mol scaffold generic prior to generate around 500 new molecules similar to the provided molecules. The generated molecules will be relatively similar to the input molecules.

This model was incorporated on 2024-03-08.

## Information
### Identifiers
- **Ersilia Identifier:** `eos57bx`
- **Slug:** `reinvent4-mol2mol-scaffold`

### Domain
- **Task:** `Sampling`
- **Subtask:** `Generation`
- **Biomedical Area:** `Any`
- **Target Organism:** `Not Applicable`
- **Tags:** `Similarity`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `500`
- **Output Consistency:** `Variable`
- **Interpretation:** Model generates up to 500 similar molecules per input molecule.

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


### References
- **Source Code**: [https://github.com/MolecularAI/REINVENT4](https://github.com/MolecularAI/REINVENT4)
- **Publication**: [https://chemrxiv.org/engage/chemrxiv/article-details/65463cafc573f893f1cae33a](https://chemrxiv.org/engage/chemrxiv/article-details/65463cafc573f893f1cae33a)
- **Publication Type:** `Preprint`
- **Publication Year:** `2023`
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
