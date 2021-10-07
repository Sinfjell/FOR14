# -*- coding: utf-8 -*-
"""
@author: Isabel Hovdahl

"""

"""
Exercise 2a:

Create a function called randomCharacter that takes a string and that returns 
a random character from that string.

For instance, if the function is given the string ‘abcdefghijklmnopqrstuvwxyz’, 
the function should return a random letter from the alphabet. 

Remember proper function documentation.

"""

from random import randint


def randomCharacter(characters):
    """
    Returns a string containing one character randomly chosen from a given string.

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



if __name__ == '__main__':
    
    letter = randomCharacter('abcdefghijklmnopqrstuvwxyz')
    print('Random letter: {}'.format(letter))