#!/usr/local/bin/python3
#-*- coding: utf-8 -*-
#
#  check_string.py
#  PythonProblems
#
#  Created by Johan Cabrera on 2/15/13.
#  Copyright (c) 2013 Johan Cabrera. All rights reserved.
#

#import os
#import sys
#import re
#import random

#!/usr/local/bin/python3
#
#check_string.py
#
strng = input("Please enter an upper-case string, ending with a period: \n")
if strng.isupper() and strng.endswith("."):
    print("THAT IS ACCEPTABLE")
elif not(strng.isupper() or strng.endswith(".")):
    print("You didn't follow any instructions!")
elif strng.isupper():
    print("Input does not end with a period")
else:
    print("Input is not all upper-case")
