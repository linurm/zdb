import os

look_this_function = 1
#1: yes 0: no

del_dir_name = '1test'

del_file_name = '.so'

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
            print "delete ...", root
            
        if look_this_function == 0:
            try:
                os.removedirs(root)
            except:
                print "ValueError"
#for test
def del_dirs2(dir):
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
                    print 'delete  ',os.path.join(root,f)
					#os.remove(os.path.join(root,f))
            print "delete ...", root

            
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

if __name__=='__main__':
    dirname=os.getcwd()
    #print __file__
    del_dirs(dirname)
    del_files(dirname)
