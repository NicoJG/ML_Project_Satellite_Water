# Notebooks containing the model building, training and evaluation  

Those notebooks were used with Google Colab and their GPU's for tensorflow.

The segmentation of satellite images for water were done with a convolutional neural network using a UNet structure. (Main Model)
As a second model a Random Forest was used pixelwise, after extracting gradient information of the image. (Alternative Model)

In order for those to work the dataset needs to be in a zip on your Google Drive.  
So a zip containing dataset/images/... must be at ML_Project_Satellite_Images/data/current_dataset.zip in your Google Drive.  

Most of those notebook are just trying out different things.

The final project was done with the notebooks 'final_model.ipynb','grid_search.ipynb' and 'grid_search_evaluate.ipynb' in the root folder.  

Outputs are deleted because of copyright reasons of the Mapbox images.
