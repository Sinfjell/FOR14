# -*- coding: utf-8 -*-
"""
@author: Isabel Hovdahl
"""

"""
Exercise 3a:
    
The text file «textabbv.txt» contains a list of common abbreviations in the 
English language.

Write a program that opens the text file and stores the abbreviations in a 
dictionary called abbv_dict. The keys should be the abbreviations, while 
the values should be the translations.

"""


# initialize dictionary
abbv_dict = {}

# open file
abbv_file = open('textabbv.txt')

# for line in file
for abbv in abbv_file:
    
    # split line on colon
    parts = abbv.split(':')
    
    # store the parts in dictionary 
    # notice: strip() removes the newline character at the end
    abbv_dict[parts[0]] = parts[1].strip()
    
# close file
abbv_file.close()