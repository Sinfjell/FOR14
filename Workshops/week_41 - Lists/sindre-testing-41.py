#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 08:24:11 2021

@author: sinfjell
"""

# Import the os module
import os

# Change the current working directory
os.chdir('/Users/sinfjell/OneDrive - Norges Handelshøyskole/FOR14/Github/Workshops/week_41 - Lists')

txt_file = open("nurseryrhyme.txt")

for line in txt_file: 
    print(line)