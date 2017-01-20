import os
from device import *
import AGDBDir
import sys
import utils

if __name__=='__main__':
    addr = AGDBDir.AGDB().getAllDir()
    #dev = utils.getDevice(adb_path=addr['adb_dir']+"\\adb")
    #adb_v = utils.getVersion(dev)
    #dev.remount()
    jdb_port = raw_input(" please input the jdb PORT(android monitor.exe debug port): ")
    while True:
        restart_jdb = raw_input(" please enter 'r' for exit jdb or restarting jdb   ")
        if restart_jdb == 'r':
            print 'restart'
            sys.exit(4)#return 1
        utils.jdb_connect(jdb_port)



