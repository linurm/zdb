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
    
    

    # apk(dex) to smali
    #print '########################'
    #cmd = '{}\\apktool.bat d -f {}.apk -o {}\\{}'.format(apktool_dir, pkg_path, pkg_path, apk_name)
    #print cmd
    #os.system("{}".format(cmd))

    # apk(dex) to jar
    #cmd = '{}\\d2j-dex2jar.bat {}.apk -f -o {}\\{}no1.jar'.format(dex2jar_dir, pkg_path, pkg_path, apk_name)
    #print '########################'
    #print cmd
    #os.system("{}".format(cmd))
    
    # jar to dex
    #cmd = '{}\\d2j-modefy-class.bat {}\\{}.jar -f -o {}\\{}.dex'.format(dex2jar_dir, pkg_path, apk_name, pkg_path, apk_name)
    #print '########################'
    #print cmd
    #os.system("{}".format(cmd))
    
    # class join jar
    '''list_class = '{}\\classlist.txt'.format(pkg_path)
    file = open(list_class)
     
    while 1:
        line = file.readline()
        if not line:
            break
        #print line
        index = line.rfind('/')
        pkg = line[0:index].replace('/','.')
        clz = line[index+1:]
        index = clz.find('.')
        name = clz[0:index]
        hz = clz[index+1:]
        classfile = clz[:-1]'''
    cmd = '{}\\d2j-class-update-jar.bat {}\\classlist.txt -i {}\\{}.jar -f -o {}\\{}-addclass.jar -p {}\\classmodefy'.format(dex2jar_dir, pkg_path, pkg_path, apk_name, pkg_path, apk_name, pkg_path)
    print '#######',cmd
        #cmd = '{}\\d2j-class-join-jar.bat {}\\addclass\\Utils.class -i {}\\{}.jar -f -p com.googlecode.dex2jar.tools.ZjUtils -o {}\\{}-addclass.jar'.format(dex2jar_dir, pkg_path, pkg_path, apk_name, pkg_path, apk_name)
        #print '#######',cmd
    os.system("{}".format(cmd))
    raw_input('Pause')
'''
%ADB_DIR%\adb shell am start -D -n dascom.telecom.vipclub/dascom.telecom.vipclub.InitActivity
rem %ADB_DIR%\adb shell am start -D -n zj.zfenlly.tools/zj.zfenlly.main.MainActivity
call test.bat
'''
