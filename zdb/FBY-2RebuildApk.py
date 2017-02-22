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
    pkg_path = "{}\\{}".format(pkg_dir, apk_name)    
    cmd = '{}\\apktool.bat b {}\\{}'.format(apktool_dir, pkg_path, apk_name)
    

    # rebuild
    print '########################'
    print cmd
    os.system("{}".format(cmd))

    #apk to jar
    cmd = 'jarsigner -verbose -keystore android.keystore -signedjar {}\\{}-signed.apk {}\\{}\\dist\\{}.apk android.keystore'.format(pkg_path, apk_name, pkg_path, apk_name, apk_name)
    print '########################'
    print cmd
    os.system("{}".format(cmd))
    #input("")
'''
%ADB_DIR%\adb shell am start -D -n dascom.telecom.vipclub/dascom.telecom.vipclub.InitActivity
rem %ADB_DIR%\adb shell am start -D -n zj.zfenlly.tools/zj.zfenlly.main.MainActivity
call test.bat
'''
