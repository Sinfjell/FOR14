# -*- coding: utf-8 -*-
"""
@author: Isabel Hovdahl

"""

"""
Exercise 1b:
    
Expand the program from the previous exercise so that it also displays the 
average grade for each student and on each test.

"""


### Create and print table ###

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

print('\nTABLE WITH GRADES\n') 
for name, scores in table.items():
    print('|{:8}|'.format(name), end = ' ')
    for score in scores:
        print('{:4}|'.format(score), end = ' ')
    print()


### Calculate and print averages ###
    
print('\nAVERAGE GRADES\n')
    
# for each student...
for student in table:
    
    # ...extract list with student scores
    scores = table[student]
    
    # ...and calculate average score for student
    student_avg = sum(scores) / len(scores)
    print('{:8}: {:.1f}'.format(student, student_avg))
    
print()

# for each test...
for i in range(tests):
    
    # ...initialize total score
    total = 0
    
    # ...add score for each student on test to total
    for student in table:
        total = total + table[student][i]
        
    # ...and calculate test average
    test_avg = total / tests    
        
    print('{:8}: {:.1f}'.format('Test ' + str(i + 1), test_avg))
   
        
            
            
    