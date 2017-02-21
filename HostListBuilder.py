
prefix='0'
lo_h=0
hi_h=0

def RangePrinter(prefix,lo_h,hi_h):
  prefix='0'
  lo_h=0
  hi_h=0
  try:
    if prefix == '0':
      prefix=input('Enter the First 3 Octets:\n->')
    if lo_h == 0:
      lo_h=int(input('Enter the first host:\n->'))
    if hi_h ==0:
      hi_h=int(input('Enter the last host:\n->'))
    host_index=0
    hosts=range(lo_h,hi_h+1)
    for addys in hosts:
      str_addys=str(addys)
      host_index+=1
      ip_addr=prefix+'.'+str_addys
      print(host_index, ip_addr)
      ip_file=open('hosts_list','a')
      ip_file.write(ip_addr)
      ip_file.write('\n')
      ip_file.close()
  except ValueError: print('upper and lower bounds require numerical value')

def PrintHostList():
    with open('hosts_list','r') as h_l:
      for h_rows in h_l:
        h_str_row=h_rows.strip()
        print(h_str_row)
