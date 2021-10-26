# -*- coding: utf-8 -*-
"""
@author: Isabel Hovdahl
"""

"""
Exercise 1a:
    
In exercise 1 last week, you were asked to write a program that asked the user 
to supply a table of grades. The table was stored in a nested list, where 
each sublist contained the grades for each student.

Now, modify the solution proposal from last week, so that the table of grades 
is instead stored in a dictionary. 

Write a program that:
    - prompts the user for the number of students and tests
    - for each student:
        - prompts for the name of the student
        - prompts for the score on each of the tests
        - store the name and scores in a dictionary
    - display the final table of grades to the user

Notice: the keys in the dictionary should be the names of the student, 
and the values should be lists with the scores.

"""


# get the dimensions of the table
students = int(input('Enter the number of students: '))
tests = int(input('Enter the number of tests: '))

# initialize the table as dictionary
table = {}

# for each student...
for i in range(students):
    
    # ...get the name of the student
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
    
    
# print table using the indexing operator ([])...
print('\nTable with grades:\n') 
for name in table:
    print(name, table[name])
    
# ...or print table using the items function...
print('\nTable with grades:\n') 
for name, score in table.items():
    print(name, score)
    
# ... or print more fancy table
print('\nTable with grades:\n') 
for name, scores in table.items():
    print('|{:8}|'.format(name), end = ' ')
    for score in scores:
        print('{:4}|'.format(score), end = ' ')
    print()
    
    

        
  
    
