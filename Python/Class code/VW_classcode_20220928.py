# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 17:06:39 2022

@author: veron
"""
import tempdata
import dates

tempData = pd.read_csv("temperatureData.csv")

sampleData = pd.read_csv("sampleDates.csv")

for stream in sampleData["Site"]:
    #print(stream)
    
    date = sampleData.loc[sampleData["Site"] == stream, "Date"]
    
    hobo = tempData.loc[(tempData["StreamName"] == stream) & (tempDate["Date"] == date), "Temperature"]
