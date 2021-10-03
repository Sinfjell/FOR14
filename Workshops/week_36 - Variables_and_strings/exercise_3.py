# -*- coding: utf-8 -*-
"""
@author: s14754

"""

"""
Exercise 3

Write a program that calculates the restaurant tab for a person with a 
gift certificate. 

The program should:
   - prompt the user for the amount spent on appetizer, entrée, dessert and 
     drinks, and for the amount on the gift certificate. 
   - display both the final tab to the customer, as well as the amount paid 
     in sales tax (assume a sales tax of 25 %).

"""

# program greeting
print('*'*50)
print('This program will calculate a restaurant tab for a \nperson with a gift certificate.\n')
print('*'*50)

# initialize tax rate
SALES_TAX = 0.25

# get amount of gift certificate
certificate = float(input('Enter amount on the gift certificate: '))

# get cost of ordered items
print('\nEnter the cost of ordered items:')
appetizer = float(input('Appetizier: '))
entree = float(input('Entree: '))
drinks = float(input('Drinks: '))
dessert = float(input('Dessert: '))

# calculate tab and sales tax
tab = appetizer + entree + drinks + dessert - certificate
tax = tab - (tab / (1 + SALES_TAX))

# display tab
print('Tab: {:.2f}'.format(tab))
print('(Sales tax: {:.2f})'.format(tax))
print('Negative tab indicates unused amount of gift certificate.')