<img src="http://imgur.com/1ZcRyrc.png" style="float: left; margin: 20px; height: 55px">

# Project 2: Ames Housing sale price

## __Problem Statement__:

Create a regression model based on the _**Ames Housing Dataset**_. This model will predict the price of a house at sale. <br><br>
Using this model, my group has decided to develop a website where homeowners who wish to sell their property can use to find out what `SalePrice` to sell their property for. The website will have specific fields for visitors to fill and submit details about their property. Using our proprietary machine learning algorithm, the website will generate an estimate visitors can use as reference to quote their property `SalePrice`. 

## __Background:__
Project 2 involves using a well-known _**Ames housing data**_ to create a regression model that predicts the price of houses in Ames, IA. The Ames Housing Dataset is an exceptionally detailed and robust dataset with over 80 columns of different features relating to houses. I am allowed to use any and all features that are present in this dataset. <br><br> This is also a [Kaggle challenge](https://www.kaggle.com/competitions/dsi-us-11-project-2-regression-challenge/overview), so I would be making one or more submissions towards this regression challenge. Kaggle leaderboard standings will be determined by root mean squared error (`RMSE`).

## __Data provided:__
There are 3 datasets included in the [`datasets`](datasets/) folder for this project.
* [`sample_sub_reg.csv`](datasets/sample_sub_reg.csv): An example of a correctly formatted submission for this challenge (with a random number provided as predictions for `SalePrice`). My submission to Kaggle must match this format
* [`test.csv`](datasets/test.csv): Contains Kaggle test data. This data is fed into my regression model to make predictions for Kaggle submission. Target variable (`SalePrice`) is excluded from this data.
* [`train.csv`](datasets/train.csv): Contains all of the training data for my model. 
* [Data Dictionary]((http://jse.amstat.org/v19n3/decock/DataDocumentation.txt))

## __Goal:__
To predict the `SalePrice` for each house. For each Id in the test set, I must predict the value of the SalePrice variable.

## __Contents:__
1. Data validation, exploration and cleaning
1. Feature engineering
1. Feature selection
1. Model and prediction
1. Business case groupwork
---
### Data validation, exploration and cleaning
