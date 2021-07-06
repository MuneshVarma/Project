# Predicting employees in need of medical treatment
## Table of Contents
- [Overview](#Overview)
- [Problem Statement](#Problem-Statement)
- [Methodology](#Methodology)
- [Technology used](#Technology-Used)
- [Result](#Result)
- [Reference](#Reference)

## Overview
The following is the problem statement for Imarticus Data Science Hackathon May 2021 which is hosted at Skillenza every half year.

## Problem Statement
A drastic thing happened and ABCXYZ123 Technical Solutions have lost one of their important employees.
The company is now very concerned about the health of their employees and would want you to find that set of employees who are in need or may be in need of treatment,
taking into account multiple attributes that are already stored in the database. So buckle up the wellness of your employees is in your hand.

## Methodology
1) Data was imported using pandas.readcsv
2) Data was checked for null values
3) Columns ('State') which showed no relation with treatment were dropped
4) Crosstab was performed on every categorical data to find any influence of the column on target treatment.
5) Histogram was plotted for numerical data('Age') to check for distribution.
6) Categorical data was then encoded using label encoder and one hot encoder.
7) Data was then split into train and test set in the ration 80:20.
8) Standard scalar was used on train data using fit transform and on test data using transform.
9) Decision Tree, Random Forest, KNN, SVM, GradientBoost, Adaboost, xgboost and voting classifier algorithms were used. 
10) Customizable functions were made for each algorithm which performed cross validation using randomizedsearchcv and returned cross validation scores.
11) Metrics like accuracy,f1_score, sensitivity, specificity and ROC AUC were compared for every model.
12) Based on the above metrics SVM was chosed to be the best.
13) This optimzied model was used to predict values on test data and create a csv file for submission.


## Technology Used
- Jupyter Notebook
- Python

## Result
Employees who needed medical treatment were predicted with 74% accuracy.
Secured 18th rank out of the total 411 participants.

## Reference
[Imarticus Data Science Hackathon - May 2021](https://skillenza.com/challenge/imarticus-data-science-hackathon-may-2021)
