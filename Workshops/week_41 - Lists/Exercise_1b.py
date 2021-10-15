# -*- coding: utf-8 -*-
"""
@author: Isabel Hovdahl

"""

"""
Exercise 1b:
    
Write a program that creates a table with the tests scores of students. 
The table should be in the form of a nested list where each sublist 
contains the tests scores for a spesific student. 

The program should:
    - prompt the user for the number of students and the number of tests that 
      each student has taken.
    - for each student:
        - prompt the user for the scores on each of the tests.
        - store the test scores in a nested list called table.

"""

# get the dimensions of the table
students = int(input('Enter the number of students: '))
tests = int(input('Enter the number of tests: '))

# initialize the table
table = []

# for each student...
for student in range(students):
    print('\nEnter scores for student number {}:'.format(student + 1))
    
    # ...initialize the scores
    scores = []
    
    # ...ask for the score on each test and append to list
    for test in range(tests):
        
        score = int(input('...Test number {}: '.format(test + 1)))
        scores.append(score)
        
    # ...append list with scores to table
    table.append(scores)
    
    
# print table
print('\nThis is the final table with grades:')
for row in table:
    print(row)