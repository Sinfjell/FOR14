#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 14:05:02 2021

@author: sinfjell
"""

# Exercise 1 
low_bound = int(input("lower bound: "))
upper_bound = int(input("higher bound "))
import random
if 
    low_bound.isdigi
print(random.randint(low_bound,upper_bound))


#%% 
# Exercise 2
# Exercise 1 
lower = input("lower bound: ")
upper = input("higher bound ")
import random

if lower.isdigit() and upper.isdigit():
    lower = int(lower)
    upper = int(upper)
    
    if 
        upper > lower:
        print(random.randint(lower,upper))
        
    else: 
        print("Your lower bound is higher than your upper bound")
    
else: 
    print("Invalid input")