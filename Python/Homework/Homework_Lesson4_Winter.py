# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 12:40:08 2022

Homework 4: Functions

Veronica A. Winter
"""
#-----------------------------------------------------------------------------# 
# # # Question 1: Rock-Paper-Scirssorsd
# print("\nQuestion 1: Rock-Paper-Scissors") 

# # Define user choice, define comp choice, pick winner:
import random  

# Define variables
picks = ["rock", "paper", "scissors"]

# Function
# User:
def user():
    # make a decision
    print("Do you want to play a game?")
    user_input = input("Pick 1! (rock, paper, scissors): ")
    return user_input   
# computer
def computer():
    # randomly choose one variable
    computer_pick = random.choice(picks)
    return(computer_pick)

# who won? 
def winner(user, computer):
# for counting
    win = 0
    lose = 0
    draw = 0
  # same, then draw
    if user == computer:
      print("Results: Draw!")
      draw += 1
        # if user picks rock and comp picks scissors
    elif user == "rock":
          if computer == "scissors":
              print("Results: Rock > scissors! You win!")
              win += 1
          else:
              print("Results: Paper > rock! You lose.")
              lose += 1
        # if user picks paper and comp picks rock
    elif user == "paper":
          if computer == "rock":
              print("Results: Paper > rock! You win!")
              win +=1
          else:
              print("Results: Scissors > paper! You lose.")
              lose +=1
    elif user == "scissors":
          if computer == "paper":
              print("Results: Scissors > paper! You win!")
              win += 1
          else:
            print("Results: Rock > scissors! You lose.")
            lose += 1
                             
   
# Main program
# while loop to keep playing
#   for counting
win = 0
lose = 0
draw = 0

while True:
    one = user()
    print("You:", one, sep = "")
    two = computer()
    print("Computer:", two, sep = "")
    winner(one, two)
    again = input("Play again? (y/n): ")
    if again.lower() != "y":
        print("You won:", win, "You lost:", lose, "You tied:", draw, sep = "\n")
        break 
    
    
# Question 2
print("\nQuestion 2: Permutation test") 
# Using this data: 
Group1 = [1, 4, 5, 3, 1, 5, 3, 7, 2, 2] 
Group2 = [6, 7, 9, 3, 5, 7, 8, 10, 12] 
 
# Write a program that will output: 
# a) The mean difference between the two groups – write this as a function. 
# b) How many times out of 1000 a difference this large or larger could have occurred due to 
# chance. I recommend starting with a smaller number of repetitions first to be sure the 
# code is working. 
# c) The p-value for this permutation test - it’s the answer to part (b) divided by the number 
# of permutations.  
 
# Hint: There is an append function, but you can also combine, or join, two lists with the “+” 
# operator: 
combinedGroups = Group1 + Group2 

# Defining variables I am using in funciton
diff_sum = 0
diff = 0
pval = 0
x1 = 0
x2 = 0
mean_x1 = 0
mean_x2 = 0

# Function
def mean_fun(*nums):
    # a. find mean
    mean1 = sum(Group1) / len(Group1)
    mean2 = sum(Group2) / len(Group2)
    diff = round(abs(mean1 - mean2), 2)
    print("The difference between the groups was: ", diff, sep = '')
    # b. Repeat over 1000x
    # count how manny times it occurs
    same = 0
    for i in range(1000):
       # print("\nNumbers", i + 1, ":", sep = '', end = "\t")
       # randomly sample a number from the combined group
        x1 = random.choices(combinedGroups, k=10)
        x2 = random.choices(combinedGroups, k=10)
        # find new means
        mean_x1 = sum(x1) / len(x1)
        mean_x2 = sum(x2) / len(x2)
        # find te difference
        diff_sum = abs(mean_x1 - mean_x2)
      # print(diff_sum)
        if diff_sum >= diff:
                same += 1
    print("A difference >= this occured ", same, " times out of 1000 by chance", sep = '')          
    # c. p-value
    pval =  same / 1000
    print("p-value is: ", pval, sep = '')
  
# Main program 
mean_fun()


## More code for question 1
# def winner():
#     while True:
#         # for counting
#             win = 0
#             lose = 0
#             draw = 0
#           # same, then draw
#             if user == computer:
#               print("Results: Draw!")
#               draw += 1
#                 # if user picks rock and comp picks scissors
#             elif user == "rock":
#                  if computer == "scissors":
#                       print("Results: Rock > scissors! You win!")
#                       win += 1
#                  else:
#                       print("Results: Paper > rock! You lose.")
#                       lose += 1
#                 # if user picks paper and comp picks rock
#             elif user == "paper":
#                  if computer == "rock":
#                       print("Results: Paper > rock! You win!")
#                       win +=1
#                  else:
#                       print("Results: Scissors > paper! You lose.")
#                       lose +=1
#             elif user == "scissors":
#                  if computer == "paper":
#                       print("Results: Scissors > paper! You win!")
#                       win += 1
#                  else:
#                     print("Results: Rock > scissors! You lose.")
#                     lose += 1
#                     again = input("Play again? (y/n): ")
#                     if again.lower() != "y":
#                         print(win, lose, draw)
#                         break 
 


# one = user()
# print("You:", one, sep = "")
# two = computer()
# print("Computer:", two, sep = "")
# winner()
