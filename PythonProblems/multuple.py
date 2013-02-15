#!/usr/local/bin/python3
#-*- coding: utf-8 -*-
#
#  multuple.py
#  PythonProblems
#
#  Created by Johan Cabrera on 2/15/13.
#  Copyright (c) 2013 Johan Cabrera. All rights reserved.
#

#import os
#import sys
#import re
#import random

tuplemonster=((1,1),(2,2),(12,13),(4,4),(99,98))

for mult in tuplemonster:
    result=mult[0]*mult[1]
    print("{0[0]:>3d} x {0[1]:>2d} = {1:>4d}".format(mult,result))
