#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 13:14:38 2021

@author: sinfjell
"""

# Exercise P3.37
name = input("What is your name?")
hourly_wage = float(input("What is your hourly wage?"))
hours_worked = float(input("How many hours have you worked this week?"))
pay = hourly_wage*hours_worked

# Calculating overtime
if hours_worked > 40: 
    overtime_hours = hours_worked % 40
    pay = (40*hourly_wage)+(overtime_hours*(hourly_wage*1.5))

# Print out paycheck
print("Hello {}, you have earned {} this week!".format(name, pay))

