# -*- coding: utf-8 -*-
"""
Created on Ttues Sep 27 16:13:03 2022

@author: V. Winter

Homework 6
"""
import pandas as pd
import numpy as np 

# 1. Question 1
print("\nstart Q1: Loading in data")
# Load in tha data
plants = pd.read_csv("plantData.csv")
# a. print first 5 lines
print(plants.head(5))

# b. Select the data from the length column and print them out.
print(plants[["length"]]) 

# c. Select the data from the site and treatment columns and print them out 
# together, side-by-side, two different ways. First, print with site in the first 
# column and treatment in the second column. Then reverse this so that 
# treatment is in the first column and site is in the second column.
print(plants[["site", "treatment"]])
print(plants[["treatment", "site"]])

# d. Create a volume column that is formed by multiplying the length, width, and 
# height columns together. Print it out. 
plants["volume"] = plants["length"] *  plants["width"] * plants["height"]
print(plants[["volume"]])

# e. Calculate the shrub carbon for all of the shrubs using the equation: 
 
# 1.8 + 2 * log(volume), where volume is the volume of the shrub. 
# Print out the carbon calculation results. 
plants["carbon"] = 1.8 + 2 * np.log(plants["volume"])
print(plants[["carbon"]])

# f. Select the height data for all of the plants with heights greater than 5 and print 
# out the result (just the height data)
tallPlants = plants[plants["height"] > 5] 
print(tallPlants[["height"]]) 

# g. The following code calculates the average height of a plant at each site: 
 
# dataMeans = data.groupby("site ").mean() 
# print(dataMeans["height "]) 
 
# There are two new methods here: groupby() and mean(). The groupby() 
# method is how you indicate how the mean() method should be applied. In this 
# example, it is being applied separately to each site. 
 
# Modify this code to calculate and print out the average height of a plant in each 
# treatment type, rather than site. 

dataMeans = plants.groupby("treatment").mean() 
print(dataMeans["height"])  
 
# h. Using another new method, max(), calculate the maximum width of a plant in 
# each site and print it out. 

dataMax = plants.groupby("site").max() 
print(dataMax["width"]) 


print("\nDone Q1")

# Question 2
print("\nstart Q2: Debugging")
#   Set a break point at each line (indicated here with a diamond). There are 3 variables: num, 
# total, and i. Fill out this table to show the value of each variable with each step through 
# the program, with 5 being the number you enter as input. I started it for you so you can see 
# what I mean: 

# The loop
num = int(input("Please give a number: ")) 
 
total = 1 
for i in range(num, 1, -1): 
      total *= i 
print(num, "! is: ", total, sep = "") 

print("\nend: Q 2") 

print("\nDebugging table")

### Table out debugging program:
## Step i  num  total  notes
# 1
# 2    5
# 3    5   1          Enters loop
# 4    5   5   1
# 5    5   5   5
# 6    4   5   5
# 7    4   5   20
# 8    3   5   20
# 9    3   5   60
# 10   2   5   60
# 11   2   5   120
# 12   2   5   120
# 13   2   5   120   print answer: 5! Is: 120