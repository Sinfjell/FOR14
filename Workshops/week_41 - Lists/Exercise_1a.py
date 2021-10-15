# -*- coding: utf-8 -*-
"""
@author: Isabel Hovdahl

"""

"""
Exercise 1a:
    
Convert the program written in the warm-up exercise into functions.

Write a program consisting of two functions:
    - avgRow – takes a table in the form of a nested list and returns the 
      average for each row (sublist) in the table.
    - avgCol – takes a table in the form of a nested list and returns the 
      average for each column in the table.

The program should use the functions to print the average grades for each 
student and on each test.

Remember proper function documentation.

"""


def rowAvg(table):
    """
    Calculates the average for each row in a table of numbers.

    Parameters
    ----------
    table : list
        A nested list where each sublist is a row in the table.

    Returns
    -------
    row_avg : list
        A list with the averages for each row (sublist) in table.

    """
    
    # get number of cols
    cols = len(table[0])
    
    # initialize list for row averages
    row_avg = []
    
    # for each row...
    for row in table:
        
        # ...sum the row and divide by number of columns
        avg = sum(row) / cols
    
        # ...append average score to list
        row_avg.append(avg)
        
    return row_avg


def colAvg(table):
    """
    Calculates the average for each column in a table of numbers.

    Parameters
    ----------
    table : list
        A nested list where each sublist is a row in the table.

    Returns
    -------
    col_avg : list
        A list with the averages for each column in the table.

    """
    
    # get the dimensions of the table
    rows = len(table)
    cols = len(table[0])
 
    # initialize list for column averages
    col_avg = []
    
    # for each columns...
    for col in range(cols):
        
        # ...initialize the sum
        tot = 0
        
        # ...loop over each row and add the value to the sum
        for row in range(rows):
            
            tot = tot + table[row][col]
    
        # calculate and store the average column value
        col_avg.append(tot / rows)
        
    return col_avg 


if __name__ == '__main__':
        
    # define table with grades
    table = [[85,91,89], 
             [78,81,86], 
             [62,75,77],
             [70,65,72]]
    
    # calculate and print average student score
    student_scores = rowAvg(table)
    print('\nAverage score for each student:')
    for i, score in enumerate(student_scores):
        print('...Student {}: {:.1f}'.format(i + 1, score))
            
    # calculate and print average test score
    test_scores = colAvg(table)
    print('\nAverage score on each test:')
    for i, score in enumerate(test_scores):
        print('...Test  {}: {:.1f}'.format((i + 1), score))