# Anomaly Detection using PCA
## Table of Contents
- [Anomaly Detection using PCA](#anomaly-detection-using-pca)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Problem Statement](#problem-statement)
  - [Methodology](#methodology)
  - [Technology Used](#technology-used)

## Overview
In today’s world of distributed systems, managing and monitoring the system’s performance is a chore—albeit 
a necessary chore. With hundreds or thousands of items to watch, anomaly detection can help point out where 
an error is occurring, enhancing root cause analysis and quickly getting tech support on the issue.
 Anomaly detection helps the monitoring cause of chaos engineering by detecting outliers, and informing the responsible parties to act.

## Problem Statement
- [probem statement.txt](https://github.com/MuneshVarma/Projects/blob/master/Anomaly%20detection%20uisng%20PCA/problem%20statement.txt)

## Methodology
1) The data was imported using pandas.read_csv().
2) The data is preprocessed with filled missing values and scaling already perfomed.
3) Since the data is from 5 sensors for 365 days, a date column was added from '01-01-2016' to '30-12-2016'. This date column was set as index. 
4) The data was split into 

## Technology Used
- Jupyter Notebook
- Python
