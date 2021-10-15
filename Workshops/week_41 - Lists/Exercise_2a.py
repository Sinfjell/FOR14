# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 16:01:00 2021

@author: s14754
"""

"""
Exercise 2a:
    
The file nurseryrhyme.txt contains the text for the nursery rhyme 
«Mary had a little lamb». 

Write a program that opens the text file and extracts all the words, 
storing them in a list called words.

"""

#################################### OBS #################################### 
# You are not expected to know how to open and handle text files for the 
# final exam. I show this to you because it could come handy in the future, 
# and in order to create some more interesting problems when working with 
# lists, sets and dictionaries.  
#############################################################################

# initialize list to store words
words = []

# Use the built-in open function to open the file. Notice two things:
    # First, opening the file does not actually import the content in
    # the file. Instead it creates an object that we can loop over (similar
    # to e.g. the range function).
    # Second, in order for this code to work, the file and the script must be
    # located in the same folder (and that folder must be your working
    # directory).

txt_file = open('nurseryrhyme.txt')
    
# for each line in the text file...
for line in txt_file:
    
    # ...split the line on space and store the words in a list
    words_in_line = line.split()
    
    # ...and expand the word list with the new words
    words = words + words_in_line
    
print(words)

  
       