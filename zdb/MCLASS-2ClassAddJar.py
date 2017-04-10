import os
#from device import *
import AGDBDir
import sys
import utils
import shutil
import zipfile
####################################################################

if __name__=='__main__':
    addr = AGDBDir.AGDB().getAllDir()

    apktool_dir = "{}".format(addr['apktool_dir'])
    pkg_dir = "{}".format(addr['pkg_dir'])
    dex2jar_dir = "{}".format(addr['dex2jar_dir'])
    apk_name = "{}".format(addr['apk_name'])
    smali_dir = "{}".format(addr['smali_dir'])
    add_clas_dirname = "{}".format(addr['add_clas_dirname'])
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
    class_dir = '{}\\{}'.format(pkg_path, add_clas_dirname)
    utils.mkdir(class_dir)
    
    pkg = 'com.googlecode.dex2jar.tools.ZjUtils'
    cn = 'Utils'
    
    fromjar = '{}\\{}.jar'.format(pkg_path, apk_name)
    tojar = '{}\\{}-addclass.jar'.format(pkg_path, apk_name)
    shutil.copyfile(fromjar, tojar)
    class_path = class_dir + os.sep + cn + '.class'
    # class join jar
    zf = zipfile.ZipFile(tojar, 'a')
    entry = pkg.replace('.', '/') + os.sep + cn + '.class'
    zf.write(class_path, entry)
    zf.close()
    
    cmd = '{}\\d2j-class-join-jar.bat {}\\classjoin\\Utils.class -i {}\\{}.jar -f -p com.googlecode.dex2jar.tools.ZjUtils -o {}\\{}-addclass.jar'.format(dex2jar_dir, pkg_path, pkg_path, apk_name, pkg_path, apk_name)
    print '#######',cmd
    #os.system("{}".format(cmd))
    raw_input('Pause')
'''
%ADB_DIR%\adb shell am start -D -n dascom.telecom.vipclub/dascom.telecom.vipclub.InitActivity
rem %ADB_DIR%\adb shell am start -D -n zj.zfenlly.tools/zj.zfenlly.main.MainActivity
call test.bat
'''