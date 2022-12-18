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

The dataset used is created by combining the following datasets:
- RAABINC WBC

_Kouzehkanan, Zahra Mousavi, et al. "A large dataset of white blood cells containing cell locations and types, along with segmented nuclei and cytoplasm." Scientific reports 12.1 (2022): 1-14._
- PBC 

_Acevedo, Andrea; Merino, Anna; Alférez, Santiago; Molina, Ángel; Boldú,
Laura; Rodellar, José (2020), “A dataset for microscopic peripheral blood cell images for development of automatic recognition systems”, Mendeley Data, V1, doi: 10.17632/snkd93bnjr.1_

Data is split to 70% training data, 15% validation data and 15% test data.

5000 images are divided into:

- train data: 3500 images - 700 images per each class (350 for each dataset except basophil class from PBC - 550 images and from RAABIN-WBC - 150 images)
- validation data: 750 images - 150 images per each class (75 for each dataset except basophil class from PBC - 45 images and from RAABIN-WBC - 30 images)
- test data: 750 images - 150 images per each class (75 for each dataset except basophil class from PBC - 45 images and from RAABIN-WBC - 30 images)

Hugging Face Hub Dataset: https://huggingface.co/datasets/polejowska/lcbsi-wbc-ap

## Models

### DenseNet121
Pretrained model can be downloaded from: https://github.com/Project-MONAI/model-zoo/releases/tag/hosting_storage_v1 

Dataset description that the pretrained model used is available here:
https://github.com/Project-MONAI/model-zoo/tree/dev/models/pathology_nuclei_classification 

Model zoo: https://github.com/Project-MONAI/tutorials/tree/main/model_zoo/transfer_learning_with_bundle

Additional information about DenseNet121: https://docs.monai.io/en/latest/networks.html#densenet121

Other models available in MONAI: https://github.com/Project-MONAI/model-zoo/tree/dev/models


## Additional application

You can experiment with the trained vision transformer in the Hugging Face space:
https://huggingface.co/spaces/polejowska/LCBSI
