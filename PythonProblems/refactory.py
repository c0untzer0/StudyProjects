#!/usr/local/bin/python3
#-*- coding: utf-8 -*-
#
#  refactory.py
#  PythonProblems
#
#  Created by Johan Cabrera on 4/11/13.
#  Copyright (c) 2013 Johan Cabrera. All rights reserved.
#


#List of words considered "small"
small_words = ("Into", "The", "A", "Of", "At", "In", "For", "On")

def book_title(title):
    """ Takes a string and returns a title-case string.
        All words EXCEPT for small words are made title case
        unless the string starts with a preposition, in which
        case the word is correctly capitalized.
        
        >>> book_title('DIVE Into python')
        'Dive into Python'
        
        >>> book_title('the great gatsby')
        'The Great Gatsby'
        
        >>> book_title('the WORKS OF AleXANDer dumas')
        'The Works of Alexander Dumas'
        
        """
    lst_of_words = title.title().split()	#Set title for the whole string and split it into a list, we will lower the case of small words later.
    for pos, word in enumerate(lst_of_words[1:]):	#Go through the list after initial word and lower the case of selected small words.
        if word in small_words:
            lst_of_words[pos+1]=word.lower()
    return " ".join(lst_of_words)        		#Return the processed list converted back into a string.

#No need to include a flow for '', the existing flow will handle it.


def _test():
    """Make sure it all tests alright"""
    import doctest, refactory
    return doctest.testmod(refactory)

if __name__ == "__main__":
    _test()
