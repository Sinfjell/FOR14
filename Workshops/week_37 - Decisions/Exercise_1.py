# -*- coding: utf-8 -*-
"""
@author: Isabel Hovdahl

"""

"""
Exercise 1

Write a program that draws a random number (integer) between a lower and upper bound. 
The program should:
    - prompt the user for a lower and upper bound.
    - check that the user-supplied values are valid.
    - draw and display the random number to the user.

"""



### Alternative 1 (random module + nested if-else statement)

import random

# welcome message
print('*'*49)
print('**** Welcome to the random number generator! ****')
print('*'*49)
print('\nThis program draws a random number between an upper and lower bound.')

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
    
else:
    print('\nInvalid inputs!')
    print('You can only enter whole numbers.')
    
    
    
    
    
### Alternative 2 (numpy module + try-except statement)

import numpy as np # give numpy an alias

# welcome message
print('*'*49)
print('**** Welcome to the random number generator! ****')
print('*'*49)
print('\nThis program draws a random number between an upper and lower bound.')

# get bounds from user
lower = input('Please enter a lower bound: ')
upper = input('Please enter an upper bound: ')

# assume that the user has entered digits only and that the bounds are valid
try:
    # convert inputs to int
    lower = int(lower)
    upper = int(upper)
    
    # draw random number
    rand_num = np.random.randint(lower, upper)
    print('\nYou asked for a random number between {} and {}.'.format(lower, upper))
    print('Your random draw is... {}!'.format(rand_num))
    
except:
    print('\nInvalid inputs!')
    print('You can only enter numbers, and the lower bound must be smaller than the upper bound.')
    
    



    
    
