#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 13:52:55 2021

@author: sinfjell
"""

checking = float(input("Amount in your checking account: "))
while checking < 0: 
    print("Amount cant be negative!")
    checking = float(input("Amount in your checking account: "))

savings = float(input("Amount in your savings account: "))
while savings < 0: 
    print("Amount cant be negative!")
    savings = float(input("Amount in your savings account: "))

transaction = input("What transaction do you want to perform? Type 1 for deposit, 2 for withdrawal and 3 for transfer")
account = input("Type 1 for checking and 2 for savings")

if account == "1": 
    deposit = float(input("Your deposit: "))
    if transaction = "1":
        while deposit > checking:
            print("Not sufficient funds, perform a new deposit")
            deposit = float(input("Your deposit: "))
            
    elif transaction = "2"
        while deposit > checking:
            print("Not sufficient funds, perform a new deposit")
            deposit = float(input("Your deposit: "))
            
