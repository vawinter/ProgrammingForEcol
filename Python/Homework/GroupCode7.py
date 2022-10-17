# -*- coding: utf-8 -*-
"""
Spyder Editor

Group Coding 7
blue code [Karen, Sydney, Josh]
purple [Tony, Sara]
green [Morgan, Veronica]
"""
import statistics

class student: #class that describes object in terms of its properties (variables)
    def __init__(self, firstName, lastName): #constructor function that allows us to send in the variable values
        self.firstName = firstName
        self.lastName = lastName
        self.test = []
        self.homework = []
        print("A new student was added")
       
    def addtest(self, tests):
        self.test.append(tests)
        #avexam = []
        #avexam.append(round(statistics.mean(exam), 2))
        self.avexam = round(statistics.mean(tests), 2)
    
    def addhomework(self, homeworks):
        self.homework.append(homeworks)
        #avhw = []
        homeworks.sort()
        homeworks.pop(0)
        #avhw.append(round(statistics.mean(homeworks), 2))
        self.avhw = round(statistics.mean(homeworks), 2)
   
    def finalGrade(self):
        return self.avexam*.4 + self.avhw*.6

#test the code:
Sydney = student("Sydney", "Bird")
Sydney.addtest([90, 80, 100])
Sydney.addhomework([80, 90, 100])
print(Sydney.finalGrade())



# Veronica and Morgan
# initisl list
studentList = []

# While lopo to get names
x = input("Do you want to enter a student? y/n: " )
while x == "y":
    firstname = input("PLease enter first name: ")
    lastname = input("PLease enter last name: ")
    studentList.append(student(firstname, lastname))
    x = input("Do you want to enter a student? y/n: " )

# Loop to add grades
for i in range(studentList):
    numTest = int(input("Please enter number of tests?: "))
    numHW = int(input("Please enter number of homeworks: "))
    for t in range(numTest):
        grade = [int(input("Please enter test grades: "))]
        studentList[i].addtest(grade)
    for h in range(numHW):    
        HWgrade = [int(input("PLease enter homework grades: "))]
        studentList[i].addhomework(HWgrade)
        
        
        
        