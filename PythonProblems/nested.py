#!/usr/local/bin/python3
#-*- coding: utf-8 -*-
#
#  nested.py
#  PythonProblems
#
#  Created by Johan Cabrera on 4/10/13.
#  Copyright (c) 2013 Johan Cabrera. All rights reserved.
#

"""Nested exception handling"""

def divide(a, b):
    """Return result of dividing a by b"""
    print("=" * 20)
    print("a: ", a, "/ b: ", b)
    try:
        result = a/b
        print("Sometimes executed")
        return result
    except TypeError:
        print("Invalid types for division")
    except ZeroDivisionError:
        print("Divide by zero error")

if __name__ == "__main__":
    print(divide(1, "string"))
    print(divide(2, 0))
    print(divide(123, 4))
