# -*- coding: utf-8 -*-
"""
@author: Isabel Hovdahl

"""

"""
Exercise 2c:
    
Notice that «Mary has a little lamb» contains several duplicate words, 
e.g. «Mary».

Use the cleaned list of words from the previous exercise and count the 
number of unique words in the nursery rhyme.

"""

# copy-paste list with cleaned words from previous exercise
cleaned_words = ['mary', 'had', 'a', 'little', 'lamb', 'whose', 'fleece', 
                 'was', 'white', 'as', 'snow', 'and', 'everywhere', 'that', 
                 'mary', 'went', 'the', 'lamb', 'was', 'sure', 'to', 'go', 
                 'it', 'followed', 'her', 'to', 'school', 'one', 'day', 
                 'which', 'was', 'against', 'the', 'rules', 'it', 'made', 
                 'the', 'children', 'laugh', 'and', 'play', 'to', 'see', 'a', 
                 'lamb', 'at', 'school', 'and', 'so', 'the', 'teacher', 
                 'turned', 'it', 'out', 'but', 'still', 'it', 'lingered', 
                 'near', 'and', 'waited', 'patiently', 'about', 'till', 'mary', 
                 'did', 'appear', 'why', 'does', 'the', 'lamb', 'love', 'mary', 
                 'so', 'the', 'eager', 'children', 'cry', 'why', 'mary', 
                 'loves', 'the', 'lamb', 'you', 'know', 'the', 'teacher', 
                 'did', 'reply']

# initialize list with unique words
unique_words = []

# for each word...
for word in cleaned_words:
    
    # ...if the word is not already in the list...
    if word not in unique_words:
        
        # ...add the word to the list
        unique_words.append(word)
        
       
print('"Mary had a little lamb" contains {} words.'.format(len(cleaned_words)))
print('But only {} unique words.'.format(len(unique_words)))