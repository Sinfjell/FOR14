# -*- coding: utf-8 -*-
"""
@author: Isabel Hovdahl

"""



"""
Exercise 1b

Modify the program in exercise 1a. Instead of re-starting the program for 
each new word, the program should display the number of vowels in a word for 
a specified number of words.

The program should:
    - prompt the user for a number of words.
    - prompt the user for each word.
    - for each word, display the number of vowels in that word.

"""

# program greeting
print('*'*58)
print('Welcome to the vowel-counting program!\n')
print('This program counts the number of vowels in English words.')
print('*'*58)

# get number of words and convert to integer
no_words = int(input('Enter the number of words: '))

for i in range(no_words):
    
    # get word
    word = input('Please enter a word: ') # simple solution
    #word = input('Enter word number {}: '.format(i + 1)) # more fancy solution
    
    # initialize counter
    count = 0 
    
    # loop over letters in word
    for letter in word:
        # increment counter if letter is a vowel
        if letter in ('a', 'e', 'i', 'o', 'u'):
            count = count + 1
          
    # display word and count
    print('\n"{}" contains {} vowel(s).'.format(word.capitalize(), count))    

