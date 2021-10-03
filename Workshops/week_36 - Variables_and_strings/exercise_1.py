# -*- coding: utf-8 -*-
"""
@author: Isabel Hovdahl

"""



"""
Exercise 1

Write a program that prompts the user for two integer values (int1 and int2) and 
prints the result of the first number divided by the second with two decimal places displayed.

"""

# convert inputs to integers
#num1 = int(input('Enter first integer: '))
#num2 = int(input('Enter second integer: '))

# store division in new variable
#res = num1 / num2

# display result with two decimals
#print('Result = {:.2f}'.format(res))

# alternatively, pass the calculation directly to the format specifier
#print('Result = {:.2f}'.format(num1 / num2))



"""
Modification 1: Ask the user for two floats and display the result with six decimal places.

"""

# convert inputs to floats
num1 = float(input('Enter first floating-point value: '))
num2 = float(input('Enter second floating-point value: '))

# display calculation with 6 decimals
print('Result = {:.6f}'.format(num1 / num2))



"""
Modification 2: Display the result using scientific notation with four decimal places.

"""

# convert inputs to floats
num1 = float(input('Enter first floating-point value: '))
num2 = float(input('Enter second floating-point value: '))

# display calculation using scientific notation with 4 decimals
print('Result = {:.4e}'.format(num1 / num2))


