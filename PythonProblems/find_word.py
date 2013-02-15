#!/usr/local/bin/python3
#-*- coding: utf-8 -*-
#
#  find_word.py
#  PythonProblems
#
#  Created by Johan Cabrera on 2/15/13.
#  Copyright (c) 2013 Johan Cabrera. All rights reserved.
#

#import os
#import sys
#import re
#import random


uin = input("Please enter a sentence: ")
if "python" in uin.lower():
    print("You mentioned Python.")
elif "perl" in uin.lower():
    print("Aha, a Perl user!")
elif "ruby" in uin.lower():
    print("So you use Ruby, then?")
else:
    print("Didn't see any languages there.")
