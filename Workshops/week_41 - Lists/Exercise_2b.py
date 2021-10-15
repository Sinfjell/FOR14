# -*- coding: utf-8 -*-
"""
@author: Isabel Hovdahl

"""

"""
Exercise 2b:
    
Notice that some of the words stored in the list words in the previous 
exercise are capitalized and/or include special characters such as «.» and «?». 

Write a function called cleanWord that takes a string as an input and that 
cleans the string by making all letters lowercase and removing characters 
that are not letters. Remember proper function documentation.

Use the function to clean the words in words and store the cleaned words 
in a new list called cleaned_words.

"""


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



# copy-paste list from previous exercise
words = ['Mary', 'had', 'a', 'little', 'lamb,', 'whose', 'fleece', 'was', 
        'white', 'as', 'snow.', 'And', 'everywhere', 'that', 'Mary', 'went,', 
        'the', 'lamb', 'was', 'sure', 'to', 'go.', 'It', 'followed', 'her', 
        'to', 'school', 'one', 'day', 'which', 'was', 'against', 'the', 
        'rules.', 'It', 'made', 'the', 'children', 'laugh', 'and', 'play,', 
        'to', 'see', 'a', 'lamb', 'at', 'school.', 'And', 'so', 'the', 
        'teacher', 'turned', 'it', 'out,', 'but', 'still', 'it', 'lingered', 
        'near,', 'And', 'waited', 'patiently', 'about,', 'till', 'Mary', 
        'did', 'appear.', '"Why', 'does', 'the', 'lamb', 'love', 'Mary', 
        'so?"', 'the', 'eager', 'children', 'cry.', '"Why,', 'Mary', 'loves', 
        'the', 'lamb,', 'you', 'know."', 'the', 'teacher', 'did', 'reply.']


# initialize list for cleaned words
cleaned_words = []

# clean each word in original list
# and append to new list
for word in words:
    cleaned_words.append(cleanWord(word))
    
# alternatively, use list comprehension:
# cleaned_words = [cleanWord(word) for word in word_lst]

print(cleaned_words)
       

