import os
from device import *
import AGDBDir
import sys
import utils


####################################################################

if __name__=='__main__':
    addr = AGDBDir.AGDB().getAllDir()
    dev = utils.getDevice(adb_path=addr['adb_dir']+"\\adb")
    adb_v = utils.getVersion(dev)
    dev.remount()
    
    
    #apktool_dir = "{}".format(addr['apktool_dir'])
    #dex2jar_dir = "{}".format(addr['dex2jar_dir'])
    pkg_dir = "{}".format(addr['pkg_dir'])
    apk_name = "{}".format(addr['apk_name'])
    pkg_path = "{}\\{}".format(pkg_dir, apk_name) 
    
    cmd = '{}\\{}-signed.apk'.format(pkg_path, apk_name)
    
    
    # install apk
    print '########################'
    print cmd
    
    dev.install(cmd, True)
    #os.system("{}".format(cmd))

    #input("")
'''
%ADB_DIR%\adb shell am start -D -n dascom.telecom.vipclub/dascom.telecom.vipclub.InitActivity
rem %ADB_DIR%\adb shell am start -D -n zj.zfenlly.tools/zj.zfenlly.main.MainActivity
call test.bat
'''
