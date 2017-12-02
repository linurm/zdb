import os
from device import *
import AGDBDir
import sys
import utils
import subprocess
import re
from ADB import *
####################################################################

if __name__=='__main__':
    addr = AGDBDir.AGDB().getAllDir2()
    dev = utils.getDevice(adb_path=addr['adb_dir']+"\\adb")
    adb_v = utils.getVersion(dev)
    dev.remount()

    while True:
    
        am_cmd = ["am", "start"]
        am_cmd.append("-D")
        component_name = "{}/{}".format(addr['pkg_name'], addr['launch_name'])
        am_cmd.append(component_name)
        print ("Launching activity {}...".format(component_name))
        
        print am_cmd
        (rc, _, _) = dev.shell_nocheck(am_cmd)
        if rc != 0:
            utils.error("Failed to start {}".format(component_name))

        pkg = (addr['pkg_name'])
        pid = utils.get_pids(dev, pkg)
        #print 
        #print '{}'.format(addr['pkg_name'])
        print 'pid = {}'.format(pid)
        #pid = (utils.get_pids(dev, "dascom.telecom.vipclub"))
        #print 'pid = {}'.format(pid)
        #print str(pid)[1:-1]
        cmd = "python {}".format('DBG-jdb.py')
        adbForwardJdwp(dev, str(pid)[1:-1])
        
        '''p1 = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        ret = p1.stdout.read()'''
        #with open(os.devnull, 'wb') as devnull:
            #utils.split_lines
            #, stdout=devnull, stderr=devnull
        '''try:
            ret = (subprocess.check_call(cmd))
        except subprocess.CalledProcessError,c:
            print c.output, c.returncode
            if c.returncode == 4:
                continue
            else:
                break'''
        #ret = os.popen("python {}".format(cmd))
        
        '''print "-----------", ret
        if ret == 4:
            print 'ret code is ' + ret'''
            #break
        ret = raw_input('e exit')
        if ret == 'e':
            break
    
    print ("exit  ")
    #print p1
'''
%ADB_DIR%\adb shell am start -D -n dascom.telecom.vipclub/dascom.telecom.vipclub.InitActivity
rem %ADB_DIR%\adb shell am start -D -n zj.zfenlly.tools/zj.zfenlly.main.MainActivity
call test.bat
'''
