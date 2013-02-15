#!/usr/local/bin/python3
#-*- coding: utf-8 -*-
#
#  pair_frequency.py
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

words={}
textwords=text.lower().split()
firstword=textwords[0]
for nextword in textwords[1:]:
    if firstword not in words:
        words[firstword]={}
    words[firstword][nextword]=words[firstword].get(nextword,0)+1
    firstword=nextword

for word in sorted(words.keys()):
    d=words[word]
    for word2 in sorted(d.keys()):
        print(word, ":", word2, d[word2])

