#!/usr/local/bin/python3
#-*- coding: utf-8 -*-
#
#  funcalls.py
#  PythonProblems
#
#  Created by Johan Cabrera on 2/15/13.
#  Copyright (c) 2013 Johan Cabrera. All rights reserved.
#

#import os
#import sys
#import re
#import random


import funcs

while True:
    inval=input('Enter a number: ')
    if not inval:
        break
    number=float(inval)
    print(funcs.commareal("{0:.2f}".format(number)))
