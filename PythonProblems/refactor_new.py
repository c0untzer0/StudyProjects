#!/usr/local/bin/python3
#-*- coding: utf-8 -*-
#
#  refactor_new.py
#  PythonProblems
#
#  Created by Johan Cabrera on 4/11/13.
#  Copyright (c) 2013 Johan Cabrera. All rights reserved.
#

#!/usr/local/bin/python3
"""Adding functionality, much easier with refactored code!"""

def list_multiply(*lists):
    """ Sums two lists of integers and multiplies them together
        
        >>> list_multiply([3,4],[3,4])
        49
        >>> list_multiply([1,2,3,4],[10,20])
        300
        >>> list_multiply([4,3,2,1],[50,50],[5,5,5])
        15000
        """
    
    total = 1
    for l in lists:
        total *= sum(l)
    return total

def _test():
    import doctest, refactor
    return doctest.testmod(refactor)

if __name__ == "__main__":
    _test()
