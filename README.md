# ML_Project_Satellite_Images
Project for the "machine learning for physics" seminar at TU Dortmund Summer 2021  
[Project report](https://github.com/NicoJG/ML_Project_Protocol/blob/main/Abgabe.pdf) , [Report Repository](https://github.com/NicoJG/ML_Project_Protocol)  

# About

In this project Samuel and I built, trained and evaluated Deep Learning models for the segmentation of larger water areas on satellite images.
The dataset consisted of images for single tiles for the satellite imagery and a mask image labeling all water pixels.  
This dataset was created/collected as part of the project.  

The folder 'ml_project' contains the scripts for the data collection.  
The folder 'data' is a dummy folder with README files explaining the data that would be in the folders.  
The folder 'colab_notebooks' contains the Jupyter Notebooks used for the actual machine learning of the project done with the GPUs for Tensorflow from withing Google Colab.  

The dataset was collected with Mapbox and therefore no images of the dataset can be uploaded here.  
This is why all outputs of the notebooks were removed using 'nbstripout'. 

In order to use this project, follow the installation instructions below.
For the dataset creation use 'ml_project/dataset_creation/dataset_creation.ipynb'.
For the segmentation using machine learning use 'colab_notebooks/final_model.ipynb', 
but read 'colab_notebooks/README.md' because you need to incorporate Google Drive.  
'colab_notebooks/grid_search.ipynb' and 'colab_notebooks/grid_search_evaluate.ipynb' were used to find the optimal hyperparameters of the selected U-Net model.

# Installation

You need to have `conda` installed.
You have to execute the following commands in the main directory. (without the `$`)

```
$ conda env create -f environment.yaml
# or to updaten an existing environment:
$ conda env update -n ml_project -f environment.yaml
```

```
$ conda activate ml_project
```

```
$ pip install -e .
```

```
$ nbstripout --install
```
