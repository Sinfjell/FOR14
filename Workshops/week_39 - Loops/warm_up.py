# -*- coding: utf-8 -*-
"""
@author: Isabel Hovdahl

"""

"""
Warm-up:
    
Use the random number generator from exercise 3 in the last workshop, and modify 
the code so that the program does not crash if the user enters invalid inputs, 
i.e. non-integers or a lower bound that is larger than the upper bound.

"""



import random

# welcome message
print('*'*49)
print('**** Welcome to the random number generator! ****')
print('*'*49)
print('\nThis program draws random numbers between an upper and lower bound.')

# initialize variable to start while loop
moreDraws = 'Y'
# alternatively, ask user whether to start random number generator
#moreDraws = input('Do you wish to draw a random number? (Y/N): ').upper()

# draw random numbers until user decides to quit
while moreDraws == 'Y':
    
    # get bounds from user
    lower = input('Please enter a lower bound: ')
    upper = input('Please enter an upper bound: ')
    
    try:
        # convert bounds to integers
        lower = int(lower)
        upper = int(upper)
        
        # draw random number
        rand_num = random.randint(lower, upper)
        print('\nYour random draw is... {}!'.format(rand_num))

        # ask whether to continue 
        # (notice that if the user types anything but "y", the loop will terminate)
        moreDraws = input('Do you wish another draw? (Y/N): ').upper()
        
    except:
        print('\nInvalid inputs!')
        print('You can only enter integers, and the lower bound must be smaller than the upper bound.')
    
print('\nThank you for using the random number generator!')