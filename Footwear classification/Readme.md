# Footwear Classification
## Table of Contents
- [Overview](#Overview)
- [Problem Statement](#Problem-Statement)
- [Methodology](#Methodology)
- [Technology used](#Technology-Used)
- [Result](#Result)

## Overview
E-commerce has rapidly grown and their business strategies are completely based on user actions and user experiences.
Although it is completely based on users, we should also not forget to say that there is a technology bridge in between users and growth in business.
It may be Machine Learning or Deep Learning. Companies apply many image classification techniques on data to improve their catalog and give best suggestions to the users.
They need accurate product classification on their platforms for better user experience.

## Problem Statement
Given the images of a product with multiple categories, train a model which can classify the type of a product.
Data is all about images of shoes with multiple categories and data is collected from a popular Ecommerce site.
Data set consists of two folders train and test.
Train set consists of images belonging to 3 different categories of shoes in 3 different folders: Boots, Sandals and Slippers.
Test set consists of images belonging to all 3 categories of shoes into a single folder.

## Methodology
1) Path was created to train and test directories.
2) Train dataset was split into train and validation set using image_dataset_from_directory() with batch size of 32.
3) 80% was used for training and rest all for testing
4) Each channel of RGB iamge was standardised by dividing it by 255.
5) CNN architecture of the model was created from keras.Sequential() which consisted of 16 nos. 3x3 filters with same padding followed by maxpooling with stride 2 
   followed by 32 nos. 3x3 filters followed by maxpooling followed by 64 nos. 3x3 filters followed by a flatten layer connected to 128 dense neural nodes leading
   to 3 nodes for 3 classes.All of the filters had relu as their activation.
6) The model architecture was then compiled using 'adam' as optmizer, SparseCategoricalCrossentropy as loss function and accuracy metrics.
7) the model.summary() showed 1,695,267 parameters to optimize.
8) The model was then trained for 15 epochs with which was validated on validation dataset for each iteration.
9) After training we get 98.72% training accuracy and 96.13 % validation accuracy.
10) For further validation, accuracy and loss was plotted along epochs for both training and validation set which showed clearly the model optimizing.
11) This model was the used to segregate the test images into their respective categories.
12) These segreagated images were stored in different folders with folder name as class name.

## Technology Used
- Jupyter Notebook
- Python

## Result
Training accuracy of 98.72% and validation accuracy of 96.13% was achieved.


