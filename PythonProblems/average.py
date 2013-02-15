#!/usr/local/bin/python3
#-*- coding: utf-8 -*-
#
#  average.py
#  PythonProblems
#
#  Created by Johan Cabrera on 2/15/13.
#  Copyright (c) 2013 Johan Cabrera. All rights reserved.
#

#import os
#import sys
#import re
#import random

def average(lst):
    """Averages a list, tuple, or set of numeric values"""
    return sum(lst)/len(lst)

tst_lst=[1,2,3,4]
print('Average this list: {0}'.format(tst_lst))
print(average(tst_lst))
t=(243,132,987,342,13)
print('Average this tuple: ',t)
print(average(t))
s={1,2,3,4,25}
print('Average this set: {0}'.format(s))
print(average(s))