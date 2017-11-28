import os
from device import *
import AGDBDir
import sys
import utils
from ADB import *
########################################################

####################################################################

if __name__=='__main__':
    addr = AGDBDir.AGDB().getAllDir()
    dev = utils.getDevice(adb_path=addr['adb_dir']+"\\adb")
    adb_v = utils.getVersion(dev)
    dev.remount()
    adbForward(dev)
	
    raw_input("")
