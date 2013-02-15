#!/usr/local/bin/python3
#-*- coding: utf-8 -*-
#
#  caching.py
#  PythonProblems
#
#  Created by Johan Cabrera on 2/15/13.
#  Copyright (c) 2013 Johan Cabrera. All rights reserved.
#

#import os
#import sys
#import re
#import random

global_cache={}

def kid(a,b):
    """Multiplication the hard way"""
    if (a,b) in global_cache:
        return global_cache[(a,b)]
    c=0
    for i in range(b):
        c+=a
    global_cache[(a,b)] = c
    return c

while True:
    a=int(input('enter a number: '))
    b=int(input('enter another number: '))
    print(kid(a,b))
    print(global_cache)
    print('-'*40)
