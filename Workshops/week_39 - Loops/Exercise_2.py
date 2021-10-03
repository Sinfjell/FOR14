# -*- coding: utf-8 -*-
"""
@author: Isabel Hovdahl

"""

"""
Exercise 2

Write a program that computes the average exam scores of students. 

The program should:
    - use a while loop that in each iteration:
        - prompt the user for the number of exams.
        - use a for loop to promp the user for each of the exam scores.
        - compute and display the average score to the user.
        - ask whether the user want to enter the grades for another student. 

"""



# program greeting
print('*'*46)
print('*'*46)
print('*'*3 + ' '*40 + '*'*3)
print('*** Welcome to the average-grade computer! ***')
print('*'*3 + ' '*40 + '*'*3)
print('*'*46)
print('*'*46)

# initialize moreStudents to start the while loop
moreStudents = 'Y'
student_no = 1

# compute average exam grades until the user wants to stop
while moreStudents == 'Y':
    
    # obtain the number of exam scores
    numExams = int(input('\nPlease enter the number of exams of student number {}: '.format(student_no)))
   
    # initialize the total
    total = 0
   
    # compute the average grade for one student
    print('\n\nEnter the exam scores.')
    for i in range(1, numExams + 1):
        # prompt for exam grade and convert to integer
        score = int(input('Exam {}: '.format(i)))  
        # add grade to total
        total = total + score
      
    # compute the grade average for a student
    average = total / numExams
    print('\nThe average score of student number {} is {:.1f}.'.format(student_no, average))
   
    # increment the student counter
    student_no += 1
   
    # prompt as to whether the user wants to enter grades for another student.
    moreStudents = input('\nEnter exam scores for another student (Y/N)? ')
    moreStudents = moreStudents.upper()
   

   
   
   

