# -*- coding: utf-8 -*-
"""
@author: Isabel Hovdahl

"""

"""
Exercise 4

Modify this week’s class exercise so that the temperature conversion program 
instead converts temperatures from celsius to fahrenheit. 

The program should:
    - prompt the user for a temperature in celsius
    - display the converted temperature in fahrenheit

"""

print('***************** Conversion program 3 *****************')
print('This program converts from Celsius to Fahrenheit.')
print('********************************************************\n')

# convert user input to integer
celsius = int(input('Please enter temperature to convert: '))

# calculate temperature conversion
fahren =  (9 / 5 * celsius) + 32

print('\n{} degree(s) Celsius is {:.1f} degree(s) Fahrenheit.'.format(celsius, fahren))