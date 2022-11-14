# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 16:06:54 2022

@author: veron
"""
# Load in dependencies
import sqlite3

# creating a conn to a db
con = sqlite3.connect("Comte_et_al_2016.db")

# Query and execution
cursor = con.execute("SELECT DISTINCT Basin FROM site")

print("Basin\n")
for row in cursor:
    print(row[0])

con.close()    
