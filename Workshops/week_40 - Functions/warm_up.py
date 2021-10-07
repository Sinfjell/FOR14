# -*- coding: utf-8 -*-
"""
@author: Isabel Hovdahl

"""

"""
Warm-up:
    
Create a function that counts the number of vowels in an English word.

The function should take one input, an English word, and should return the 
number of vowels in that word.

Remember proper function documentation!

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


# Notice that we can include an if-statement that will execute a 
# test case only if this is the "main" file.
# That means that the test case will not be executed if the script is
# imported into another program as a module.
if __name__ == '__main__': 
    
    word = 'apple'
    count = countVowels(word)
    print('\n"{}" contains {} vowel(s).'.format(word.capitalize(), count))    



