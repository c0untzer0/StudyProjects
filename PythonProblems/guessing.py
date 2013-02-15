#!/usr/local/bin/python3
#
#  guessing.py
#  PythonProblems
#
#  Created by Johan Cabrera on 2/15/13.
#  Copyright (c) 2013 Johan Cabrera. All rights reserved.
#

#import os
#import sys

import random

counter=1
sol=random.randint(1,101)
print("Time to play a guessing game.")
message="Enter a number between 1 and 100: "
while True:
    guess=int(input(message))
    if guess>sol:
        message="Too high. Try again: "
        counter+=1
        continue
    elif guess<sol:
        message="Too low. Try again: "
        counter+=1
        continue
    else:
        print("Congratulations! You answered correctly! The number was:",sol)
        print("\nNumber of tries was:",counter)
        break



