# -*- coding: utf-8 -*-
"""
@author: Isabel Hovdahl

"""

  
"""
Exercise 1a

Modify the random number generator from last workshop so that the 
program now draws multiple random numbers within the given bounds. 

The program should now:
    - prompt the user for a lower and upper bound, and for the number 
      of draws.
    - use a while loop to draw and display the random numbers to 
      the user.

For simplicity, you can ignore checking whether the inputs are valid. 

"""  


import random


# welcome message
print('*'*49)
print('**** Welcome to the random number generator! ****')
print('*'*49)
print('\nThis program draws random numbers between an upper and lower bound.')

# get number of draws and bounds from user
num_draws = int(input('Please enter the number of random numbers: '))
lower = int(input('Please enter a lower bound: '))
upper = int(input('Please enter an upper bound: '))

print('\nYou asked for {} random number(s) between {} and {}.'.format(num_draws, lower, upper))
print('The random numbers are:\n')

i = 0

while i < num_draws:
    
    # draw and display random number
    rand_num = random.randint(lower, upper)
    print(rand_num)
    
    # increment counter
    i = i + 1 # alternatively, "i += 1"
    
    