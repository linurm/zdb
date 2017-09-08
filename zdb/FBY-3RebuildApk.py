from FBY import *



####################################################################

if __name__=='__main__':
    apkname = ''
    if len(sys.argv) == 1:
        print '1'
    else:
        apkname = raw_input('input build apk dir: ')
    
    RebuildApk(apkname)
'''
%ADB_DIR%\adb shell am start -D -n dascom.telecom.vipclub/dascom.telecom.vipclub.InitActivity
rem %ADB_DIR%\adb shell am start -D -n zj.zfenlly.tools/zj.zfenlly.main.MainActivity
call test.bat
'''
