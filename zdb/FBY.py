import os
from device import *
import AGDBDir
import sys
import utils
import time


################################################

####################################################################
def InstallApk(apkname):
    addr = AGDBDir.AGDB().getAllDir2()
    #adb_path = addr['adb_dir'] + "\\adb"
    #print adb_path
    dev = utils.getDeviceLoop(adb_path=addr['adb_dir']+"\\adb")

        
    
    #input('========')
    adb_v = utils.getVersion(dev)
    dev.remount()
    print '====',adb_v
    
    #apktool_dir = "{}".format(addr['apktool_dir'])
    #dex2jar_dir = "{}".format(addr['dex2jar_dir'])
    pkg_dir = "{}".format(addr['pkg_dir'])
    apk_name = "{}".format(addr['apk_name'])
    pkg_path = "{}\\{}".format(pkg_dir, apk_name) 
    
    if apkname == '':
        cmd = '{}\\{}-signed.apk'.format(pkg_path, apk_name)
    else:
        cmd = apkname
    
    
    # install apk
    print '#######',cmd
    #raw_input('')
    try:
        dev.install(cmd, True)
    except subprocess.CalledProcessError as e:
        print '',e
    
    #os.system("{}".format(cmd))
    time.sleep(3)
    #input("end")
    
####################################################################
def RebuildApk(apkname):
    addr = AGDBDir.AGDB().getAllDir2()

    apktool_dir = "{}".format(addr['apktool_dir'])
    pkg_dir = "{}".format(addr['pkg_dir'])
    dex2jar_dir = "{}".format(addr['dex2jar_dir'])
    apk_name = "{}".format(addr['apk_name'])
    pkg_path = "{}\\{}".format(pkg_dir, apk_name)    
    
    
    if apkname != '':
        # rebuild
        print apkname
        cmd = '{}\\apktool.bat b {}'.format(apktool_dir, apkname)
        print '#######', cmd
        os.system("{}".format(cmd))
        
        index = apkname.rfind("\\")
        
        nameapk = apkname[index+1:]
        
        namedir = apkname[:index]
        
        print nameapk
        signedapk = '{}\\{}-signed.apk'.format(namedir, nameapk)
        #apk to jar
        cmd = 'jarsigner -verbose -keystore android.keystore -storepass 123456 -keypass 123456 -signedjar {} {}\\dist\\{}.apk android.keystore'.format(signedapk, apkname, nameapk)
        print '#######',cmd
        os.system("{}".format(cmd))
    else:
        # rebuild
        cmd = '{}\\apktool.bat b {}\\{}'.format(apktool_dir, pkg_path, apk_name)
        print '#######',cmd
        os.system("{}".format(cmd))

        signedapk = '{}\\{}-signed.apk'.format(pkg_path, apk_name)
        #apk to jar
        cmd = 'jarsigner -verbose -keystore android.keystore -storepass 123456 -keypass 123456 -signedjar {} {}\\{}\\dist\\{}.apk android.keystore'.format(signedapk, apk_name, pkg_path, apk_name, apk_name)
        print '#######', cmd
        os.system("{}".format(cmd))
    #input("")
    #time.sleep(3)
    return signedapk
###################################################################
def FbyApk(apkname):
    #raw_input('')
    addr = AGDBDir.AGDB().getAllDir2()

    apktool_dir = "{}".format(addr['apktool_dir'])
    pkg_dir = "{}".format(addr['pkg_dir'])
    dex2jar_dir = "{}".format(addr['dex2jar_dir'])
    apk_name = "{}".format(addr['apk_name'])
    smali_dir = "{}".format(addr['smali_dir'])
    pkg_path = "{}\\{}".format(pkg_dir, apk_name)    
    
    
    if apkname != '':
        index = apkname.rfind("\\")
        print ''
        #print index
        #raw_input('')
        apkdir = apkname[0:index]
        print apkdir
        #C:\Users\Administrator\Desktop
        #raw_input('')
        nameapk = apkname[index+1:]
        #raw_input('')
        #print nameapk
        index = nameapk.rfind('.')
        #raw_input('')
        aname = nameapk[0:index]
        print aname
        #ti.android.ble.devicemonitor_1.12_6
        #raw_input('')
        
        # apk(dex) to smali
        cmd = '{}\\apktool.bat d -f {} -o {}\\{}\\{}'.format(apktool_dir, apkname, apkdir, aname, aname)
        print '#######',cmd
        os.system("{}".format(cmd))
         
        # apk(dex) to jar       
        cmd = '{}\\d2j-dex2jar.bat {} -f -o {}\\{}\\{}.jar'.format(dex2jar_dir, apkname, apkdir, aname, aname)
        print '#######',cmd
        os.system("{}".format(cmd))
    else:
        # apk(dex) to smali
        cmd = '{}\\apktool.bat d -f {}.apk -o {}\\{}'.format(apktool_dir, pkg_path, pkg_path, apk_name)
        print '#######',cmd
        os.system("{}".format(cmd))

        # apk(dex) to jar
        cmd = '{}\\d2j-dex2jar.bat {}.apk -f -o {}\\{}.jar'.format(dex2jar_dir, pkg_path, pkg_path, apk_name)
        print '#######',cmd
        os.system("{}".format(cmd))
    raw_input('end')
    time.sleep(3)

###############################################    
    
    
    
    
    
    
    
    
    