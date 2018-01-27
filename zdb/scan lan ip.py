

import platform 
import sys 
import os 
import time 
import thread 
import os

from socket import gethostbyname, gethostname

host = gethostbyname(gethostname())
  
def get_os(): 
  os = platform.system() 
  if os == "Windows": 
    return "n"
  else: 
    return "c"
    
def find_mac(ip):
    os.system('arp -a > temp.txt')
    with open('temp.txt') as fp:
        for line in fp:
            line = line.split()[:2]                        #print line            
            if(line and line[0] == ip):
                if line and line[0].startswith(host[:4]) and (not line[0].endswith('255')):
                    print(line[1] + ' : ' + (line[0]) + ' is ok ***')
                    
def ping_ip(ip_str): 
  cmd = ["ping", "-{op}".format(op=get_os()), 
      "1", ip_str] 
  output = os.popen(" ".join(cmd)).readlines() 
    
  flag = False
  for line in list(output): 
    if not line: 
      continue
    if str(line).upper().find("TTL") >=0: 
      flag = True
      break
  if flag: 
    find_mac(ip_str)
    #print "ip: %s is ok ***"%ip_str 
  
def find_ip(ip_prefix): 
  ''''' 
  '''
  for i in range(1,256): 
    ip = '%s.%s'%(ip_prefix,i) 
    thread.start_new_thread(ping_ip, (ip,)) 
    time.sleep(0.3) 
    
if __name__ == "__main__": 
  print "start time %s"%time.ctime() 
  commandargs = sys.argv[1:] 
  commandargs = host
  args = "".join(commandargs)   
    
  ip_prefix = '.'.join(args.split('.')[:-1]) 
  #print ip_prefix
  find_ip(ip_prefix) 
  print "end time %s"%time.ctime()