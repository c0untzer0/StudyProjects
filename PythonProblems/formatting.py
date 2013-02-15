#!/usr/local/bin/python3
#-*- coding: utf-8 -*-
#
#  formatting.py
#  PythonProblems
#
#  Created by Johan Cabrera on 2/15/13.
#  Copyright (c) 2013 Johan Cabrera. All rights reserved.
#

#import os
#import sys
#import re
#import random

i = 42
r = 31.97
c = 2.2 + 3.3j
s = "String"
lst = ["zero", "one", "two", "three", "four", "five"]
dct = {"Jim":"Dandy", "Stella":"du Bois", 1:"integer"}
while True:
    fmt=input("Format string: ")
    if not fmt:
        break
    fms="{"+fmt+"}"
    print("Format:", fms, "output:", fms.format(i,r,c,s,e=lst,f=dct))
