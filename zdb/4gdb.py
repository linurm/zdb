import os
from device import *
import AGDBDir
import sys
import utils

########################################################

################################################
####################################################################
def setPidLibBaseAddr(dev, pid, name):
    cat_script = """
    cat /proc/{}/maps | grep {} | grep xp
    """.format(pid,name)
    cat_script = " ".join([line.strip() for line in cat_script.splitlines()])
    #print cat_script
    output, _ = dev.shell([cat_script])
    #print output
    lba = output.split(" ")[0].split("-")[0]
    f = open('out\\libbaseaddr.txt','w')
    print "write {} to out\\libbaseaddr.txt".format(lba)
    f.write('{}\n'.format(lba))
    f.close()


def getLibMemAddr(dev, name):
    ps_script = """
    ps | grep {}
    """.format(name)
    ps_script = " ".join([line.strip() for line in ps_script.splitlines()])
    #print ps_script
    output, _ = dev.shell([ps_script])
    #print output

def getBaseAddr():
        f = open('out\\libbaseaddr.txt')
        for i, l in enumerate(f, 1):
                a = int(l, 16)
                global base_addr_t
                base_addr_t = a
                break

def b2gdbbreak():
        bp = open('in\\breakpoint')
        breaktxt = open('out\\gdbinit.txt','w')
        line_num = []
        breaktxt.write('target remote 127.0.0.1:23946\n')
        breaktxt.write('set step-mode on\n')
        breaktxt.write('set disassemble-next on\n')
        breaktxt.write('set arm fallback-mode auto\n')
        breaktxt.write('set arm force-mode auto\n')
        for i, l in enumerate(bp, 1):
                #print l
                global base_addr_t
                a = int(l, 16)
                b = a + base_addr_t
                #print a
                c = hex(b)
                print l.strip('\n') + ' + ' + hex(base_addr_t)+ ' = ' + c
                breaktxt.write('b *' + c + '\n')
                #t = l.split(':')
                #print t[2]#line number
                #line_num.append(int(t[2]))
        print " ===> gdbinit.txt    OK!!!"
        breaktxt.close()
        bp.close()
        return line_num#reverse()#.sort()#reverse=True)
####################################################################

if __name__=='__main__':
    addr = AGDBDir.AGDB().getAllDir()
    dev = utils.getDevice(adb_path=addr['adb_dir']+"\\adb")
    adb_v = utils.getVersion(dev)
    dev.remount()



    cwd = os.getcwd()
    print ''
    print ''
    print '  source {}\out\gdbinit.txt'.format(cwd)
    print ''
    print ''

    
    
    pkg = (addr['pkg_name'])
    pid = utils.get_pids(dev, pkg)
    print pid
    cmd = ["/data/gdbserver",":23946","--attach","{}".format(pid[0])]
    print (cmd)
    dev.shell_popen(cmd)

    utils.adbForward(dev)
    
    libname = addr['lib_name']
    setPidLibBaseAddr(dev, pid[0], libname)
    getBaseAddr()
    b2gdbbreak()

    # change dir to start gdb cmd
    os.chdir('{}'.format(addr['gdb_dir']))
    gdb_cmd = ['gdb']
    subprocess.check_call(gdb_cmd)
    
    

    #raw_input("")
    

