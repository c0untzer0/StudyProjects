#!/usr/local/bin/python3
#-*- coding: utf-8 -*-
#
#  secret_code.py
#  PythonProblems
#
#  Created by Johan Cabrera on 2/15/13.
#  Copyright (c) 2013 Johan Cabrera. All rights reserved.
#

#import os
#import sys
#import re
#import random

inp_str=input('Enter message: ')
out_str=""
for letter in inp_str:
    out_str+=chr(ord(letter)+1)
print(out_str[::-1])
#
# A more efficient algorithm:
# outlst=[]
# out_str=""
# for letter in inp_str:
#     outlst.append(chr(ord(letter)+1))
# out_str="".join(outlst)
# print(out_str[::-1])