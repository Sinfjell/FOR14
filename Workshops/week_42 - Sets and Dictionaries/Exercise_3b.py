# -*- coding: utf-8 -*-
"""
@author: Isabel Hovdahl
"""

"""
Exercise 3b:
    
Write a function called translateAbbrev that translates an abbreviated word. 

The function should take two inputs: a string and a dictionary with 
abbreviations, and it should return the translated string. 

Notice: the function should remove potential punctuation marks (.;,:!?)
from the string before translating it.

"""


def translateAbbrev(abbv, dictAbbv):
    """
    Translates a single abbreviation using the translation map. If the 
    abbreviation ends with a punctuation mark, it remains part of the 
    translation. 

    Parameters
    ----------
    abbv : String
        a string that contains the abbreviation to be translated.
    dictAbbv : Dictionary
        a dictionary containing the common translations.

    Returns
    -------
    String
        the word or phrase corresponding to the abbreviation. If the
    abbreviation cannot be translated, it is returned unchanged.

    """
    
    # extract last character
    lastChar = abbv[len(abbv) - 1]
    
    # strip last character if punctuation mark
    if lastChar in '.;,:!?':
        abbv = abbv.rstrip(lastChar) # notice: "rstrip" strips only from the end of the string as opposed to "strip"
    else:
        lastChar = ''
    
    # translate abbreviation if in dictionary
    if abbv in dictAbbv:
        word = dictAbbv[abbv]
    else:
        word = abbv
    
    return word + lastChar



### test case

# initialize dictionary
abbv_dict = {}

# open file
abbv_file = open('textabbv.txt')

# for line in file
for abbv in abbv_file:
    
    # split line on colon
    parts = abbv.split(':')
    
    # store the parts in dictionary 
    # notice: strip() removes the newline character at the end
    abbv_dict[parts[0]] = parts[1].strip()
    
# close file
abbv_file.close()

print(translateAbbrev("fyi!", abbv_dict))