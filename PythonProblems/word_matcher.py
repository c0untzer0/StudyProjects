#!/usr/local/bin/python3
#-*- coding: utf-8 -*-
#
#  word_matcher.py
#  PythonProblems
#
#  Created by Johan Cabrera on 2/15/13.
#  Copyright (c) 2013 Johan Cabrera. All rights reserved.
#

#import os
#import sys
#import re
#import random

text1=input("Please input a sentence: ")
text2=input("Please input another sentence: ")

for punct in ".,;?!":
    text1=text1.replace(punct,"")
    text2=text2.replace(punct,"")

words1=set(text1.lower().split())
words2=set(text2.lower().split())

print("The words in common are: ", sorted(words1&words2))
print("Exclusive to sentence 1 : ", sorted(words1-words2))
print("Exclusive to sentence 2 : ", sorted(words2-words1))

