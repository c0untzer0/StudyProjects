#!/usr/local/bin/python3
#-*- coding: utf-8 -*-
#
#  tests.py
#  PythonProblems
#
#  Created by Johan Cabrera on 3/7/13.
#  Copyright (c) 2013 Johan Cabrera. All rights reserved.
#

import os
import threading
import subprocess
import re
#import sys
#import re
#import random

def check_server(itempos):
    
    global servinfo
    server=servinfo[itempos]['name']
    print("Server: "+server)
    cmd='./pinger.sh '+server
    outpt = subprocess.check_output(cmd, shell=True)
    #print(outpt)
    if outpt == b'0\n' or outpt == b'':
        servinfo[itempos]['status']='Down'
    else :
        servinfo[itempos]['status']='Up'

def threaded_ping():
    threads = []
    print("Pinging servers...")
    for item in range(0,len(servinfo)) :
        thread = threading.Thread(target=check_server, args=(item,))
        thread.start()
        threads.append(thread)
    for thread in threads :
        thread.join()
    print("Done.")


def print_status():
    global servinfo
    print("{0:.<30s}{1:.<30s}".format("Server","Status"))
    for item in servinfo:
        #print(item)
        print("{0:<30s}{1:<30s}".format(item['name'],item['status']))


if __name__ == '__main__':

    servinfo=[]

    servlist=open('conf.txt','r').readlines()

    print("Servers to be monitored: ")
    for pos,serv in enumerate(servlist):
        print(serv.strip())
        servinfo_item={}
        servinfo_item['name']=serv.strip()
        servinfo.append(servinfo_item)
    

    #check_server(0)
    threaded_ping()
    print(servinfo)
    print_status()



