# -*- coding: utf-8 -*-
"""
@author: Isabel Hovdahl

"""

"""
Exercise 3c:
    
Write a program that prompts the user for a message to translate using the 
dictionary with the abbreviations and the translateAbbrev function.

Implement the program in a main function.

"""


def main():
    """
    Translates an abbreviated message to english words and print it

    Returns
    -------
    None.

    """
    
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
    
    # Prompt the user for the message
    message = input('Please enter a message to translate: ')
    
    # Get the abbreviations in the message
    messageParts = message.split()
    
    # Translate the message to english
    englishMessage = ''
    for part in messageParts:
        word = translateAbbrev(part, abbv_dict)
        englishMessage = englishMessage + word + ' '
    
    print(englishMessage)
    
    
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
    

if __name__ == '__main__':
    main()