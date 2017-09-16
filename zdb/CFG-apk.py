import sys
import time
import AGDBDir
import os
####################################################################

if __name__=='__main__':
    apkname = ''
    for arg in sys.argv: 
        print arg
        if arg.endswith('.apk'):
            index = arg.rfind('\\')
            index2 = arg.find(".apk")
            print index
            if index == -1:
                index = index
            else:
                apkname = arg[index + 1: index2]
                #AGDBDir.AGDB().setConfig("apk_name", apkname)
    print apkname
    time.sleep(3)
    #FbyApk(apkname)
    raw_input('over')
'''
%ADB_DIR%\adb shell am start -D -n dascom.telecom.vipclub/dascom.telecom.vipclub.InitActivity
rem %ADB_DIR%\adb shell am start -D -n zj.zfenlly.tools/zj.zfenlly.main.MainActivity
call test.bat
'''
