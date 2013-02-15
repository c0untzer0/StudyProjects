#!/usr/local/bin/python3
#-*- coding: utf-8 -*-
#
#  sentence_splitter.py
#  PythonProblems
#
#  Created by Johan Cabrera on 2/15/13.
#  Copyright (c) 2013 Johan Cabrera. All rights reserved.
#

#import os
#import sys
#import re
#import random


s = input("Enter your string: ")
words = s.strip().split()
for word in words:
    print(word)