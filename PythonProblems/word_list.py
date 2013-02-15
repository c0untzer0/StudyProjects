#!/usr/local/bin/python3
#-*- coding: utf-8 -*-
#
#  word_list.py
#  PythonProblems
#
#  Created by Johan Cabrera on 2/15/13.
#  Copyright (c) 2013 Johan Cabrera. All rights reserved.
#

#import os
#import sys
#import re
#import random

uplist=[]
lowerlist=[]
mainstr=input("Please specify a string: ")
wordlist=mainstr.strip().split()
for word in wordlist:
    if word.islower():
        lowerlist.append(word)
    else:
        uplist.append(word)

printlist=uplist+lowerlist
for printout in printlist:
    print(printout)
