# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 00:10:23 2023

@author: Tim_Maundu
"""
#Import library
import pandas as pd

#Read the csv file
sales = pd.read_csv('transaction.csv', sep=';')

#Calculation & Column creation
sales['TransactionCostPerItem'] = sales['CostPerItem'] * sales['NumberOfItemsPurchased']

sales['TransactionSellPerItem'] = sales['SellingPricePerItem'] * sales['NumberOfItemsPurchased']

sales['TransactionProfitPerItem'] = sales['TransactionSellPerItem'] - sales['TransactionCostPerItem']


sales['ProfitMargin'] = sales['TransactionProfitPerItem'] / sales['TransactionCostPerItem']

#round off the profit margin values
sales['ProfitMargin'] = round(sales['ProfitMargin'], 2)

#Column Combining
#Convert the interger to strings before combing
day = sales['Day'].astype('str')
year = sales['Year'].astype('str')

#Create a Date Column by combining columns
sales['Date'] = day + '-' + sales['Month'] + '-' + year

#Seperate the data in columns
client = sales['ClientKeywords'].str.split(',' ,expand = True)

#Create New separate Column
sales['ClientAge'] = client[0]
sales['ClientType'] = client[1]
sales['ClientContract'] = client[2]

#Make Replacement on the columns unwanted data 
sales['ClientAge'] = sales['ClientAge'].str.replace('[', '')
sales['ClientContract'] = sales['ClientContract'].str.replace(']', '')

#Make Changes in the Sentenses to lowercase
sales['ItemDescription'] = sales['ItemDescription'].str.lower()

#Delete Unwanted/ Uneeded Columns
sales = sales.drop('ClientKeywords', axis = 1)
sales = sales.drop('Day', axis = 1)
sales = sales.drop('Year', axis = 1)

# Add new dataset to yout dataframe
season = pd.read_csv('season.csv', sep =';')

#Use the Merge function from pandas
sales = pd.merge( sales, season, on = 'Month')

#Delete the Month Column that i had to merge with season dataset
sales = sales.drop('Month', axis = 1)


#Export the file
sales = sales.to_csv('ValueInc_Cleaned.csv', index = False)

