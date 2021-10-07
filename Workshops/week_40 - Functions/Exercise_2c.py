# -*- coding: utf-8 -*-
"""
@author: Isabel Hovdahl

"""

"""
Exercise 2c:
    
Modify the password-generating program in the previous exercise so that the 
symbol and digit are instead inserted at random locations in the password 
except for the first location (the passwrod cannot start with a symbol or a digit).

Implement this change by adding another function called insertRandom 
to the program.

"""


from random import randint


def main():
    """
    Generate a random password of 10 characters consisting of lower-
    case letters, with a single digit and symbol inserted at random
    locations. 

    Returns
    -------
    None.

    """
    
    password = makePassword(10)
    print('Random password: {}'.format(password))
    
    
def makePassword(length):
    """
    Generates a random password consisting of lower-case letters 
    and with a digit and symbol at the end of the password. 

    Parameters
    ----------
    length : int
        Length of password.

    Returns
    -------
    password : str
        Random password.

    """
   
    # initialize and empty password
    password = ''
   
    # pick random letters and add to end of password
    # (notice that we pick two letter less than the length of the
    # password)
    for i in range(length - 2):
        password = password + randomCharacter('abcdefghijklmnopqrstuvwxyz')
        
    # insert a random digit at random location 
    digit = randomCharacter('0123456789')
    password = insertAtRandom(password, digit)
 
    # insert a random symbol at random location
    symbol = randomCharacter('+-*/?!@#$%&')
    password = insertAtRandom(password, symbol)
 
    return password


def randomCharacter(characters):
    """
    Returns a string containing one character randomly 
    chosen from a given string.

    Parameters
    ----------
    characters : str
        A sequence of characters.

    Returns
    -------
    rand_char : string
        A randomely drawn character from the sequence.

    """
    
    # draw a random location given the length of the string
    n = len(characters)
    r = randint(0, n - 1)
    
    # extract character at random location
    rand_char = characters[r]
    
    return rand_char


def insertAtRandom(string, to_insert):
    """
    Inserts one string into another at a random position, except for the first
    location in the string.

    Parameters
    ----------
    string : str
        String into which another string is inserted..
    to_insert : str
        String to be inserted..

    Returns
    -------
    str
        The concatenated string.

    """
    
    # draw random location to insert character
    n = len(string)
    r = randint(1, n)
    
    # extract first part of the new string
    part_one = string[:r]
    
    # extract the second part of the new string
    if r < n: 
        part_two = string[r:]
    else:
        part_two = ''
        
    # return the new string with the string to_insert inserted in the
    # original string
    return part_one + to_insert + part_two



if __name__ == '__main__':
    main()