# -*- coding: utf-8 -*-
"""
@author: Isabel Hovdahl

"""


"""
Exercise 1a

Most words in the English language contain vowels (a, e, i, o, u). 
Some of the exceptions are “shh”, “by” and “hmm”.  

Write a program that determines the number of vowels in an English word. 
The program should:
    - prompt the user for an English word.
    - display the number of vowels in that word.

"""

# program greeting
print('*'*58)
print('Welcome to the vowel-counting program!\n')
print('This program counts the number of vowels in English words.')
print('*'*58)

# get word
word = input('Please enter a word: ')

# initialize counter
count = 0 

# loop over letters in word
for letter in word:
    # increment counter if letter is a vowel
    if letter in ('a', 'e', 'i', 'o', 'u'):
        count = count + 1
            
# display word and count
print('\n"{}" contains {} vowel(s).'.format(word.capitalize(), count))




            
    
        
    


    
    
    




