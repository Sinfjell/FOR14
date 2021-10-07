#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 15:56:32 2021

@author: sunnivafjellestad
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
account = input("Type 1 for checking and 2 for savings ")


if account == '1' and transaction == '1':
    deposit_checking = float(input('Deposit: '))
    
    balance_checking = checking + deposit_checking
    print("You have {} in checkin and {} in savings".format(balance_checking, savings))
    

elif account == '1' and transaction == '2':
    withdrawal_checking = float(input('Withdrawal: '))
    
    while withdrawal_checking > checking:
        print("Not sufficient funds, perform a new withdrawal")
        withdrawal_checking = float(input("Withdrawal: "))
    
    balance_checking = checking - withdrawal_checking
    balance_savings = savings 
    print("You have {} in checkin and {} in savings".format(balance_checking, balance_savings))

elif account == '1' and transaction == '3':
    transfer_checking = float(input('Transfer: '))
    
    while transfer_checking > savings:
        print("Not sufficient funds, perform a new withdrawal")
        transfer.checking = float(input("Withdrawal: "))
        
    balance_checking = checking - transfer_checking
    balance_savings = savings + transfer_checking
    print("You have {} in checkin and {} in savings".format(balance_checking, balance_savings))
    
    
    
elif account == '2' and transaction == '1':
    deposit_savings = float(input('Deposit: '))
    
    balance_savings = savings + deposit_savings
    balance_checking = checking 
    print("You have {} in checkin and {} in savings".format(balance_checking, balance_savings))
    
elif account == '2' and transaction == '2':
    withdrawal_savings = float(input('Withdrawal: '))
    
    while withdrawal > savings:
        print("Not sufficient funds, perform a new withdrawal")
        withdrawal_savings = float(input("Withdrawal: "))
        
    balance_savings = savings - withdrawal_savings
    balance_checking = checking 
    print("You have {} in checkin and {} in savings".format(checking, balance_savings))
    

elif account == '2' and transaction == '3':
    
    transfer_savings = float(input('Transfer: '))
    
    while transfer_savings > savings:
        print("Not sufficient funds, perform a new withdrawal")
        transfer_savings = float(input("Withdrawal: "))
        
    balance_savings = savings - transfer_savings
    balance_checking = checking + transfer_savings
    print("You have {} in checkin and {} in savings".format(balance_checkin, balance_savings))