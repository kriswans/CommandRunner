## This defines functions to connect to an IOS switches and Router,
# pull the inventory and hostname and print that to a file with the hostname of the Cisco device
#It will do this in a single row, with the hostname and IP in the first 2 columns
#use: pip install -e git+https://github.com/paramiko/paramiko/#egg=paramiko to install paramiko for ssh connectivity

import sys
import paramiko
from contextlib import suppress
import datetime
import time

line_do=[]

def  show_inventory_raw(host):

  cmdout=open('cmdoutput.csv','a')
  cmdout.write(host)
  cmdout.close()

  ssh = paramiko.SSHClient()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  try:
        ssh.connect(host, username='cisco', password='cisco')
  except paramiko.SSHException:
        print ("Connection Failed")
        quit()

  stdin,stdout,stderr = ssh.exec_command("show invent raw")

  for line in stdout.readlines():
        #print (line.strip())
        cmdout=open('cmdoutput.csv','a')
        cmdout.write(','+line.strip())
        cmdout.close()
  ssh.close()

  cmdout=open('cmdoutput.csv','a')
  cmdout.write('\n')
  cmdout.close()

def  show_hostname(host):

  ssh = paramiko.SSHClient()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  try:
        ssh.connect(host, username='cisco', password='cisco')
  except paramiko.SSHException:
        print ("Connection Failed")
        quit()

  stdin,stdout,stderr = ssh.exec_command("show run | incl hostname")

  for line in stdout.readlines():
        cmdout=open('cmdoutput.csv','a')
        cmdout.write(line.strip())
        cmdout.write(',')
        cmdout.close()
  ssh.close()


def HostsCreateList():
    ## make sure to set line_do=[] outside of this function and before it's called in the program
    with open('hosts_list','r') as h_l:
      for h_rows in h_l:
        h_str_row=h_rows.strip()
        line_do.append(h_str_row)
      host_list_len=(len(line_do))
      h_i=0
    while h_i < host_list_len :
        try:
          show_hostname(line_do[h_i])
          show_inventory_raw(line_do[h_i])
          h_i+=1
        except Exception:
          print("There was a problem connecting ssh to: {ld}, please make sure device exists and is reachable.".format(ld=line_do[h_i]))
          ts = time.time()
          st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
          error_file=open('error_file.txt','a')
          error_file.write("Using HostsCreateList Function's Exception:\n")
          error_file.write("{timestp}||>there was a problem connecting ssh to: {ld} at {timestp}\n".format(ld=line_do[h_i], timestp=st))
          error_file.write("{timestp}||>the list length counter is at:{hi}, the host list length is: {hll} at {timestp}\n".format(hi=h_i,hll=host_list_len, timestp=st))
          error_file.close()
          rm_line=line_do[h_i]
          line_do.remove(rm_line)
          host_list_len=len(line_do)
          LoopThruHosts(h_i,host_list_len)

def LoopThruHosts(h_i,host_list_len):
          while h_i <= host_list_len :
            try:
              show_hostname(line_do[h_i])
              show_inventory_raw(line_do[h_i])
              h_i+=1
            except Exception:
              print("There was a problem connecting ssh to: {ld}, please make sure device exists and is reachable.".format(ld=line_do[h_i]))
              ts = time.time()
              st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
              error_file=open('error_file.txt','a')
              error_file.write("Using LoopThruHosts Fucntions Exception:\n")
              error_file.write("{timestp}||>there was a problem connecting ssh to: {ld} at {timestp}\n".format(ld=line_do[h_i], timestp=st))
              error_file.write("{timestp}||>the list length counter is at:{hi}, the host list length is: {hll} at {timestp}\n".format(hi=h_i,hll=host_list_len, timestp=st))
              error_file.close()
              rm_line=line_do[h_i]
              line_do.remove(rm_line)
              host_list_len=len(line_do)
              LoopThruHosts(h_i,host_list_len)
