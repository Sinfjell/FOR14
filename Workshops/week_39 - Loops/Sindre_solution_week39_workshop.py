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
    lower = int(input('Please enter a lower bound: '))
    upper = int(input('Please enter an upper bound: '))

    if lower != int: 
        print("Your lower input is  not an integer.")
        lower = int(input('Please enter a lower bound: '))

    elif upper != int: 
        print("Your upper input is  not an integer.")
        upper = int(input('Please enter a upper bound: '))
        
    else: 
        # draw random number
        rand_num = random.randint(lower, upper)
        print('\nYour random draw is... {}!'.format(rand_num))

    # ask whether to continue 
    # (notice that if the user types anything but "y", the loop will terminate)
    moreDraws = input('Do you wish another draw? Type "Y" to continue, and "N" to quit: ').upper()
    
print('\nThank you for using the random number generator!')
    