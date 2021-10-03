# -*- coding: utf-8 -*-
"""
@author: Isabel Hovdahl

"""



"""
Exercise 3

The prisoner’s dilemma is a common example used in game theory. 
One example of the game is found in the table below (see slide).

Write a program that implements the game. The program should:
    - prompt the user for two inputs – prisoner A’s choice and prisoner B’s choice (confess or stay silent).
    - print the outcome of the game, i.e. how much time must each of the prisoners serve.

"""

print('**********************************')
print("Welcome to the Prisoner's Dilemma.")
print('**********************************')

choiceA = input('Prisoner A, you are up.\nPress 1 for "confess", press 2 for "stay silent": ')
choiceB = input('Prisoner B, you are up.\nPress 1 for "confess", press 2 for "stay silent": ')

if choiceA == '1' and choiceB == '1':
    print('\nYou both get 2 years.')
    
elif choiceA == '1' and choiceB == '2':
    print('\nPrisoner A gets 3 years, prisoner B goes free.')
    
elif choiceA == '2' and choiceB == '1':
    print('\nPrisoner A goes free, prisoner B gets 3 years.')

elif choiceA == '2' and choiceB == '2':
    print('\nYou both get 1 year.')
    
else:
    print('INVALID INPUT')