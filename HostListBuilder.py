
prefix='0'
lo_h=0
hi_h=0

def RangePrinter(prefix,lo_h,hi_h):
  try:
    if prefix == '0':
      prefix=input('Enter the First 3 Octets:\n->')
    if lo_h == 0:
      lo_h=int(input('Enter the first host:\n->'))
    if hi_h ==0:
      hi_h=int(input('Enter the last host:\n->'))
    host_index=0
    hosts=range(lo_h,hi_h)
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

#RangePrinter(prefix,lo_h,hi_h)
