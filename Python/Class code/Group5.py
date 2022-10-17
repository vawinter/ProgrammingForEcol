# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 16:11:00 2022

@author: Josh, Morgan, Veronica

Group coding 5
"""
# print("\Problem 1: Pig latin") 

# User defines a word
pig = input("What word would you like to translate into pig latin? ")
vowel = ["a", "e", "i", "o" , "u", "y"]

# Need to find first vowel
if pig[0] not in vowel and pig[1] not in vowel:
  # Grab whole word minus first
    latin = pig[2:]
# Grab first letter
    x = pig[0:2]
# put together
    piglatin = latin.capitalize() + x + "ay"
    print("Original word: ", pig, "Pig latin: ", piglatin)
# Second if
if pig[0] not in vowel and pig[1] in vowel:
  # Grab whole word minus first
    latin = pig[1:]
# Grab first letter
    x = pig[0]
# put together
    piglatin = latin.capitalize() + x + "ay"
    print("Original word: ", pig, "Pig latin: ", piglatin)
if pig[0] in vowel:
  # Grab whole word minus first
    # latin = pig[0:]
# # Grab first letter
#     x = pig[0:2]
# put together
    piglatin = pig.capitalize() + "yay"
    print("Original word: ", pig, "Pig latin: ", piglatin)

# Question 2
print("\Problem 2: Caesar's cipher") 
import string

# Grab alphabet list
letters = string.ascii_lowercase

# Get inputs from user
word = input("Give me a lower case word: ")
param = int(input("Give me a shifting parameter: "))


# Define position
for i in range(len(word)):
       #new_var = word[i] 
       pos1=letters.index(word[i])
       newPos = int(pos1 + param)
       x = letters[newPos]
       print("Encrypted word is: ", x, end = '')


#print("Encrypted word:")
















