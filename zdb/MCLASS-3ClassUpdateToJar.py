import os
#from device import *
import AGDBDir
import sys
import zipfile


####################################################################

if __name__=='__main__':
    addr = AGDBDir.AGDB().getAllDir()

    apktool_dir = "{}".format(addr['apktool_dir'])
    pkg_dir = "{}".format(addr['pkg_dir'])
    dex2jar_dir = "{}".format(addr['dex2jar_dir'])
    apk_name = "{}".format(addr['apk_name'])
    smali_dir = "{}".format(addr['smali_dir'])
    modefy_class_dirname = "{}".format(addr['modefy_class_dirname'])
    class_list_file = "{}".format(addr['class_list_file'])
    
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
    # delete class of jar
    cmd = '{}\\d2j-class-update-jar.bat {}\\{} -i {}\\{}-addclass.jar -f -o {}\\{}-updateclass.jar -p {}\\{}'.format(dex2jar_dir, pkg_path, class_list_file, pkg_path, apk_name, pkg_path, apk_name, pkg_path, modefy_class_dirname)
    #print '#######',cmd
        #cmd = '{}\\d2j-class-join-jar.bat {}\\addclass\\Utils.class -i {}\\{}.jar -f -p com.googlecode.dex2jar.tools.ZjUtils -o {}\\{}-addclass.jar'.format(dex2jar_dir, pkg_path, pkg_path, apk_name, pkg_path, apk_name)
        #print '#######',cmd
    os.system("{}".format(cmd))
    
    # classes add jar
    list_class = '{}\\{}'.format(pkg_path, class_list_file)
    file = open(list_class)
    
    class_dir = '{}\\{}'.format(pkg_path, modefy_class_dirname)
    
    out_file = '{}\{}-updateclass.jar'.format(pkg_path, apk_name)
    print '#######',out_file 
    #zf = zipfile.zipfile(out_file,'w')
    
    zf = zipfile.ZipFile(out_file, 'a')
    while 1:
        line = file.readline()
        if not line:
            break
        line = line[:-1]
        #print line
        index = line.rfind('/')
        pkg = line[0:index]#.replace('/','.')
        clz = line[index+1:]
        index = clz.find('.')
        name = clz[0:index]
        hz = clz[index+1:]
        classfile = pkg + os.sep + clz
        class_path = class_dir + os.sep + classfile
        #print "class: ",classfile
        if os.path.exists(class_path):
            if os.path.isfile(class_path):
                entry = pkg+os.sep+name+'.'+hz
                print entry
                zf.write(class_path, entry)
    zf.close()    
   
    raw_input('Pause')
'''
%ADB_DIR%\adb shell am start -D -n dascom.telecom.vipclub/dascom.telecom.vipclub.InitActivity
rem %ADB_DIR%\adb shell am start -D -n zj.zfenlly.tools/zj.zfenlly.main.MainActivity
call test.bat
'''
