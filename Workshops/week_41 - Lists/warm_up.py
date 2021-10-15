# -*- coding: utf-8 -*-
"""
@author: Isabel Hovdahl

"""

"""
Warm-up:
    
Consider the following nested list, where each sublist contains the test 
scores for a single student on each of the three tests:

table = [[85, 91, 89],  # test scores for student 1
         [78, 81, 86],  # test scores for student 2
         [62, 75, 77],  # test scores for student 3
         [70, 65, 72]]  # test scores for student 4
    
1. Write a program that calculates the average score for each student and 
stores the averages in a list called student_scores.

2. Write a program that calculates the average on each test and that stores 
the averages in a list called test_scores.

"""


# student scores
table = [[85,91,89], 
         [78,81,86], 
         [62,75,77],
         [70,65,72]]

# dimensions of the table
students = len(table) # rows
tests = len(table[0]) # columns


################################
### 1. Average student score ###
################################

# initialize list for student scores
student_scores = []

# for each student...
for row in table:
    
    # ...sum the score and divide by total number of tests
    avg = sum(row) / tests

    # ...append average score to list
    student_scores.append(avg)

# alternative solution using list comprehension:
# student_scores = [sum(row) / tests for row in table]  
  
print('\nAverage score for each student:')
for i, score in enumerate(student_scores):
    print('...Student {}: {:.1f}'.format(i + 1, score))
    

#############################
### 2. Average test score ###
#############################

# initialize list for test scores
test_scores = []
    
# for each test (column)...
for col in range(tests):
    
    # ...initialize the sum
    tot = 0
    
    # ...loop over each student and add the score to the sum
    for row in range(students):
        
        tot = tot + table[row][col]

    # calculate and store the average test score
    test_scores.append(tot / students)
    
print('\nAverage score on each test:')
for i, score in enumerate(test_scores):
    print('...Test  {}: {:.1f}'.format((i + 1), score))