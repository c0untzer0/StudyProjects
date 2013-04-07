#!/usr/local/bin/python3
#-*- coding: utf-8 -*-
#
#  keyword_args.py
#  PythonProblems
#
#  Created by Johan Cabrera on 4/7/13.
#  Copyright (c) 2013 Johan Cabrera. All rights reserved.
#

#import os
#import sys
#import re
#import random

"""Demonsrates capture of keyword arguments"""

def keywords(**kwargs):
    "Prints the keys and arguments passed through"
    for key in kwargs:
        print("{0}: {1} ".format(key,kwargs[key]))

def keywords_as_dict(**kwargs):
    "Returns the keyword arguments as a dict"
    return kwargs

if __name__ == "__main__":
    keywords(guido="Founder of Python", python="Used by NASA and Google")
    print(keywords_as_dict(guido="Founder of Python", python="Used by NASA and Google"))
