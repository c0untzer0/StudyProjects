#!/usr/local/bin/python3
#-*- coding: utf-8 -*-
#
#  sentence_splitter2.py
#  PythonProblems
#
#  Created by Johan Cabrera on 2/15/13.
#  Copyright (c) 2013 Johan Cabrera. All rights reserved.
#

#import os
#import sys
#import re
#import random


s = input("Please enter a sentence: ")
while True:
    while s.startswith(" ") or s.startswith('\t'):
        s = s[1:]
    pos = 0
    for c in s:
        if c == " " or c == '\t':
            print(s[:pos])
            s = s[pos+1:]
            break
        pos += 1
    else:
        print(s)
    break