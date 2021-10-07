#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 14:26:59 2021

@author: sinfjell
"""


# Problem R1.7
print("39+3")
print(39+3)

#%%
"""
# Problem R1.8
"""
print("Hello", "World", "!")

#%%
"""
Problem R1.12
"""
IB = 10000
interest_rate = 0.005
monthly_withdraws = 500
x = 23

income = IB*(1+interest_rate) ** x
out = 500 * x
a = income-out
print(a)

print("Bank account is depleted after {} years".format(x))

#%%
"""
Problem R1.20
"""

# Input
tip = 0.15

# Convert input to floats.   
bill = float(input("Bill: "))
num_persons = float(input("Persons:"))

# Performing the calculations
tot_tip = bill*tip
tot_cost = bill + tot_tip
tot_cost_person = tot_cost / num_persons
tot_bill_person = tot_cost / num_persons
tot_tip_person = tot_tip / num_persons

# Results
print("The total cost of the meal was {}$ where {}$ was the bill and {}$ the tip" 
      .format(tot_cost, bill, tot_tip))
print("Each person had to pay {}".format(tot_cost_person))
print("For each person, the bill constituted {} and the tip {}"
      .format(tot_bill_person, tot_tip_person))

#%%
"""
Problem P1.10
"""
print(" /\_/\   -------")
print("( ’ ’ ) / Hello \ ")
print(" ( - ) < Sindre  |")
print(" | | |  \ Fjell!/")
print("(__|__)   ------")

#%%
"""
Problem P1.11
"""
# Input
best = str(input("Best movie:"))
second = str(input("Second best movie:"))
third = str(input("Third best movie:"))


# Print
print("Best movie is {}".format(best))
print("Second best movie is {}".format(second))
print("Third best movie is {}".format(third))

#%%
"""
Problem P1.16
"""
# Importing the panda library
import pandas as pd

# Define dictionary containting the translation
data = {"English": ["Ronaldo is the best football player ever"], 
        "Norwegian": ["Ronaldo er den beste fotballspilleren noensinne"]} 

# Convert the dictionary into DataFrame        
df = pd.DataFrame(data)

print(df)

#%%
"""
Problem P2.34
"""
price = float(input("price:"))

dollar = int(price)
cents = int(((price-dollar)*100)+0.5)

print("The price converts to {} dollars and {} cents."
      .format(dollar, cents))
 






