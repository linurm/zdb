import os
#from device import *
import AGDBDir
import sys
#import utils


####################################################################

if __name__=='__main__':
    addr = AGDBDir.AGDB().getAllDir()

    apktool_dir = "{}".format(addr['apktool_dir'])
    pkg_dir = "{}".format(addr['pkg_dir'])
    dex2jar_dir = "{}".format(addr['dex2jar_dir'])
    apk_name = "{}".format(addr['apk_name'])
    smali_dir = "{}".format(addr['smali_dir'])
    pkg_path = "{}\\{}".format(pkg_dir, apk_name)    
 
    # jar to dex
    cmd = '{}\\d2j-jar2dex.bat {}\\{}-updateclass.jar -f -o {}\\{}.dex'.format(dex2jar_dir, pkg_path, apk_name, pkg_path, apk_name)
    print '#######',cmd
    os.system("{}".format(cmd))
    
    # dex to smali
    cmd = 'java -jar {}\\baksmali-2.1.3.jar {}\\{}.dex -f -o {}\\smali'.format(smali_dir,pkg_path, apk_name, pkg_path)
    print '#######',cmd
    os.system("{}".format(cmd))
    #raw_input('')
'''
%ADB_DIR%\adb shell am start -D -n dascom.telecom.vipclub/dascom.telecom.vipclub.InitActivity
rem %ADB_DIR%\adb shell am start -D -n zj.zfenlly.tools/zj.zfenlly.main.MainActivity
call test.bat
'''
