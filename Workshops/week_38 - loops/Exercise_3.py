# -*- coding: utf-8 -*-
"""
@author: Isabel Hovdahl

"""

  
"""
Exercise 3

Again modify the random number generator so that the program continues 
to draw random numbers until the user decides to quit.

The program should now:
    - initialize a while loop that in each iteration:
        - prompt the user for a lower and upper bound.
        - draw and display the random number.
        - ask the user whether to continue or quit.
	
For simplicity, you can ignore checking whether the inputs are valid. 

"""  



import random

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

    # draw random number
    rand_num = random.randint(lower, upper)
    print('\nYour random draw is... {}!'.format(rand_num))

    # ask whether to continue 
    # (notice that if the user types anything but "y", the loop will terminate)
    moreDraws = input('Do you wish another draw? Type "Y" to continue, and "N" to quit: ').upper()
    
print('\nThank you for using the random number generator!')
    





   
    





    
    
    
    
    