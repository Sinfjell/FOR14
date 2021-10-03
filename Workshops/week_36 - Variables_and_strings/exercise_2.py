# -*- coding: utf-8 -*-
"""
@author: Isabel Hovdahl

"""



"""
Exercise 2

Write a program that prompts the user to enter two integer values and that displays 
the results when each of the arithmetic operators are applied. 
All floating-point results should be displayed with two decimal places of accuracy. 

"""

# convert inputs to integers
num1 = int(input('Enter first integer: '))
num2 = int(input('Enter second integer: '))

# display addition
print('{} + {} = {}\n'.format(num1, num2, num1 + num2))

# display subtraction
print('{} - {} = {}\n'.format(num1, num2, num1 - num2))

# display mutliplication
print('{} * {} = {}\n'.format(num1, num2, num1 * num2))

# display division
print('{} / {} = {:.2f}\n'.format(num1, num2, num1 / num2))

# display floor division
print('{} // {} = {}\n'.format(num1, num2, num1 // num2))

# display modulus
print('{} % {} = {}\n'.format(num1, num2, num1 % num2))

# display exponentiation
print('{}**{} = {}\n'.format(num1, num2, num1**num2))



