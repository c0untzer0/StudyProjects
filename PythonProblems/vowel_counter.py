#!/usr/local/bin/python3
#-*- coding: utf-8 -*-
#
#  vowel_counter.py
#  PythonProblems
#
#  Created by Johan Cabrera on 2/15/13.
#  Copyright (c) 2013 Johan Cabrera. All rights reserved.
#

#import os
#import sys
#import re
#import random

s = input("Enter any string: ")
vcount=0
for c in s:
    if c in "aeiouAEIOU":
        vcount+=1
print("Vowel count: ", vcount)
