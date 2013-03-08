#!/usr/local/bin/python3
#-*- coding: utf-8 -*-
#
#  interestcalc.py
#  PythonProblems
#
#  Created by Johan Cabrera on 2/15/13.
#  Copyright (c) 2013 Johan Cabrera. All rights reserved.
#

#import os
#import sys
#import re
import math
#import random

#def newfunction(*arg):
##
## Insert function definitions in here.
##

if __name__ == '__main__':
    print('Loan calculator.\n')
    princ=int(round(float(input("Amount borrowed: "))*100))
    rate=int(input("Interest rate: "))
    term=int(input("Term (years): "))
    intpaid=princ*term*rate/100
    print('{0:<30s}${1:>10.2f}'.format("Amount borrowed:",princ/100))
    print('{0:<30s}${1:>10.2f}\n'.format("Total interest paid:",(intpaid/100)))
    rembal=princ+intpaid
    mamount=int(math.ceil(rembal/(12*term)))
    counter=0
    
    print('{0:^10s}{1:^10s}{2:^12s}'.format(" "*6,"Amount","Remaining"))
    print('{0:^10s}{1:^10s}{2:^12s}'.format("Pymnt#","Paid","Balance"))
    print('{0:^10s}{1:^10s}{2:^12s}'.format("-"*5,"-"*7,"-"*9))
    print('{0:>5}      ${1:^6.2f}     ${2:>6.2f}'.format(counter,0,rembal/100))
    while mamount<rembal:
        rembal-=mamount
        counter+=1
        print('{0:>5}      ${1:^6.2f}     ${2:>6.2f}'.format(counter,mamount/100,rembal/100))
    counter+=1
    print('{0:>5}      ${1:^6.2f}     ${2:>6.2f}'.format(counter,rembal/100,0))
