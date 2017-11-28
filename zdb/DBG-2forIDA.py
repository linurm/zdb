import os
from device import *
import AGDBDir
import sys
from utils import *
########################################################

################################################

####################################################################

if __name__=='__main__':
    addr = AGDBDir.AGDB().getAllDir2()
    dev = getDevice(adb_path=addr['adb_dir']+"\\adb")
    adb_v = getVersion(dev)
    print dev.remount()

    
    #os.system('cmd')
    cmd = ["/data/android_server"]
    dev.shell_popen(cmd) 

	
    adbForward(dev)
    raw_input("")
