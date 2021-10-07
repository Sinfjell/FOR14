# -*- coding: utf-8 -*-
"""
@author: Isabel Hovdahl

"""

"""
Exercise 2b:
    
Write a program that generates a random password of a specified length. 
The password should consist of random lower-case letters, and it should 
end with a random digit (0-9) and a random symbol (+-*/?!@#$%&).

The program should be run only by functions. Create a function called 
makePassword that generates a random password of a given length, and generate 
a random password of length 8 using a main function.

Remember proper function documentation.

"""


from Exercise_2a import randomCharacter


# (notice that we can define the main function before
# we have defined the makePassword function)
def main():
    """
    Generate a random password of 8 characters consisting of lower-
    case letters, with a single digit and symbol at the end. 

    Returns
    -------
    None.

    """
    
    password = makePassword(8)
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
        
    # pick random digit and insert it at end of password
    digit = randomCharacter('0123456789')
    password = password + digit
 
    # pick random symbol and insert it at end of password
    symbol = randomCharacter('+-*/?!@#$%&')
    password = password +  symbol
 
    return password


main()

