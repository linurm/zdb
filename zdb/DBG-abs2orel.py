import os
from device import *
import AGDBDir
import sys
import utils

########################################################

def getBaseAddr():
    f = open('out\\libbaseaddr.txt')
    for i, l in enumerate(f, 1):
        a = int(l, 16)
        global base_addr_t
        base_addr_t = a
        break


def abs2orel(abs_addr, ida_file_deviation):
    global base_addr_t
    a = int(abs_addr, 16)
    b = a - base_addr_t + int(ida_file_deviation, 16)
    c = hex(b)
    #print c
    return c
####################################################################

if __name__=='__main__':
    addr = AGDBDir.AGDB().getAllDir()
    #dev = utils.getDevice(adb_path=addr['adb_dir']+"\\adb")
    #adb_v = utils.getVersion(dev)
    #dev.remount()



    #cwd = os.getcwd()
    #print ''
    #print ''
    #print '  source {}\out\gdbinit.txt'.format(cwd)
    #print ''
    #print ''

    
    
    #pkg = (addr['pkg_name'])
    #pid = utils.get_pids(dev, pkg)
    #print pid
    #cmd = ["/data/gdbserver",":23946","--attach","{}".format(pid[0])]
    #print (cmd)
    #dev.shell_popen(cmd)

    #utils.adbForward(dev)
    
    ida_file_deviation = addr['ida_file_deviation']
    #setPidLibBaseAddr(dev, pid[0], libname)
    getBaseAddr()
    #b2gdbbreak()
    while True:
        abs_addr = raw_input("input the abstract address 0x")
        global base_addr_t
        rel_addr = abs2orel(abs_addr, ida_file_deviation)
        print("the relative address is                    0x"+rel_addr)

    # change dir to start gdb cmd
    #os.chdir('{}'.format(addr['gdb_dir']))
    #gdb_cmd = ['gdb']
    #subprocess.check_call(gdb_cmd)
    
    

    #raw_input("")
    

