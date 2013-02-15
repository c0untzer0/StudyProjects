#!/usr/local/bin/python3
#-*- coding: utf-8 -*-
#
#  personlist.py
#  PythonProblems
#
#  Created by Johan Cabrera on 2/15/13.
#  Copyright (c) 2013 Johan Cabrera. All rights reserved.
#

#import os
#import sys
#import re
#import random

data=[
      ("Steve", 59, 202),
      ("Dorothy", 49, 156),
      ("Simon", 39, 155),
      ("David", 61, 135)]
for name, age, weight in data:
    print("{0:.<30s} {1:4d} {2:4d}".format(name,age,weight))

