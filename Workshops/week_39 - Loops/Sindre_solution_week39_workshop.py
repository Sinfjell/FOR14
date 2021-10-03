#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 07:53:52 2021

@author: sinfjell
"""

import random

#%%
### Warm up! ###


# welcome message
print('*'*49)
print('**** Welcome to the random number generator! ****')
print('*'*49)
print('\nThis program draws random numbers between an upper and lower bound.')

# initialize variable to start while loop
#moreDraws = 'Y'
# alternatively, ask user whether to start random number generator
moreDraws = input('Do you wish to draw a random number? Type "Y" to continue, and "N" to quit: ').upper()

# draw random numbers until user decides to quit
while moreDraws == 'Y':
    
    # get bounds from user
    lower = input('Please enter a lower bound: ')
    upper = input('Please enter an upper bound: ')
    
    # check that the user has entered digits only
    if lower.isdigit() and upper.isdigit():
        
        # convert inputs to int
        lower = int(lower)
        upper = int(upper)

        
        # check that the user has entered valid bounds
        if lower > upper:
            print('\nInvalid inputs!')
            print('You must enter a lower bound that is lower than the upper bound.')
        
        else:
            # draw random number
            rand_num = random.randint(lower, upper)
            print('\nYou asked for a random number between {} and {}.'.format(lower, upper))
            print('Your random draw is... {}!'.format(rand_num))
            
            rand_num = random.randint(lower, upper)
            print('\nYour random draw is... {}!'.format(rand_num))
            
            # ask whether to continue 
            # (notice that if the user types anything but "y", the loop will terminate)
            moreDraws = input('Do you wish another draw? Type "Y" to continue, and "N" to quit: ').upper()
            
    else:
        print('\nInvalid inputs!')
        print('You can only enter whole numbers.')
  
print('\nThank you for using the random number generator!')

#%% 
# Exercise 1a

word = input("Write out a english word: ")
count = 0
 
for vowel in word :
    if vowel in ("a", "e", "i", "o", "u"):
        count = count + 1

    
print("In your selected word, there are {} vowels".format(count))



#%%
# Exercise 1b

sentence = int(input("How many words should we test for vowals?: "))
count = 0
i = 0

# Loop will run the amount of times = sentence 

for i in range(sentence) :
    word = input("Write out a english word: ")
    i = i + 1
    
    # Testing for vowels in a word
    for vowel in word :
        if vowel in ("a", "e", "i", "o", "u"):
            count = count + 1
    
    print("In your {}. word, there are {} vowels".format(i, count))        
        
#%% Exercise 1c

count = 0
i = False

# Loop will run the amount of times = sentence 

while i == False :
    word = input("Write out a english word: ")
    i = i + 1
    
    # Testing for vowels in a word
    for vowel in word :
        if vowel in ("a", "e", "i", "o", "u"):
            count = count + 1
    
    print("In your {}. word, there are {} vowels".format(i, count))
    moreWords = input('Do you wish another draw? Type "Y" to continue, and "N" to quit: ')             
    if moreWords == "Y": 
        i == False 
    else: 
        i == True
        
print("Thanks for the time! Bye!")        

#%% Exercise 2
cont = True
total = 0

while cont == True :
    no_exam = int(input("How many exams?"))
    
    # Ask the user for the grades
    for i in range(no_exam):
        i = i + 1
        score = int(input("Grade {}: ".format(i)))
        total = total + score            
        i = i + 1    
    
    average = total / no_exam
    print("Your average score is {}".format(average))
    
    another_student = input("Do you want to do this for another student? Type Y to continue, and N to quit")
    if another_student == "Y":
        cont == True
    else: 
        cont == False
        









    