#!/usr/local/bin/python3
#-*- coding: utf-8 -*-
#
#  validate_input.py
#  PythonProblems
#
#  Created by Johan Cabrera on 2/15/13.
#  Copyright (c) 2013 Johan Cabrera. All rights reserved.
#

#import os
#import sys
#import re
#import random

valid_inputs=['yes','no','maybe']
input_query_string='Type %s: ' % ' or '.join(valid_inputs)
while True:
    s = input(input_query_string)
    if s in valid_inputs:
        break
    print("Wrong! Try again.")
print(s)
