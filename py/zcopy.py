#!/usr/bin/python2.7
import os
import re
import shutil
import tarfile


###########################################################
def TarDir(fname):
    t = tarfile.open(fname + ".tar.gz", "w:gz")
    for root, dirs, files in os.walk(fname):
        print root, files
        for file in files:
            fullpath = os.path.join(root, file)
            t.add(fullpath)
    t.close()
    print fname+' =====> ' + fname + ".tar.gz"

def MkDir(Dir):
    if look_this_function == 0:
        aDir = os.path.abspath(Dir)
        if os.path.isdir(aDir):
            ''
        else:
            print 'makedirs', aDir
            os.makedirs(aDir)
def RmDir(Dir):
    if look_this_function == 0:
        aDir = os.path.abspath(Dir)
        if os.path.isdir(aDir):
            print 'rmtree', aDir
            shutil.rmtree(aDir)
#copy sourceDir pattern targetDir ==> OutDir
def copyFiles(sourceDir, targetDir):
    aSourceDir = os.path.abspath(sourceDir)
    #print aSourceDir
    aTargetDir = os.path.abspath(targetDir)
    #print aTargetDir
    aOutDir = os.path.abspath(OutDir)
   
    #print aOutDir
    for root,dirs,files in os.walk(targetDir,False,None,False):
        for targetFile in files:
            #print ''

            r = root + os.path.sep + targetFile
            a = os.path.abspath(r)

            nPos = a.replace(aTargetDir, "." + os.path.sep, 1)
            #print nPos

            aSourceDirFile = os.path.abspath(aSourceDir + os.path.sep + nPos)

            aDstDirFile = os.path.abspath(aOutDir + os.path.sep + nPos)
            #print aDstDirFile

            if os.path.exists(aSourceDirFile):
                if os.path.exists(os.path.dirname(aDstDirFile)):
                    ''
                else:
                    MkDir(os.path.dirname(aDstDirFile))
                if look_this_function == 0:
                    shutil.copy2(aSourceDirFile, aDstDirFile)
                print aSourceDirFile +"   ==>   "+aDstDirFile

                
def copyFileToDir(sourceFile):

    aSourceDirFile = os.path.abspath(sourceFile)
    aDstDirFile = CurDirName + os.path.sep + OutDir + os.path.sep + sourceFile

    if os.path.exists(aSourceDirFile):
        if os.path.exists(os.path.dirname(aDstDirFile)):
            ''
        else:
            MkDir(os.path.dirname(aDstDirFile))
            #print 'mkdir'
        if os.path.isdir(aSourceDirFile):
            print aSourceDirFile + "   ===>   " + aDstDirFile
            if look_this_function == 0:
                shutil.copytree(aSourceDirFile, aDstDirFile)
        else:
            print aSourceDirFile + "   ==>   " + aDstDirFile
            if look_this_function == 0:
                shutil.copy2(aSourceDirFile, aDstDirFile)
        
    else:
        print '\033[1;31;40m'
        print aSourceDirFile + ' is not exists'
        print '\033[0m'

def copyFile2FromTxt(txtFile):
    f = open(txtFile, "r")
    
    while True:
        line = f.readline()
        if line:
            if line.find("Files") == 0:
                #print line.split(" ")[3]
                copyFileToDir(line.split(" ")[3])
        else:  
            break
    f.close()
def copyFileFromDiffTxt(txtFile):
    f = open(txtFile, "r")
    
    while True:
        line = f.readline()
        #print line.strip('\n')#.split(" ")[0]
        if line:
            if line.find("Files") == 0:
                #print line.split(" ")[1]
                copyFileToDir(line.split(" ")[1])
                copyFileToDir(line.split(" ")[3])
            else:
                if line.find("Only") == 0:
                    a = line.split(" ")[2].replace(":", os.path.sep, 1) + line.split(" ")[3]
                    #print a
                    b = a.strip('\r\n').strip('\n')
                    copyFileToDir(b)
        else:
            break
    f.close()

def getCfilesByOfilesToDir(cfilesdir, targetDir, outDir):
    #print cfilesdir
    for root, dirs, files in os.walk(cfilesdir, False, None, False):
        #print root,targetDir
        if targetDir in root:
            try:
                files = os.listdir(root)
            except:
                print "ValueError"
            #print root
            for f in files:
                # print f
                if (os.path.isfile(os.path.join(root, f)) == True):
                    # rf = root[root.rfind(dirname)+2:]
                    refile = root.lstrip(cfilesdir) + os.path.sep + f
                    # the file name is :  1test\1\1.c
                    #if look_this_function == 1:
                        #print refile
                    abfile = os.path.join(root, f)
                    #if look_this_function == 1:
                        #print abfile
                    # C:\Users\Administrator\Desktop\1test\1\1.c
                    tm = abfile[abfile.rfind('.'):]
                    #if look_this_function == 1:
                        #print tm
                    #print 'the file name is : ', abfile #,os.path.join(root,f)
                    if tm == '.o':
                        absfile = abfile[:abfile.rfind('.')] + '.c'
                        if os.path.exists(absfile):
                            #print 'ads :', absfile, 'is exist'
                            if look_this_function == 1:
                                print 'abs: ',absfile
                            # ads : C:\Users\Administrator\Desktop\1test\1\1.c is exist
                            tarlen = len(targetDir)
                            reltfile = absfile[absfile.find(targetDir) + tarlen + 1:]
                            if look_this_function == 1:
                                print ': ',reltfile                            
                            # rel:  1\1.c
                            copyTargetFileToDir(targetDir, reltfile, outDir)
                        #else:
                            #print '', absfile, 'is not exist'

def copyTargetFileToDir(targetDir, sourceFile, outDir):

    aSourceDirFile = CurDirName + os.path.sep + targetDir + os.path.sep + sourceFile
    aDstDirFile = CurDirName + os.path.sep + outDir + os.path.sep + sourceFile
    #print aSourceDirFile
    #print aDstDirFile
    if os.path.exists(aSourceDirFile):
        if os.path.exists(os.path.dirname(aDstDirFile)):
            ''
        else:
            MkDir(os.path.dirname(aDstDirFile))
            #print 'mkdir ', os.path.dirname(aDstDirFile)
        if os.path.isdir(aSourceDirFile):
            print '\033[1;31;40m'
            print aSourceDirFile + "  ===dir===>   " + aDstDirFile
            print '\033[0m' 
            if look_this_function == 0:
                shutil.copytree(aSourceDirFile, aDstDirFile)
        else:
            print '\033[1;31;40m'
            print aSourceDirFile + "   ==>   " + aDstDirFile
            print '\033[0m' 
            if look_this_function == 0:
                shutil.copy2(aSourceDirFile, aDstDirFile)
        
    else:
        print '\033[1;31;40m'
        print aSourceDirFile + ' is not exists'
        print '\033[0m' 

##################################################################
look_this_function = 0
#1: yes 0: no
OutDir = 'out'
TargetDir = 'nd/kernel'
#TargetDir = '1\\1test'
CurDirName = os.getcwd()
##################################################################
if __name__=='__main__':
    RmDir(OutDir)
    MkDir(OutDir) 
    #print __file__
    #del_dirs(dirname)
    #zRename(CurDirName)
    #copyFiles("pad", "test")
    #   test\frameworks\av\camera\Camera.cpp
    #copyFileToDir("test\\frameworks\\av\\camera\\Camera.cpp", "test", "out")
    #copyFileFromDiffTxt("2.txt")
    
    getCfilesByOfilesToDir(CurDirName+os.path.sep+TargetDir, TargetDir, OutDir)

    TarDir(OutDir)
    #copyFile2FromTxt("1.txt")
