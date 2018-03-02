# -*- coding: cp936 -*-
import os
import re


look_this_function = 1
#1: yes 0: no

#先删文件，再删目录
del_dir_name = 'Caches'

del_file_name = '.so'


CurDirName = os.getcwd()


def del_dirs(dir):
    for root,dirs,files in os.walk(dir,False,None,False):
        #print dirs
        if del_dir_name in root:
            try:
                files = os.listdir(root)
            except:
                print "ValueError"
            for f in files:
                #print f
                if (os.path.isfile(os.path.join(root,f))==True):
                    print 'the file name is : ',os.path.join(root,f)
                    if look_this_function == 0:
                        os.remove(os.path.join(root,f))
            
            
        if look_this_function == 0:
            try:
                os.removedirs(root)
				#print "delete ...", root
            except:
                print "ValueError"
#for test
def del_dirs2(dir):
    i=0
    for root,dirs,files in os.walk(dir,False,None,False):
        #print dirs
        print ""
        i=i+1
        print root, " ",i#, "root"#mulu dir
        #i=i+1
        #if del_dir_name in dirs:
        #for d in root:
        #for f in files:
            #i=i+1
            #print d, "dir", i#mulu name
            
            #try:
                #files = os.listdir(root)
            #except:
                #print "ValueError"
            #for f in files:
                #print f," ", i
                #i = i + 1#,"file"
                #if (os.path.isfile(os.path.join(root,f))==True):
                    #print ""
                    #print 'delete2  ',os.path.join(root,f)
					#os.remove(os.path.join(root,f))
            #print "delete ...", root
    print i
def zRename(dir):
    i=0
    for root,dirs,files in os.walk(dir,False,None,False):
        for f in files:
            p = re.compile(r'(.*?)_2v_31020$')
            m = p.match(f)
            if m:
                i=i+1
                n = f.split('_2v_31020')[0]
                #print f
                print f,"===>",n,"",i
                os.rename(os.path.join(root,f),os.path.join(root,n))

    print i
def del_files(dir1):
    for root,dirs,files in os.walk(dir1,False,None,False):
        try:
            files = os.listdir(root)
        except:
            print "ValueError"
        for f in files:
            
            #if f.endswith(".so"):
                #print f
            if del_file_name in f:
                #print del_file_name
                if (os.path.isfile(os.path.join(root,f))==True):
                    
                    if __file__ in os.path.join(root,f):
                        print os.path.join(root,f),'is not delete (local file)'
                    else:
                        print 'delete  ',os.path.join(root,f)
                        if look_this_function == 0:
                            os.remove(os.path.join(root,f))

#dir1: from dir
#dir2: para dir
def zExtractFiles(from_dir, p_dir, out_dir):
    for root,dirs,files in os.walk(p_dir,False,None,False):
        print root

        #文件夹
        #for d in dirs:
            #print "dir:" + d
        #文件
        for f in files:
            print "file:" + f

            
    #for root,dirs,files in os.walk(dir2,False,None,False):
        #for f in files:
            #print root+"\\"+f
    
if __name__=='__main__':
    
    #print __file__
    #del_dirs(dirname)
    zRename(CurDirName)
    #zExtractFiles(".\\n", ".\\r", ".\\out")
