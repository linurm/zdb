import os
import sys


  
for arg in sys.argv:  
    print arg  
  
raw_input() 


list_class = '{}\\classlist.txt'.format(pkg_path)
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
        pkg_name = pkg + '.' + name
        #print clz
    # modefy class
        cmd = '{}\\d2j-modefy-class.bat {}\\{}.jar -f -d -o {}\\{} -c {}.class'.format(dex2jar_dir, pkg_path, apk_name, pkg_path, clz, pkg_name)
    #print '########################'
        print '#######',cmd
        os.system("{}".format(cmd))
    