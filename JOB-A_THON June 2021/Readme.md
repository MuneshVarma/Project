# JOB-A-THON June 2021
## Table of Contents
- [Overview](#Overview)
- [Problem Statement](#Problem Statement)
- [Methodology](#Methodology)
- [Technologgy used](#Technology Used)
- [Result](#Result)
- [Reference](#Reference)

## Overview
Every Year analytics Vidhya presents "JOB-A-THON" - India's Largest Data Engineering Hiring Event, where every data engineering enthusiast and big data professional will get
the opportunity to showcase their skills and get a chance to interview with top companies for leading job roles in Data Engineering, Big Data & Analytics.

## Problem Statement
An eCommerce company ComZ wants to focus on targeting the right customers with the right products to increase overall revenue and conversion rate. As part of the data engineering team, we are expected to “Develop input features” for the efficient marketing model given the Visitor log data and User Data so that further data analysis and ML models can be built on top of it

## Methodology
1) The visitorlogsdata and usertable were imported using pandas.
2) Both of these tables were checked for null values.
3) Since as per problem statement we want data of ony registered users.Therefore non registered users were removed from visitorlogsdata.
4) The data now contains close to 6.5 lakhs rows as compared to 66 lakhs that it previously had.
5) The timestamp values were in different formats. Pandas function pd.to_datetime was used to convert all datetimestamps to a single format.
6) Since the data contained empty spaces all empty spaces were replaced with np.nan values.
7) VisitDateTime column had many NaN values. These values were imputed with mean value of each respective user.
8) The data was exported into mysql using mysql-connector.
9) Rest of the queries were run in mysql in the same jupyter file.
10) A new database was created.
11) These dataframe files were then send to the database as tables with suitable datatype conversions.
12) A variable @current_date was created for ease of use of queries.
13) A dataframe was created to save the output of each query.
14) All queries were then run one by one with simultaneous saving of query output to results dataframe.
15) Finally the results dataframe was saved as a csv file.

## Technology Used
- Jupyter Notebook
- Python
- MySQL

## Result
Out of the total 6467 participants secured 141 position(top 2%)
<img src=https://github.com/MuneshVarma/Projects/blob/master/JOB-A_THON%20June%202021/Images/Rank.PNG>

## Reference
[JOB-A-THON - June 2021](https://datahack.analyticsvidhya.com/contest/job-a-thon-june-2021/)
