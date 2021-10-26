# -*- coding: utf-8 -*-
"""
@author: Isabel Hovdahl

"""

"""
Exercise 2a:
    
In exercise 2 in last week’s workshop, we wrote a program that read the text 
file “nurseryrhyme.txt” and counted the number of unique words in file.

We then used lists to store the words in the file. Now, we will use sets instead.

Write a program that opens the text file, stores all the words in the text 
in a set called unique_words, and daiplays the number of unique words to the user.

"""


# initialize set to store unique words
unique_words = set()

# get filename
file = input('Enter filename (or press enter to use default file): ')
if file == '':
	file = 'nurseryrhyme.txt'

# open file
txt_file = open(file)

# for each line in the text file...
for line in txt_file:

    # ...split the line on space and store the words in a list
    words_in_line = line.split()
    
    # for each word in line...
    for word in words_in_line:
        
          # ...add the word to the set
          unique_words.add(word)
                
# close file
txt_file.close()

print('\n{} contains {} unique word(s).'.format(file, len(unique_words)))