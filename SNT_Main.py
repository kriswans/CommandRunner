import sys
import copy
import HostListBuilder
import time
import paramiko
import pullinvwrite
import netaddr
import datetime

prefix='0'
lo_h=0
hi_h=0

start=0
while start != 10:
    print(56*'*')
    print('*  '+'Please Enter Your Choice: '+'                          *')
    print('*  '+'1=Enter Address Range to add to Host List'+'           *')
    print('*  '+'2=Run Inventory against the Host List'+'               *')
    print('*  '+'3=Print the Host List'+'                               *')
    print('*  '+"0=Enter '0' to quit                        "+'         *')
    print(56*'*')
    menu_choice=input('->')
    start!=1
    if menu_choice == str(1):
        HostListBuilder.RangePrinter(prefix,lo_h,hi_h)
        start=0
    if menu_choice == str(2):
        print(2*'\n')
        pullinvwrite.HostsCreateList()
        break
        print(2*'\n')
        start=0
    if menu_choice == str(3):
        print(2*'\n')
        HostListBuilder.PrintHostList()
        print(2*'\n')
        start=0
    if menu_choice == str(0):
        break
    start+=1
print("\n\nThanks for stopping by...exiting now")
