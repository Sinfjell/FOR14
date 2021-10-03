# -*- coding: utf-8 -*-
"""
@author: Isabel Hovdahl

"""



"""
Exercise 2

FOR14 students who want to sit in the final exam must complete all practice 
assignments given throughout the semester.

Write a program that:
    - prompts a student for the number of assignments during the semester 
      and the number of assignments that the student has completed.
    - display a message confirming if the student is allowed to sit in 
      the final exam or not.
      
The program should check that the user-supplied inputs are valid, i.e. non-negative 
inputs and no more submissions than total assignments.

"""

# get inputs and convert to integers
totAssignments = int(input('Enter the number of due assignments: '))
numComplete = int(input('Enter the number of complete submissions: '))

# check that user has supplied non-negative values
if totAssignments < 0 or numComplete < 0:
    print('You cannot enter negative numbers!')
else:
    # check that the user has not supplied more submissions than assignments
    if numComplete > totAssignments:
        print('You cannot have more submissions than assignments!')
    else:
        if numComplete == totAssignments:
            print('You can take the final exam.')
        else:
            print('You cannot take the final exam.')
    
    
   
    
    
"""
Modification: 
    
Modify the code so that it uses if-elif statements instead.

"""

# get inputs and convert to integers
totAssignments = int(input('Enter the number of due assignments: '))
numComplete = int(input('Enter the number of complete submissions: '))

# check that user has supplied non-negative values
if totAssignments < 0 or numComplete < 0:
    print('You cannot enter negative numbers!')

# check that the user has not supplied more submissions than assignments
elif numComplete > totAssignments:
    print('You cannot have more complete assignments than total assignments!')
    
elif numComplete == totAssignments:
    print('You can take the final exam.')

else:
    print('You cannot take the final exam.')

    
    
    
