import os
from device import *
import AGDBDir
import sys
import utils

########################################################

################################################
def adbForward(dev):
    port = "23946"
    str = "tcp:{}".format(port)
    print ("adb forward {}".format(str))
    dev.forward(str, str)
####################################################################

if __name__=='__main__':
    addr = AGDBDir.AGDB().getAllDir()
    dev = utils.getDevice(adb_path=addr['adb_dir']+"\\adb")
    adb_v = utils.getVersion(dev)
    dev.remount()
    adbForward(dev)
	
    raw_input("")
