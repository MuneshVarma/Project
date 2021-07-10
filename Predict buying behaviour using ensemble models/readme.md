# Predict buying behaviour of customers using ensemble models
## Table of Contents
- [Overview](#Overview)
- [Problem Statement](#Problem-Statement)
- [Methodology](#Methodology)
- [Technology used](#Technology-Used)
- [Result](#Result)

## Overview
In the U.S. approximately 9% of total retail sales comes from an e-commerce website. In fact, companies like Amazon have created retail empires
off being such a huge e-commerce website. With e-commerce becoming more and more prevalent in today’s economy it is important for businesses within
this sector to understand what factors into a site visitor making a purchase, and being able to put their attention on potential customers.

## Problem Statement
Predict whether a customer will purchase from the store given data about customer’s information and past behaviour.

## Methodology
1) The target variable was binary classification in nature since we had to predict YES/NO.The train data consisted of 1.5 lakh rows and test data consisted of 50000 rows
2) The variable ID was dropped since it was different for all records of test and train data and cannot in any way 
    increase the accuracy of model. Also whether a customer purchases or not has no relation with his ID number.
3) The count of target variable was plotted which showed 'NO' value count of 114537 and 'YES' value count of 35463.
    'YES' value count was almost 3.23 times of 'NO' value counts which showed that target variable was imbalanced.
4) Data was checked for null values and varible LOYALTY_PROGRAM had approx 12% null values in train and test data. These null values was imputed with N.A
6) Since 5 of the the 7 variables were categorical in nature we used crosstab to plot the 5 variables against target variable.
  The following inferences were drawn:
  1) Customers with loyalty program have higher chance of purchasing a product
  2) Maximum customers belonged from Maharashtra followed by Uttar Pradesh, Tamil Nadu and Karnataka
  3) People with occupation as Business purchased the least.
  4) People with high income tend to purchase more and people with low income purchased the least.
  5) People who have beem customers since 2012 puchrchased the most.

7) Numerical variable:
  - Age was checked for outliers using boxplot which showed no outliers.
  - The distribution plot of age showed that people with age around 50 purchased the most and people with age around 30 purchased the least
  - Also age was plotted against INCOME_GROUP which gave the following insight
  - People of age around 50 belonged to high income group and people of age group around 30 were mostly of low income group
  
8) data preparation:
* Target variable was separated from train data
* All categorical values were label encoded.

9) Data was then splitted into training and validation set with validation size of 20% total size
10) numerical variables were scaled based on StandardScalar on both training,validation and test set

11) Model building:
we selected the following model for cross validation
  - Decision Tree, Random Forest, KNN, SVM, Adaboost and XGBoost
12) Since the data is unbalanced we used f1_micro as evaluation criteria
13) The following are the cross validation score of each model:

|Model|Cross validaiton Score|
|--|--|
|Decision Tree|0.852|
|Random Forest|0.8571|
|K Nearest Neighbors|0.8339|
|Support Vector Machine|0.79285|
|Gradient Boost|0.8581|
|Adaboost|0.8548|

## Result
Although XGBoost,Gradientb and Random Forest gave almost equal metrics score we chose Random Forest since it took less time to train and hence less time to deploy.
The predictions made from Random Forest were then exported as csv which was finally submitted for evaluation.

## Technology Used
- Jupyter Notebook
- Python

