# -*- coding: utf-8 -*-
"""
@author: Isabel Hovdahl

"""



"""
Exercise 4

Modify the temperature-conversion program from this week’s class exercise so that
it also converts temperatures in Kelvin. There are now three temperatures to
convert form and to (Fahrenheit, Celsius and Kelvin), and we now have the
following formulas for conversion:
C = (F – 32) * 5 / 9
K = (F – 32) * 5 / 9 + 273.15
F =  (9 / 5) * C) + 32
K = C + 273.15
F = (9 / 5 * (K – 273.15)) + 32
C = K – 273.15

Write a program that prompts the user for a temperature, scale to convert from,
and scale to convert to. For simplicity, the program should ignore checking
that the user-supplied inputs are valid.

"""

print('This program converts temperatures between Fahrenheit/Celsius/Kelvin')

# get temperature and convert to float
temp = float(input('Enter temperature: '))

# get temperature scale to convert from
fromScale = input('Is this in (F)ahrenheit, (C)elsius or (K)elvin?: ').upper()

# get temperature scale to convert to
toScale = input('Convert to (F)ahrenheit, (C)elsius or (K)elvin?: ').upper()

# converting from Fahrenheit...
if fromScale == 'F':
    converting_from = 'Fahrenheit'
    # ...to Celsius
    if toScale == 'C':
        converting_to = 'Celsius'
        converted_temp = (temp - 32) * 5/9
    # ...to Kelvin
    elif toScale == 'K':
        converting_to = 'Kelvin'
        converted_temp = (temp - 32) * 5/9 + 273.15
    # ...to Fahrenheit
    else:
        converting_to = 'Fahrenheit'
        converted_temp = temp

# converting from Celsius...
elif fromScale == 'C':
    converting_from = 'Celsius'
    # ...to Fahrneheit
    if toScale == 'F':
        converting_to = 'Fahrenheit'
        converted_temp = (9/5 * temp) + 32
    # ...to Kelvin
    elif toScale == 'K':
        converting_to = 'Kelvin'
        converted_temp = temp + 273.15
    # ...to Celsius
    else:
        converting_to = 'Celsius'
        converted_temp = temp

# converting from Kelvin...
else:
    converting_from = 'Kelvin'
    # ...to Fahrenheit
    if toScale == 'F':
        converting_to = 'Fahrenheit'
        converted_temp = (9/5 * (temp - 273.15)) + 32
    # ...to Celsius
    elif toScale == 'C':
        converting_to = 'Celsius'
        converted_temp = temp - 273.15
    # ...to Kelvin
    else:
        converting_to = 'Kelvin'
        converted_temp = temp


print('{:.1f} degrees {} equals {:.1f} degrees {}'.
      format(temp, converting_from, converted_temp, converting_to))
