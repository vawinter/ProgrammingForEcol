# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 10:04:49 2022

@author: Veronica Winter

HW. 5: Strings and regular expressions
"""

# Question 1
print("\nQ 1: encoding/decoding program")

import string
import random

# Part 1a: print backwards
print("\nQ 1a: print backwards")
# User input
word = input("Please give me a word to encode: ")
# Find length of word
length = len(word)
# Print backwards: start = last position, stop = first
backwards = word[length::-1]
print("Backwards?: ",backwards, sep = "\n")

# Past 1b: Now, lets encrypt
print("\nQ 1b: encrypt")
# Grab alphabet list
letters = string.ascii_lowercase
# Encrypt word
print("New word is: ")
for i in range(len(word)):
      # Grab random letter
        random_let = random.choice(string.ascii_lowercase)
      # Find position in alphabet
        newWord = word[i] + random_let
        # Combine
        print(newWord, end ='')
        
# Decode (which is just printing the original?)
print("\nOriginal word is: ",word, sep = "\n")
       
# Question 2
import re
print("\nQ 2: DNA sequences")      

# Input the string
dna = "ttcacctatgaatggactgtccccaaagaagtaggacccactaatgcagatcctgtgtgtctagctaagatgtattattctgctgtggatcccactaaagatatattcactgggcttattgggccaatgaaaatatgcaagaaaggaagtttacatgcaaatgggagacagaaagatgtagacaaggaattctatttgtttcctacagtatttgatgagaatgagagtttactcctggaagataatattagaatgtttacaactgcacctgatcaggtggataaggaagatgaagactttcaggaatctaataaaatgcactccatgaatggattcatgtatgggaatcagccgggtctcactatgtgcaaaggagattcggtcgtgtggtacttattcagcgccggaaatgaggccgatgtacatggaatatacttttcaggaaacacatatctgtggagaggagaacggagagacacagcaaacctcttccctcaaacaagtcttacgctccacatgtggcctgacacagaggggacttttaatgttgaatgccttacaactgatcattacacaggcggcatgaagcaaaaatatactgtgaaccaatgcaggcggcagtctgaggattccaccttctacctgggagagaggacatactatatcgcagcagtggaggtggaatgggattattccccacaaagggagtgggattaggagctgcatcatttacaagagcagaatgtttcaaatgcatttttagataagggagagttttacataggctcaaagtacaagaaagttgtgtatcggcagtatactgatagcacattccgtgttccagtggagagaaaagctgaagaagaacatctgggaattctaggtccacaacttcatgcagatgttggagacaaagtcaaaattatctttaaaaacatggccacaaggccctactcaatacatgcccatggggtacaaacagagagttctacagttactccaacattaccaggtaaactctcacttacgtatggaaaatcccagaaagatctggagctggaacagaggattctgcttgtattccatgggcttattattcaactgtggatcaagttaaggacctctacagtggattaattggccccctgattgtttgtcgaagaccttacttgaaagtattcaatcccagaaggaagctggaatttgcccttctgtttctagtttttgatgagaatgaatcttggtacttagatgacaacatcaaaacatactctgatcaccccgagaaagtaaacaaagatgatgaggaattcatagaaagcaataaaatgcatgctattaatggaagaatgtttggaaacct" 

# how many occurances of 'gagg'
searchString = 'gagg'
numOccurences = dna.count(searchString) 

# first occurance of 'atta'
searchString2 = 'atta'
firstOccurrence = dna.find(searchString2)

# length of sequence
seq = len(dna)

# find GC content [w/ regualr expression?]
# # I couldn't remember if this was RE or not, so I used RE just in case....
numGC = re.findall("[gc]", dna)
# Get %
# divig length of gc content by sequence length, multiply by 100, round to 2nd decimal
totalPercent = round(len(numGC)/seq * 100, 2)

# print statements
print("There are", numOccurences, "occurance(s) of '" +  
        searchString + "'.")
print("The starting position of the first 'atta' is:",    
  firstOccurrence) 
print("The length of the sequence is", seq, "base pairs long.")
print("The GC content is",totalPercent, "%")

# Question 3
import re 

print("\nQ 3: Regular expressions")
# The string
string = "We use a state-of-the-art method, magnetic resonance imaging, to get accurate volumetric data for 2 sensory processing regions, the olfactory bulbs and optic tecta. We found a tight correlation between ecology and the size of these brain regions relative to total brain size in 2 lakes with intact species pairs."

print("\nPart a")
# (a) How many times is the word “brain” found in this string?
searchWord = "brain" 
brain = string.count(searchWord) 
print("Brain ocurs", brain, "time(s) in the string")

print("\nPart b")
# (b) Split the sentences up into clauses. In other words every time there is punctuation (, or 
# .) split the string. 
StSplit = re.split(",", string) 
print(StSplit) 

print("\nPart c")
# (c) Remove all five-letter words. 
five = re.split(r'\b\w{5}\b', string)
print(five)

#  Done!

print("\nFin: hw 5.")

       