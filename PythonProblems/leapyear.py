#!/usr/local/bin/python3
#-*- coding: utf-8 -*-
#
#  leapyear.py
#  PythonProblems
#
#  Created by Johan Cabrera on 2/15/13.
#  Copyright (c) 2013 Johan Cabrera. All rights reserved.
#

#import os
#import sys
#import re
#import random

def findifleap(year):
    if (year%400==0) or (year%4==0 and not year%100==0):
        return "%s Is a leap year." % (year)
    else:
        return "%s Is not a leap year." % (year)


if __name__ == '__main__':
    while True:
        askyear=input("What year?: ")
        if askyear:
            print(findifleap(int(askyear)),"\n")
        else:
            break


