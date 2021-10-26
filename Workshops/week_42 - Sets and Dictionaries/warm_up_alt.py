# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 13:00:08 2021

@author: s14754
"""



# If the text file for some reason is not stored in the same folder as the
# Python script (or you want to be able to run the code line-by-line), you
# have to specify where the text file is stored when using the open function.

# The following path to the file is specific to me and only me.
# You must replace the path with where you have stored the text file
# on your computer.
filepath = 'C:/Users/s14754/Documents/Teaching/FOR14/workshops/Week 42/populations.txt'

# Also, notice that the path can be specified using dobble backward slashes.
#filepath = 'C:\\Users\\s14754\\Documents\\Teaching\\FOR14\\workshops\\Week 42\\populations.txt'


# open file (from specified path) 
infile = open(filepath)

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


        
    



