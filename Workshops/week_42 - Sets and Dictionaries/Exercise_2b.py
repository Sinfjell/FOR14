# -*- coding: utf-8 -*-
"""
@author: Isabel Hovdahl

"""

"""
Exercise 2b:
    
Make two modifications the solution to the previous exercise:

1. Use the cleanWord function that we created in the last workshop 
  (see exercise 2b) to clean each word before it is added to the set.

2. Place the program inside a main function.

"""


def main():
    """
    This program counts the number of unique words in a text document.

    Returns
    -------
    None.

    """
    
    # initialize set to store unique words
    unique_words = set()

    # get filename
    file = input('Enter filename (or press enter to use default file): ')
    if file == '':
        	file = 'nurseryrhyme.txt'

    # open file
    txt_file = open(file)
    
    # for each line in the text file...
    for line in txt_file:
    
        # ...split the line on space and store the words in a list
        words_in_line = line.split()
        
        # for each word in line...
        for word in words_in_line:
            
                # ...clean word
                clean_word = cleanWord(word)
                
                # ...and if cleaned word is not empty
                if clean_word != '':
            
                    # ...add the word to the set
                    unique_words.add(clean_word)
                    
    # close file
    txt_file.close()
            
    print('\n"{}" contains {} unique words.'.format(file, len(unique_words)))



def cleanWord(word):
    """
    Cleans a string by making letters lowercase and removing characters
    that are not letters

    Parameters
    ----------
    word : str
        The string to be cleaned.

    Returns
    -------
    cleaned : str
        The cleaned string.

    """
    
    # initialize the cleaned string
    cleaned = ''
    
    # for every character in string...
    for char in word:
        
        # ...if that character is a letter...
        if char.isalpha():
            
            #...convert the letter to lowercase and add to the string
            cleaned = cleaned + char.lower()
    
    return cleaned



if __name__ == '__main__':
    main()

