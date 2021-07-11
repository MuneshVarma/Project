# Machine Learning to Predict Subscription to Bank Term Deposits 
## Table of Contents
- [Machine Learning to Predict Subscription to Bank Term Deposits](#machine-learning-to-predict-subscription-to-bank-term-deposits)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Problem Statement](#problem-statement)
  - [Methodology](#methodology)
  - [Technology Used](#technology-used)

## Overview
Term deposit is the money deposit at a banking institution
that cannot be withdrawn for a specific term or period of time (unless a penalty is paid).
Predicting if a client will subscribe to a term deposit can help increase the efficiency 
of a marketing campaign and help us understand the factors that influence a successful 
outcome (subscription) from a client.

## Problem Statement
The data is related with direct marketing campaigns of a Portuguese banking institution. 
The task is to predict whether the product (bank term deposit) would be ('yes') or not ('no') subscribed. 


## Methodology
1) The data were imported using pandas.
2) EDA of the data revealed the following:
   * The data contains both factor & numeric data types
   * It has no null values
   * Columns 'duration', 'pdays' and 'previous' contains null values
   * duration = 0 means the client has not been contacted.Therefore it is valid zero.
   * pdays= 0 means that the client has been contacted the same day. Therefore it is a valid zero.
   * previous= 0 has 35563 zeros out of 41188 i.e ~86% data is null. Therefore it can considered as a singularity.
3) Value counts of target variable showed that people who have not subscribed is almost 8 times of people who have subscribed.
    Therefore target variable is unbalanced.
4) The target variable was one hot encoded i.e. 'yes'=1 and 'no'=0.
5) Data was segragated into categorical and numerical features and primary analysis
    was performed on both.
6) Primary Analysis on Categorical Data revealed the following:
   * People with degree qualification have been contacted more.
   * People with admin,blue_collar and technician jobs have subscribed very less.
   * People with high degree have subscribed more.
   * People were contacted more in the month of May.
7) Primary Analysis on Numerical Data revealed the following:
   * Campaign and duration are not normally distributed.
   * From heatmap it appears that emp.var.rate shows high correlation with nr.employed, euribor3m 
  and cons.price.idx emp.var.rate therefore can be subsequently removed 
8) Categorical data was one hot encoded using pd.get_dummies()
9) Data was split into train and test set in 70:30 ratio.
10) Data was scaled using StandardScaler()
11) Random Forest, Logostic Regression, Adaboost and KNN model were trained.
12) Metrics were accuracy, f1_score, sensitivity,   specificity, and ROC were used
    best model selection.
13) The model was trained agained after removing correlated variables from heatmap.
14) Comparing the metrics we selected Logistic model as the best model among all. 
    
## Technology Used
- Jupyter Notebook
- Python
  
