import os
from device import *
import AGDBDir
import sys
import utils
import time


################################################

####################################################################
def InstallApk(apkname):
    addr = AGDBDir.AGDB().getAllDir()
    #adb_path = addr['adb_dir'] + "\\adb"
    #print adb_path
    while(True):
        dev = utils.getDevice(adb_path=addr['adb_dir']+"\\adb")
        if dev == None:
            time.sleep(3)
        else:
            break
        
    
    #input('========')
    adb_v = utils.getVersion(dev)
    dev.remount()
    
    
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
    
    dev.install(cmd, True)
    
    
    #os.system("{}".format(cmd))

    #input("end")
    
####################################################################
def RebuildApk():
    addr = AGDBDir.AGDB().getAllDir()

    apktool_dir = "{}".format(addr['apktool_dir'])
    pkg_dir = "{}".format(addr['pkg_dir'])
    dex2jar_dir = "{}".format(addr['dex2jar_dir'])
    apk_name = "{}".format(addr['apk_name'])
    pkg_path = "{}\\{}".format(pkg_dir, apk_name)    
    cmd = '{}\\apktool.bat b {}\\{}'.format(apktool_dir, pkg_path, apk_name)
    

    # rebuild
    print '#######',cmd
    os.system("{}".format(cmd))

    #apk to jar
    cmd = 'jarsigner -verbose -keystore android.keystore -storepass 123456 -keypass 123456 -signedjar {}\\{}-signed.apk {}\\{}\\dist\\{}.apk android.keystore'.format(pkg_path, apk_name, pkg_path, apk_name, apk_name)
    print '#######',cmd
    os.system("{}".format(cmd))
    #input("")
    
###################################################################
def FbyApk(apkname):
    #raw_input('')
    addr = AGDBDir.AGDB().getAllDir()

    apktool_dir = "{}".format(addr['apktool_dir'])
    pkg_dir = "{}".format(addr['pkg_dir'])
    dex2jar_dir = "{}".format(addr['dex2jar_dir'])
    apk_name = "{}".format(addr['apk_name'])
    smali_dir = "{}".format(addr['smali_dir'])
    pkg_path = "{}\\{}".format(pkg_dir, apk_name)    
    cmd = '{}\\apktool.bat d -f {}.apk -o {}\\{}'.format(apktool_dir, pkg_path, pkg_path, apk_name)
    
    if apkname != '':
        index = apkname.rfind("\\")
        print ''
        #print index
        #raw_input('')
        apkdir = apkname[0:index]
        print apkdir
        #raw_input('')
        nameapk = apkname[index+1:]
        #raw_input('')
        #print nameapk
        index = nameapk.rfind('.')
        #raw_input('')
        aname = nameapk[0:index]
        print aname
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
        print '#######',cmd
        os.system("{}".format(cmd))

        # apk(dex) to jar
        cmd = '{}\\d2j-dex2jar.bat {}.apk -f -o {}\\{}.jar'.format(dex2jar_dir, pkg_path, pkg_path, apk_name)
        print '#######',cmd
        os.system("{}".format(cmd))
    #raw_input('end')
    

###############################################    
    
    
    
    
    
    
    
    
    