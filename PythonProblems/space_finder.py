#!/usr/local/bin/python3
#-*- coding: utf-8 -*-
#
#  space_finder.py
#  PythonProblems
#
#  Created by Johan Cabrera on 2/15/13.
#  Copyright (c) 2013 Johan Cabrera. All rights reserved.
#

#import os
#import sys
#import re
#import random

s = input("Please enter a string: ")
pos = 0
for c in s:
    if c == " ":
        print("First space encountered at position ", pos)
        break
    pos += 1
else:
    print("No spaces on that string")
