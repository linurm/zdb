import os
from device import *
import AGDBDir
import sys
import utils

########################################################

################################################
def pushGdbserver(dev, gdb_path):
    win_gdbserver_path = "{}\\gdbserver".format(gdb_path)
    print (win_gdbserver_path)
    dev_gdbserver_path = "/data/gdbserver"
    cmd = ["ls", dev_gdbserver_path, "2>/dev/null"]
    (rc, _, _) = dev.shell_nocheck(cmd)
    #print rc
    if rc == 0:
        print ("Found app gdbserver: {}".format(dev_gdbserver_path))
        #return dev_gdbserver_path
    else:
        print ("push gdbserver")
        dev.push(win_gdbserver_path, dev_gdbserver_path)
    #dev.push(addr['adb_dir']+"\\gdbserver", "/data")
    
    cmd = ["chmod", "777", dev_gdbserver_path]
    dev.shell_nocheck(cmd)
################################################
def pushAndroidserver(dev, as_path):
    win_androidserver_path = "{}\\add\\android_server".format(as_path)
    print (win_androidserver_path)
    dev_androidserver_path = "/data/android_server"
    cmd = ["ls", dev_androidserver_path, "2>/dev/null"]
    (rc, _, _) = dev.shell_nocheck(cmd)
    #print rc
    if rc == 0:
        print ("Found app android_server: {}".format(dev_androidserver_path))
        #return dev_androidserver_path
    else:
        print ("push android_server")
        dev.push(win_androidserver_path, dev_androidserver_path)
    cmd = ["chmod", "777", dev_androidserver_path]
    dev.shell_nocheck(cmd)
    #dev.push(addr['adb_dir']+"\\gdbserver", "/data")

####################################################################

if __name__=='__main__':
    addr = AGDBDir.AGDB().getAllDir()
    dev = utils.getDevice(adb_path=addr['adb_dir']+"\\adb")
    adb_v = utils.getVersion(dev)
    dev.remount()

    
    pushGdbserver(dev, addr['gdbserver_dir'])
    pushAndroidserver(dev, addr['adb_dir'])

    
    raw_input("success and exit")
    #os.system('cmd')

        
