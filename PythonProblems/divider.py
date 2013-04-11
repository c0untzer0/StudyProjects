#!/usr/local/bin/python3
#-*- coding: utf-8 -*-
#
#  divider.py
#  PythonProblems
#
#  Created by Johan Cabrera on 4/10/13.
#  Copyright (c) 2013 Johan Cabrera. All rights reserved.
#

"""Tries to catch several exceptions"""

while True:
    inp=input("Provide an integer: ")
    if not inp:
        break
    try:
        intinp=int(inp)
        result=10/intinp
        print(result)
    except ValueError:
        print("Your input must be an integer")
    except ZeroDivisionError:
        print("Your input must not be zero (0)")