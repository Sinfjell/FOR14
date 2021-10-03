# -*- coding: utf-8 -*-
"""
@author: Isabel Hovdahl

"""


"""
Exercise 1c

Modify the program in exercise 1b. Instead of specifying the number of words at 
the beginning of the program, the program should continue to ask the user 
for a new word until the user decides to quit the program.

The program should:
    - use a while loop that in each iteration:
        - prompts the user for word.
        - use a for loop to count the number of vowels in the word.
        - display the word and its number of vowels.
        - ask for next word unless the user decides to quit.

"""

# program greeting
print('*'*58)
print('Welcome to the vowel-counting program!\n')
print('This program counts the number of vowels in English words.')
print('*'*58)

# get first word
word = input('Enter a word (or press "q" to quit): ').lower()

# continue until user decides to quit
while word != 'q':
    
    # initialize counter
    count = 0 
    
    # loop over letters in word
    for letter in word:
        # increment counter if letter is a vowel
        if letter in ('a', 'e', 'i', 'o', 'u'):
            count = count + 1
    
    # display word and count
    print('\n"{}" contains {} vowel(s).'.format(word.capitalize(), count))
    
    # get next word
    word = input('Enter next word (or press "q" to quit): ').lower()
    
print('Thank you for using the vowel-counting program!')


    
"""
Modification: 

Modify the program so that the while loop uses a Boolean flag.

"""

# program greeting
print('*'*58)
print('Welcome to the vowel-counting program!\n')
print('This program counts the number of vowels in English words.')
print('*'*58)

    
# initialize flag
stop = False

# continue until user decides to quit
while not stop:
    
    # get word
    word = input('Enter a word (or press "q" to quit): ').lower()
    
    # change flag if user wants to quit
    if word == 'q':
        stop = True
        
    # otherwise, count number of vowels
    else:
        # loop over letters in word
        for letter in word:
            # increment counter if letter is a vowel
            if letter in ('a', 'e', 'i', 'o', 'u'):
                count = count + 1
                  
        # display word and count
        print('{} contains {} vowel(s).'.format(word.capitalize(), count))
        
print('Thank you for using the vowel-counting program!')


