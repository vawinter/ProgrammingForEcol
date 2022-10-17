# -*- coding: utf-8 -*-
"""
Homework: Lesson 2
Author: Veronica Winter
Date created: 08/28/2022
Last modified: 08/28/2022
Description: data types, variable assignments, and expressions

"""

## Question 2:
# Variables
name = input("Give a name: ")
state1 = input("Name a state: ")
state2 = input("Name another state: ")
occupation = input("Name an occupation: ")
adj = input("Give an adjective: ")
adj2 = input("Give another adjective: ")
verb = input("Give another verb: " )

# Ouptut
print("My friend's name is", name, "and they are a crazy person. Why are they crazy, you ask?",
      name, "decided to MOVE from", state1, "to", state2,
      ",quit their job, and become a(n)", occupation, ". Frankly, I bet they're",
      adj, ". Now, they are starting a new job and are", adj2, "and I do not know what they were thinkging! If it were me, I would",
     verb, "and relax. Oh well! Lesson learned.")

## Question 3:
# Input meal price
mealPrice = input('What was the cost of your meal? ')
mealPrice = float(mealPrice)
# Add tax
salesTax = 0.06
# calculate tip
tip10 = mealPrice * 0.10
tip15 = mealPrice * 0.15
tip20 = mealPrice * 0.20
# give options for all potential tips + tax + meal
totalPrice1 = mealPrice + (salesTax * mealPrice) + tip10
totalPrice2 = mealPrice + (salesTax * mealPrice) + tip15
totalPrice3 = mealPrice + (salesTax * mealPrice) + tip20

# Output
print("With tax, your meal with a 10% tip would be: ", totalPrice1, ", a 15% tip would be:",
      totalPrice2, ", and a 20% tip would be:", totalPrice3, ".")   

## Question 4: 
# a clunky way to do this.....
pig1 = input("Give the first letter of a word: ")
pig2 = input("Write the rest of the word minus first letter: ")

# if i uses +, then no spaces would've been introduced    
print(pig2, pig1, "ay", sep = '')

## Question 5:
temp = input("Temperature in Fahrenheit: ")
temp = int(temp)
celsius = 5/9 * (temp-32)
print("The temperature in Celsius is:", round(celsius, 1))


# Done with homework 2













