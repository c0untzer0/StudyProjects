#!/usr/local/bin/python3
#-*- coding: utf-8 -*-
#
#  word_counter.py
#  PythonProblems
#
#  Created by Johan Cabrera on 2/15/13.
#  Copyright (c) 2013 Johan Cabrera. All rights reserved.
#

#import os
#import sys
#import re
#import random


text="""\
    Baa, baa, black sheep,
    Have you any wool?
    Yes sir, yes sir,
    Three bags full;
    One for the master,
    And one for the dame,
    And one for the little boy
    Who lives down the lane."""

for punc in ",?.:;":
    text=text.replace(punc,"")
print(text)
words=set(text.lower().split())
print("There are ", len(words), " distinct words in the text.")

print(list(words)[::-2])

