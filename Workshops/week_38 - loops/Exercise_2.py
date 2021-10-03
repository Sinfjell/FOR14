# -*- coding: utf-8 -*-
"""
@author: Isabel Hovdahl

"""

"""
Exercise 2

Use the solution proposal for the prisoner’s dilemma from last 
workshop and modify the program so that it does not terminate 
if the players enter invalid inputs (i.e. not «1» or «2»).

Modify the program so that the players are re-prompted for inputs 
until they enter valid inputs.

Ask the players for their choices, and if their choices are not valid, 
ask for new choices in a while loop.

"""


# program welcome
print('**********************************')
print("Welcome to the Prisoner's Dilemma.")
print('**********************************')

# get choice from prisoner A
choiceA = input('Prisoner A, you are up.\nPress 1 for "confess", press 2 for "stay silent": ')

# re-prompt prisoner A for choice until choice is valid
while choiceA not in ('1', '2'):
    print('Invalid input!')
    print('Prisoner A, you must choose either 1 or 2.')
    choiceA = input('Press 1 for "confess", press 2 for "stay silent": ')

# get choice from prisoner B
choiceB = input('Prisoner B, you are up.\nPress 1 for "confess", press 2 for "stay silent": ')

# re-prompt prisoner B from choice until choice is valid
while choiceB not in ('1', '2'):
    print('Invalid input!')
    print('Prisoner B, you must choose either 1 or 2.')
    choiceB = input('Press 1 for "confess", press 2 for "stay silent": ')


if choiceA == '1' and choiceB == '1':
    print('\nYou both get 2 years.')
    
elif choiceA == '1' and choiceB == '2':
    print('\nPrisoner A gets 3 years, prisoner B goes free.')
    
elif choiceA == '2' and choiceB == '1':
    print('\nPrisoner A goes free, prisoner B gets 3 years.')

else:
    print('\nYou both get 1 year.')
    
    
    
"""
Modification:
    
Modify the program so that the while loop uses a boolean flag.

"""


# program welcome
print('**********************************')
print("Welcome to the Prisoner's Dilemma.")
print('**********************************')

# initialize boolean flags
validInputA = False
validInputB = False

# re-prompt prisoner A from choice until choice is valid
print('Prisoner A, you are up!')
while not validInputA:
    
    # get choice of prisoner A
    choiceA = input('Press 1 for "confess", press 2 for "stay silent": ')

    # change boolean flag if choice is valid
    if choiceA in ('1', '2'):
        validInputA = True
        
    # else, continue loop 
    else:
        print('\nInvalid input! You must choose either 1 or 2.')
        
# re-prompt prisoner B from choice until choice is valid    
print('Prisoner B, you are up!') 
while not validInputB:
    
    # get choice of prisoner B
    choiceB = input('Press 1 for "confess", press 2 for "stay silent": ')

    # change boolean flag if choice is valid
    if choiceB in ('1', '2'):
        validInputB = True
        
    # else, continue loop 
    else:
        print('\nInvalid input! You must choose either 1 or 2.')
        

if choiceA == '1' and choiceB == '1':
    print('\nYou both get 2 years.')
    
elif choiceA == '1' and choiceB == '2':
    print('\nPrisoner A gets 3 years, prisoner B goes free.')
    
elif choiceA == '2' and choiceB == '1':
    print('\nPrisoner A goes free, prisoner B gets 3 years.')

else:
    print('\nYou both get 1 year.')
    
    

 
    
