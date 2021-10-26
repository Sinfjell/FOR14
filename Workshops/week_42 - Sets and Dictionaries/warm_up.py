# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 13:39:29 2021

@author: s14754
"""

# Notice that this script will only work if:
    # "population.txt" and "Exercise_1.py" are saved in the same folder
    # AND
    # The script is run by pressing the "Run file" button

# This is because Python must know where to find the file. As a default, 
# Python will look for the text file in the current working directory. 
# By pressing the "Run file" button, the working directory is
# automatically set to be the folder where the Python script is saved. 

# To see current working directory, execute this code:
# import os
# print(os.getcwd())
    
# open file (from current working directory)
infile = open('populations.txt')

records = {}

# for each line in file...
for line in infile:

    # ...extract country name and population
    fields = line.split(':')
    country = fields[0]
    population = int(fields[1].replace(',', ''))
    
    # ...and add to dictionary
    records[country] = population

infile.close()

for country, population in records.items():
    print('{:22} {:12}'.format(country, population))


        
    


