# -*- coding: utf-8 -*-
"""
@author: Isabel Hovdahl

"""

"""
Exercise 1b:
    
Use the vowel counting program in exercise 1c from last week’s workshop and 
convert the program into a program run only by functions. 

The program should consist of two functions:
    - countVowels – return the number of vowels in a given word (you can 
                    import existing function from the warm-up exercise)
    - main – prompt the user for words and display the number of vowels 
             until the user decides to quit

All functions should be properly documented, and the program should make 
a function call to the main function in order to execute the program.

"""

from warm_up import countVowels


def main():
    """
    Main function for the vowel-counting program. The function continues to
    propmpt the user for words and display the number of vowels in the words,
    until the user decides to quit.

    Returns
    -------
    None.

    """
    
    # program greeting
    print('*'*58)
    print('Welcome to the vowel-counting program!\n')
    print('This program counts the number of vowels in English words.')
    print('*'*58)

    # get first word
    word = input('Enter a word (or press "q" to quit): ').lower()

    # continue until user decides to quit
    while word != 'q':
    
        # count vowels in word
        count = countVowels(word)
    
        # display word and count
        print('\n"{}" contains {} vowel(s).'.format(word.capitalize(), count))
    
        # get next word
        word = input('Enter next word (or press "q" to quit): ').lower()
    
    print('\nThank you for using the vowel-counting program!')
    
    
# execute program   
main()

# or alternatively, include the function call inside an if statement
#if __name__ == '__main__':
#    main()