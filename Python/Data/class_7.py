# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 16:05:30 2022

@author: veron

class 7
"""
import pandas as pd

# Load in data
ourData = pd.read_csv("MRIexampleData.csv")
print(ourData)
 
print(ourData.head(10))

# Create a new column
ourData["Brain/SL"] = ourData["Total Brain mm^3"]/ ourData["SL"]

# To save
ourData.to_csv("MRIexampleData_edited.csv", index = False)

print(ourData[["Brain/SL", "Total Brain mm^3", "SL"]].shape)