from FBY import *
#import utils


####################################################################

if __name__=='__main__':
    apkname = ''
    for arg in sys.argv:  
        print arg
        if arg.endswith('.apk'):
            apkname = arg
    FbyApk(apkname)
    raw_input('')
'''
%ADB_DIR%\adb shell am start -D -n dascom.telecom.vipclub/dascom.telecom.vipclub.InitActivity
rem %ADB_DIR%\adb shell am start -D -n zj.zfenlly.tools/zj.zfenlly.main.MainActivity
call test.bat
'''
