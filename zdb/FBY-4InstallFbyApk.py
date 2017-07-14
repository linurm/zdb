from FBY import *


####################################################################

if __name__=='__main__':
    apkname = ''
    for arg in sys.argv:  
        print arg
        if arg.endswith('.apk'):
            apkname = arg
    print apkname
    #os.system("adbdevice.bat");
    InstallApk(apkname)
    
'''
%ADB_DIR%\adb shell am start -D -n dascom.telecom.vipclub/dascom.telecom.vipclub.InitActivity
rem %ADB_DIR%\adb shell am start -D -n zj.zfenlly.tools/zj.zfenlly.main.MainActivity
call test.bat
'''
