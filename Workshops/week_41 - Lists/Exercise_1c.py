# -*- coding: utf-8 -*-
"""
@author: Isabel Hovdahl

"""

"""
Exercise 1c:
    
Write a program that creates a table with student scores and that calculates 
and prints the average scores for each student and each test.

Implement the program using a main function. 

The main function should:
    - program should prompt the user for the number of students and tests.
    - create the table.
    - calculate the average student (row) and test (column) scores.
    - display the averages.

"""

# import the functions to calculate the student and test averages
from Exercise_1a import rowAvg, colAvg


def main():
    """
    Executes a program that creates a table with student test scores and that 
    displays the average scores for each student and for each test.

    Returns
    -------
    None.

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
        
    # calculate average score for each student
    student_scores = rowAvg(table)
    print('\nAverage score for each student:')
    for i, score in enumerate(student_scores):
        print('...Student {}: {:.1f}'.format(i + 1, score))
            
    # calculate average score on each test
    test_scores = colAvg(table)
    print('\nAverage score on each test:')
    for i, score in enumerate(test_scores):
        print('...Test  {}: {:.1f}'.format((i + 1), score))
  

   
if __name__ == '__main__':
    
    # table = [[85,91,89], 
    #         [78,81,86], 
    #         [62,75,77],
    #         [70,65,72]]

    main()