from FBY import *



####################################################################

if __name__=='__main__':
    apkname = ''
    print len(sys.argv)
    if len(sys.argv) == 1:
        print '1'
    elif len(sys.argv) == 2:
        #apkname = sys.argv
        apkname = sys.argv[1]
    else:
        apkname = raw_input('input build apk dir: ')
    
    #raw_input('')
    RebuildApk(apkname)
'''
%ADB_DIR%\adb shell am start -D -n dascom.telecom.vipclub/dascom.telecom.vipclub.InitActivity
rem %ADB_DIR%\adb shell am start -D -n zj.zfenlly.tools/zj.zfenlly.main.MainActivity
call test.bat
'''
