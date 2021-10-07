# -*- coding: utf-8 -*-
"""
@author: Isabel Hovdahl

"""

"""
Exercise 1a:
    
Use the vowel counting program in exercise 1a from last week’s workshop and 
convert the program into a program run only using functions.

The program should consist of three functions:
    - countVowels – return the number of vowels in a given word.
    - getWord – return the word prompted from an user.
    - main – calls all the functions and displays the result to the user.

All functions should be properly documented, and the program should make 
a function call to main in order to execute the program.

"""

def countVowels(word):
    """
    Counts the number of vowels in an English word.

    Parameters
    ----------
    word : str
        An English word.

    Returns
    -------
    count : int
        The number of vowels.

    """
    
    # initialize count
    count = 0
    
    # loop over letters in word
    for letter in word.lower(): # convert word to all lower-case
        # increment counter if letter is a vowel
        if letter in ('a', 'e', 'i', 'o', 'u'):
            count = count + 1
            
    return count


def getWord():
    """
    Prompts the user for a word.

    Returns
    -------
    word : str
        A word.

    """
   
    word = input('Please enter a word: ')
    
    return word



def main():
    """
    Main function to execute the vowel-counting program.

    Returns
    -------
    None.

    """
    
    # program greeting
    print('*'*58)
    print('Welcome to the vowel-counting program!\n')
    print('This program counts the number of vowels in English words.')
    print('*'*58)

    # get word
    word = getWord()
    
    # count vowels
    count = countVowels(word)
    
    # display result
    print('\n"{}" contains {} vowel(s).'.format(word.capitalize(), count))    
    
    
    
# call main function to execute program    
main()


