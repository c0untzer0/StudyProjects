#!/usr/local/bin/python3
#-*- coding: utf-8 -*-
#
#  ptr_report_liveview.py
#  PythonProblems
#
#  Created by Johan Cabrera on 2/15/13.
#  Copyright (c) 2013 Johan Cabrera. All rights reserved.
#

#import os
#import sys
#import re
#import random

#INFORMATION:
#  Following Python Modules need to be Installed beforehand:
#           pyXML
#           ZSI
#----------------------------------------------------------------------------------------------------------------
#<<<<< Libraries >>>>>
from ZSI.client import Binding                        #Imports Binding from ZSI.Client Lib
from ZSI.auth import AUTH                             #Imports AUTH from ZSI.auth
from xml.etree import ElementTree                     #Imports ElementTree from xml.etree Lib
import re                                             #Imports Regex Lib
import _mysql
import time
import math
from time import time as time2
import sys


b = Binding(url='http://amadeus.aproach.net/aproach/services/AproachWebServices?WSDL') #Creates Object
b.SetAuth(AUTH.httpbasic,"foo","bar") #Sets WinAproach UserId and Password
db=_mysql.connect(host="test",port=3307,user="testmonitor",passwd="",db="notifier")

def getTitle(recordId):
    print "Checking "+recordId
    #Defines getTilte Function using Record Nr as Argument
    status=''
    phase=''
    assignee=''
    ownerg=''
    owneru=''
    master=''
    datetime_entered=''
    datetime_last=''
    date_last=''
    time_last=''
    date_entered=''
    time_entered=''
    lastupdate=''
    title=''
    ismaster='N'
    Record = b.retrieve(str(recordId))
    #try:                                               #Tests next Instruction
    #   Record = b.retrieve(str(recordId))              #Retrieves the Record, the result is Record Dictionary
    #except:                                            #In case of Excpetion
    #  return "Record Not Found"                       #Prints out Error Message
    for liNe in Record.keys():                         #Loops through the Keys in Record Dictionary
        Lines = Record[liNe]
    #print Lines+"\n"
    doc_node = ElementTree.XML(Lines)                  #Creates the XML Object from the String
    buf = ''
    severity=0
    for eLement in doc_node.getiterator(tag="record"):
        for attribs in eLement.attrib.keys():
            if attribs=="type":
                type=eLement.attrib[attribs]
    for eLement in doc_node.getiterator(tag="field"):  #Loops through the Fields
        for attribs in eLement.attrib.keys():
            if "Title" in eLement.attrib[attribs]:
                title=eLement.text
            if "Status" in eLement.attrib[attribs]:
                status=eLement.text
            if "AsysCategory" in eLement.attrib[attribs]:
                phase=eLement.text
            if "AssigneeGroup" in eLement.attrib[attribs]:
                assignee=eLement.text
            if "OwnerGroup" in eLement.attrib[attribs]:
                ownerg=eLement.text
            if "OnwerName" in eLement.attrib[attribs]:
                owneru=eLement.text
            if "BAMasterRecord" in eLement.attrib[attribs]:
                master=eLement.text
            if "EnteredDate" in eLement.attrib[attribs]:
                date_entered=eLement.text[:7]
            if "EnteredTime" in eLement.attrib[attribs]:
                time_entered=eLement.text[:5]
            if "LastModifyDate" in eLement.attrib[attribs]:
                date_last=eLement.text
            if "LastModifyTime" in eLement.attrib[attribs]:
                time_last=eLement.text
            #if "Severity" in eLement.attrib[attribs]:// Flop when there is a field named "SeverityOneAck" or "MaxSeverity"
            if eLement.attrib[attribs]=="Severity":
                severity=eLement.text
            if "MasterID" in eLement.attrib[attribs]:
                masterid=eLement.text
            if "MasterRecord" in eLement.attrib[attribs]:
                ismaster=eLement.text
    
    #buf = buf + eLement.attrib[attribs] + ': ' + eLement.text + '\n'
    if severity=="1" and type=="WO":
        severity=2
    pi=''
    pikey=''
    pistatus=''
    #print "1"+date_entered+" "+time_entered
    #print "2"+date_last+" "+time_last
    datetime_entered=time.strftime("%Y-%m-%d %H:%M:00",time.strptime(date_entered+" "+time_entered,"%d%b%y %H:%M"))
    datetime_last=time.strftime("%Y-%m-%d %H:%M:00",time.strptime(date_last+" "+time_last,"%d%b%y %H:%M"))
    asses=list()
    print status
    for eLement in doc_node.getiterator(tag="list"):  #Loops through the Fields
        for attribs in eLement.attrib.keys():
            if "MultiAssignedTo" in eLement.attrib[attribs]:
                for line in range(len(eLement)):
                    if eLement[line].text == "OIAOPS":
                        #print "PI:"+eLement[line].text
                        pi = eLement[line].text
                        print "GOT PI:"+pi
                        pikey = line
            if "MultiAssStatus" in eLement.attrib[attribs]:
                # print "PI Status:"+eLement[pikey].text
                for item in range(len(eLement)):
                    asses.append(eLement[item].text)
    # buf = buf + str(eLement.attrib[attribs]) + ': ' + str(eLement[0].text) + '\'
    if pi:
        pistatus=asses[pikey]
        print "pi status is "+pistatus
    
    for eLement in doc_node.getiterator(tag="fft"):  #Loops through the Fields
        for attribs in eLement.attrib.keys():
            if "StatusText" in eLement.attrib[attribs]:
                contents=list()
                for line in reversed(range(len(eLement))):
                    #print eLement[line].text
                    if eLement[line].text !="========================================================================":
                        if eLement[line].text:
                            contents.append(eLement[line].text)
                        else:
                            contents.append("")
                    else:
                        contents.append(eLement[line].text)
                        break
                contents.reverse()
                lastupdate='\n'.join(contents)
        #print lastupdate
        if not lastupdate:
            for attribs in eLement.attrib.keys():
                if "Description" in eLement.attrib[attribs]:
                    contents=list()
                    for line in reversed(range(len(eLement))):
                        #print eLement[line].text
                        if eLement[line].text !="========================================================================":
                            if eLement[line].text:
                                contents.append(eLement[line].text)
                            else:
                                contents.append("")
                        else:
                            contents.append(eLement[line].text)
                            break
                    contents.reverse()
                    lastupdate='\n'.join(contents)
        #print lastupdate
        if not lastupdate:
            for attribs in eLement.attrib.keys():
                if "Overview" in eLement.attrib[attribs]:
                    contents=list()
                    for line in reversed(range(len(eLement))):
                        if eLement[line].text !="========================================================================":
                            if eLement[line].text:
                                contents.append(eLement[line].text)
                            else:
                                contents.append("")
                        else:
                            contents.append(eLement[line].text)
                            break
                    contents.reverse()
                    lastupdate='\n'.join(contents)

        if pi!="" and pistatus in ['AS','AC','AA']:
            status=pistatus
            assignee=pi
    #print "~"+lastupdate+"~"
    lastupdate=lastupdate.replace("'","\\'")
    query="select id from records_tbl where recnum='"+recordId+"'"
    db.query(query)
    r=db.store_result()
    row=r.fetch_row()
    if not row:
        title="IR %s: %s" % (recordId,title)
        title=re.sub("'","\\'",title)
        query="insert into records_tbl values('','IR','%s','%s','IT Services Incident Management and Change','%s','%s','%s')" % (title,severity,datetime_entered,recordId,ismaster)
        #print query
        db.query(query)
    
    query="select datetime_last from record_details_tbl where recid='"+recordId+"'"
    db.query(query)
    r=db.store_result()
    row=r.fetch_row()
    #print "%s %s %s %s %s %s %s %s %s %s" % (status,assignee,ownerg,owneru,master,datetime_entered,datetime_last,lastupdate,severity,recordId)
    query="update record_details_tbl as rd, records_tbl as r,records_ptr_tbl as rp set rd.status='%s',rd.assignee='%s',rd.ownerg='%s',rd.owneru='%s',rd.master='%s',rd.datetime_entered='%s',rd.datetime_last='%s',rd.lastupdate='%s',rd.last_check=NOW(),r.severity='%s',rp.last_check='%s'  where rd.recid='%s' and rd.recid=r.recnum and rd.recid=rp.recnum" % (status,assignee,ownerg,owneru,master,datetime_entered,datetime_last,lastupdate,severity,datetime_last,recordId)
    #    print query
    if row:
        datetime_last1=row[0][0]
        query="update record_details_tbl as rd, records_ptr_tbl as rp set rd.last_check=NOW(),rp.last_check=NOW() where rd.recid='"+recordId+"' and rp.recnum=rd.recid"
        db.query(query)
        if not status in ['AS','AC','AA']:
            db.query("select UNIX_TIMESTAMP(date_accept) from notifier_accepts where recid="+recordId+" and date_closed='0000-00-00 00:00:00'")
            r=db.store_result()
            row=r.fetch_row()
            if row:
                db.query("update notifier_accepts as na, records_tmp_tbl as rt set na.date_closed=now(), rt.status='CM' where na.recid='"+recordId+"' and na.recid=rt.recnum")
                dateacc=row[0][0]
                mins=int(math.ceil(time2() - int(dateacc))/60)
                db.query("update trends.register set time_spent="+str(mins)+" where record_num='"+recordId+"' and log_type='1'")
        
        if status and assignee:
            query="update record_details_tbl as rd, records_tbl as r, records_ptr_tbl as rp set rd.status='%s',rd.assignee='%s',rd.ownerg='%s',rd.owneru='%s',rd.master='%s',rd.datetime_entered='%s',rd.datetime_last='%s',rd.lastupdate='%s',rd.last_check=NOW(),r.severity='%s',rp.last_check='%s'  where rd.recid='%s' and rd.recid=r.recnum  and rd.recid=rp.recnum" % (status,assignee,ownerg,owneru,master,datetime_entered,datetime_last,lastupdate,severity,datetime_last,recordId)
            #print query
            db.query(query)
        else:
            print "error"
    else:
        if status and assignee:
            query="insert into record_details_tbl (recid,status,phase,assignee,ownerg,owneru,master,datetime_entered,datetime_last,lastupdate,last_check) value('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',NOW())" % (recordId,status,phase,assignee,ownerg,owneru,master,datetime_entered,datetime_last,lastupdate)
            print query
            db.query(query)
            db.query("update records_tbl as r set r.severity='"+str(severity)+"' where r.recnum='"+recordId+"'")
        else:
            print "error"

def getRecordId(searchRec,name):#efines getRecordId Function using a 2 Items List with Record Type and Record Title
    recTyp,sev = searchRec.split(",")                #Splits the List into Variables recTyp and tiTle
    #tiTle = re.sub("[/:-]"," ",tiTle)                  #Substitutes : and - with Space
    mygroup='OIAOPS'
    if name=="ROBERTS":
        mygroup="OIA030"
    
    #db.query("delete from records_ptr_tbl where owner='"+name+"' and severity='"+sev+"'")
    searchItem = '<record type="%s" database="PRD"><select><field pword="TYPE" /></select><where><clause>((GROC/%s))</clause><clause>((PERC/%s))</clause><clause>((PRIO/%s))</clause></where></record>' % (str(recTyp).upper(),mygroup,name,sev) #Builds Up the Message to Search fori
    #searchItem = '<record type="%s" database="PRD"><select><field pword="TYPE" /></select><where><clause>((GROC/%s))</clause><clause>((PERC/%s))</clause><clause>((PRIO/%s))</clause></where></record>' % (tiTle,mygroup,name,sev)
    
    #print searchItem
    try:                                               #Tests next Instruction
        Record = b.search(searchItem)                   #Rmeetrieves the Search Found
    #print Record
    except:                                            #In case of Exception
        return "Record Not Found"                       #Prints out Error Message
    for liNe in Record.keys():                         #Loops through the Keys in Record Dictionary
        Lines = Record[liNe]                            #Lines is the Content of the Record Dictionary Ke
    #print Lines
    doc_node = ElementTree.XML(Lines)                  #Creates the XML Object from the String
    title=''
    status=''
    recordNum=''
    assignee=''
    #for eLement in doc_node.getiterator():             #Loops through the Element
    #     if "id" in eLement.keys(): #id is one of the Element Keys then Returns the Record Nr
    #         if eLement.attrib["id"]:
    #             recordNum=eLement.attrib["id"]
    title=''
    status=''
    recordNum=''
    assignee=''
    date_last=''
    time_last=''
    for eLement in doc_node.getiterator():  #Loops through the Fields
        for attribs in eLement.attrib.keys():
            #print eLement.attrib[attribs]
            if "Title" in eLement.attrib[attribs]:
                title=eLement.text
            if "Status" in eLement.attrib[attribs]:
                status=eLement.text
            if "id" in eLement.keys():
                if eLement.attrib["id"]:
                    recordNum=eLement.attrib["id"]
            if "AssigneeGroup" in eLement.attrib[attribs]:
                assignee=eLement.text
        if title and status and recordNum and assignee:
            print "PTR %s %s\t%s\t%s %s" % (recordNum,title,status,assignee,date_last)
            title=''
            status=''
            recordNum=''
            assignee=''
            time_last=''
            date_last=''

#db.query("select rd.recid from records_tbl as r, record_details_tbl as rd where r.recnum=rd.recid and rd.recid='"+eLement.attrib["id"]+"'")
#r=db.store_result()
#row=r.fetch_row()
#if not row:
#   getTitle(eLement.attrib["id"])
#print eLement.attrib["id"]



def main():
    db.query("select user_name from trends.users where site='Miami'")
    r=db.store_result()
    for row in r.fetch_row(100):
        fname,lname=row[0].split(" ")
        lname=lname.upper()
        if lname=='FLORES':
            lname='G_Flores'
        print lname
        getRecordId("PTR,2",lname) #Check all open records to make sure we dont miss any open records
        #       getRecordId("PTR,2",lname)
        #        getRecordId("PTR,3",lname)
        getRecordId("PTR,3",lname)
#print getRecordId(["TR","TPF GC BE Software - Load Cycle 2009-44"]) #Gets the Record Number searching the Record Type + Record Title

if __name__ == '__main__':                            #If gets called
    main()                                             #Call main() Function
