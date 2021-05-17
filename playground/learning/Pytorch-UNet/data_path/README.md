# Carvana Image Masking Challenge

## Description 
This dataset contains a large number of car images (as .jpg files). Each car has exactly 16 images, each one taken at different angles. Each car has a unique id and images are named according to id_01.jpg, id_02.jpg ... id_16.jpg. In addition to the images, you are also provided some basic metadata about the car make, model, year, and trim.

For the training set, you are provided a .gif file that contains the manually cutout mask for each image. The competition task is to automatically segment the cars in the images in the test set folder. To deter hand labeling, we have supplemented the test set with car images that are ignored in scoring.

The metric used to score this competition requires that your submissions are in run-length encoded format. Please see the evaluation page for details, and train_masks.csv for a real example of what the encoding looks like.
File descriptions

    /train/ - this folder contains the training set images
    /test/ - this folder contains the test set images. You must predict the mask (in run-length encoded format) for each of the images in this folder
    /train_masks/ - this folder contains the training set masks in .gif format
    train_masks.csv - for convenience, this files gives a run-length encoded version of the training set masks.
    sample_submission.csv - shows the correct submission format
    metadata.csv - contains basic information about all the cars in the dataset. Note that some values are missing.

## Space
24.43 GB

## Reference 
https://www.kaggle.com/c/carvana-image-masking-challenge/data 


