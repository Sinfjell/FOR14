#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 13:27:27 2021

@author: sinfjell
"""

target_price = float(input("What is the target price?"))
current_price = float(input("What is the current price"))

while current_price < target_price: 
    print("Stock price is not yet at target price. Dont purchase yet")
    current_price = float(input("What is the current price"))
    
print("Stock price is at target price, BUY!")