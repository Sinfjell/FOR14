# -*- coding: utf-8 -*-
"""
@author: Isabel Hovdahl

"""

"""
Exercise 1b (more fancy print statements):
    
Expand the program from the previous exercise so that it also displays the 
average grade for each student and on each test.

"""


### Create table with grades ###

# get the dimensions of the table
students = int(input('Enter the number of students: '))
tests = int(input('Enter the number of tests: '))

# initialize the table as dictionary
table = {}

# for each student...
for i in range(students):
    
    # ...get student name
    name = input('Enter {}. student name: '.format(i + 1))
    print('\nEnter scores for {}:'.format(name))
    
    # ...initialize the scores
    scores = []
    
    # ...ask for the score on each test and append to list
    for j in range(tests):
        
        score = int(input('...Test number {}: '.format(j + 1)))
        scores.append(score)
        
    # ...add name-scores to dictionary
    table[name] = scores
    
    
### Print table with grades and averages ###

print('\nTable with grades and averages:\n') 

for name, scores in table.items():
    print('|{:10}|'.format(name), end = ' ')
    for score in scores:
        print('{:4}|'.format(score), end = ' ')
        
    # print student averages    
    student_avg = sum(scores) / len(scores)
    print('{:.1f}'.format(student_avg))

# print test averages
print(' '*12, end = ' ')

for test in range(tests):
    total = 0
    for student in table:
        score = table[student][test]
        total = total + score
    test_avg = total / students
    print('{:4.1f}'.format(test_avg), end = '  ')
        
        
        
        
