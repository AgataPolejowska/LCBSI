# LCBSI
Leukocytes classification from blood smear images.


## Setup the environment

Create the environment:
`conda env create -f environment.yml`

Update the environment:
`conda env update -f environment.yml`

Run the app (in the root project directory):
`python index.py`

## Models notebooks
https://github.com/AgataPolejowska/LCBSI/tree/main/notebooks


## Dataset

PBC
* 200 images for each class

RAABIN-WBC
* 200 images for each class

Total: 2000 images, 400 per class

Hugging face hub: https://huggingface.co/datasets/polejowska/lcbsi-wbc

### Models

Pretrained: https://github.com/Project-MONAI/model-zoo/releases/tag/hosting_storage_v1 

https://github.com/Project-MONAI/model-zoo/tree/dev/models/pathology_nuclei_classification 

Model zoo: https://github.com/Project-MONAI/tutorials/tree/main/model_zoo/transfer_learning_with_bundle
https://docs.monai.io/en/latest/networks.html#densenet121
https://github.com/Project-MONAI/model-zoo/tree/dev/models
