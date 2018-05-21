from FBY import *

if __name__ == '__main__':
    apkname = ''
    if len(sys.argv) == 1:
        print '1'
    elif len(sys.argv) == 2:
        #apkname = sys.argv
        apkname = sys.argv[1]
    else:
        apkname = raw_input('input build apk dir: ')
    
    InstallApk(RebuildApk(apkname))