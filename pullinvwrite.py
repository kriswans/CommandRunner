## This defines functions to connect to an IOS switches and Router,
# pull the inventory and hostname and print that to a file with the hostname of the Cisco device
#It will do this in a single row, with the hostname and IP in the first 2 columns
#use: pip install -e git+https://github.com/paramiko/paramiko/#egg=paramiko to install paramiko for ssh connectivity

import paramiko

host='192.168.220.238'
username='cisco'
password='cisco'

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
        #print (line.strip())
        cmdout=open('cmdoutput.csv','a')
        cmdout.write(line.strip())
        cmdout.write(',')
        cmdout.close()
  ssh.close()
