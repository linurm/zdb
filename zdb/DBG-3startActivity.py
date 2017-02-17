import os
from device import *
import AGDBDir
import sys
import utils
import subprocess
import re
####################################################################

if __name__=='__main__':
    addr = AGDBDir.AGDB().getAllDir()
    dev = utils.getDevice(adb_path=addr['adb_dir']+"\\adb")
    adb_v = utils.getVersion(dev)
    dev.remount()

    while True:

        am_cmd = ["am", "start"]
        #am_cmd.append("-D")
        component_name = "{}/{}".format(addr['pkg_name'], addr['launch_name'])
        am_cmd.append(component_name)
        print ("Launching activity {}...".format(component_name))
        (rc, _, _) = dev.shell_nocheck(am_cmd)
        if rc != 0:
            utils.error("Failed to start {}".format(component_name))
        break


    print ("exit  ")
    #print p1
'''
%ADB_DIR%\adb shell am start -D -n dascom.telecom.vipclub/dascom.telecom.vipclub.InitActivity
rem %ADB_DIR%\adb shell am start -D -n zj.zfenlly.tools/zj.zfenlly.main.MainActivity
call test.bat
'''
