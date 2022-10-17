###################################X
#--- Programming for ecologists ---X
#-Program: R Homework Lesson 1 & 2-X 
#------- Author: V. Winter --------X
#-------  Created: 10/12/2022 -----X
#-- Description:  Answers to first-X
#-------- R HW assignment ---------X 
###################################X
#------ Last edited xx/xx/2022 ----X
###################################X

# Question 2 ----
# 2)   (10pts) Prime numbers. Write a program that prints out all the prime numbers between 1 
# and 100 (inclusive). For example, 5 is prime because the only numbers that evenly divide 
# into 5 are 1 and 5. 6, however, is not prime because 1, 2, 3 and 6 are all divisors of 6. 
# Technically, only numbers greater than 1 can be considered prime numbers. The difference 
# between how R and Python do sequences in the for loop is really critical for this problem. 

## Answer ----
# Create list of numbers from 1 to 100
prime <- c(0:100)

# iterate over numbers in loop
for(i in prime){
  if (i < 2)
    next
  else {
    f = FALSE
    for (temp in 2:sqrt(max(prime)))
      if (i %% temp == 0 && i > temp){
        f = TRUE
        break
      }
    if (f) next
  }
  # print statement
  cat(i, end = "")
}


# Question 3: You have three vectors ---- 
a <- seq(0, 10, 2) 
b <- seq(10, 100, 10) 
c <- c(1, 15, 4, 20, 10, 6) 

# Given these three vectors, do the following: 
# a. Find which numbers in vector c are greater than or equal to the max number in vector a. ---- 
## Answer ----
# Finding which numbers are greater
bigger <- c[c >= max(a)]
# print statement
cat("number(s) in c that are greater than or equal to max(a):", bigger)

# b. Find which numbers in vector c are in both vector a and vector b ----
## Answer ----
both_ab <- c[c %in% b & c %in% a]
# print statement
cat("number(s) in c that are also in a and b:", both_ab)

# c. Convert the numbers in vector b from Fahrenheit to Celsius. ----
##  Answer ----

# Establish the formula in a function:
#   I am just putting the formula into the wrapper of function() so it will
#  loop over the list of variables and calculate for each variable the new temperature
#  in Celsius
convert <- function(f){
  c = 5/9 * (f - 32)
  }

# Apply function to list b
converted_listb <- convert(f = b)
# print statement
cat("numbers in b converted from F to C:", round(converted_listb, 2))

# 4) Tidyverse data manipulation practice. ----

# Load in libraries  
#install.packages("AppliedPredictiveModeling") 
library("AppliedPredictiveModeling") 
library(tidyverse)

# Load in data
data(abalone) 
Abalone <- as_tibble(abalone) 

# a. Find mean and std error by sex ----
# Define std error fun
se <- function(x) { 
  # standard standard error function 
  sd(x) / sqrt(length(x)) 
}

## Answer ----
# Find mean and std error per sex
abalone_sum <- Abalone %>%
  # select desired columns
  select(Type,
         Rings) %>% 
  # group by sex
  group_by(Type) %>% 
  # find mean and std error for each
  summarise(meanRings = mean(Rings),
            seRings = se(Rings)) %>%
  # format as tibble
  as_tibble()
abalone_sum

#b. Create a new column called “volume” ----
#   Assuming the shell is a cylinder by using the formula: 
#   volume = pi * r2 * h. Remember that r = diameter / 2.

# d and h are user defined variables
vol <- function(d, h){
  # calculate the volume with the formula provided
  x = pi * (d/2)^2 * h
  return(x)
} 

## Answer ----
abalone_vol <- Abalone %>% 
  # Create a column and apply the function above
  mutate(volume = vol(d = Diameter, h = Height)) %>% 
  as_tibble()
abalone_vol

# c. Use piping to select all males with shells with more than 10 rings and then count how 
#   many males there are. Do the same thing for females. ----

## Answer ----
shells <- Abalone %>% 
  # grab columns
  select(Type,
         Rings) %>% 
  # Remove intermediates
 # filter(!(Type ==  "I")) %>% 
  # group by sex
  group_by(Type) %>% 
  # filter shells with greater than 10 rings
  filter(Rings > 10) %>% 
  #count how many by sex
  count(Type)
shells

# d. Make a new tibble with just the Sex (called “Type” here), Height and Diameter. ----
## Answer ----
Sex <- Abalone %>%
  # Select desired columns
  select(Type,
         Height,
         Diameter) %>% 
  as_tibble()
Sex

