#!/usr/local/bin/python3
#-*- coding: utf-8 -*-
#
#  doggies.py
#  PythonProblems
#
#  Created by Johan Cabrera on 4/10/13.
#  Copyright (c) 2013 Johan Cabrera. All rights reserved.
#

"""Doggies.py homework"""

dogs=list()

class Dog():
    def __init__(self,name,breed):
        global dogs
        self.name=name
        self.breed=breed
        dogs.append(self)
    
    def __str__(self):
        return "{0}:{1}".format(self.name,self.breed)

if __name__ == "__main__":
    while True:
        newname=input("Name: ")
        if not newname:
            break
        else:
            newbreed=input("Breed: ")
            newdog=Dog(newname,newbreed)
            print("DOGS")
            for pos, dog in enumerate(dogs):
                print("{0}. {1}".format(pos,dog))
            print("*" * 40)

