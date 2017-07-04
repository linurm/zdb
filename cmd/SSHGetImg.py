import paramiko
import os

ipAddr = '192.168.3.16'
port = 22
username = 'root'
password = '123456'

#win:\\
#unix:/
localDir = "E:\\WORK\\arm\\rk3288\\arm\\rk3288\\AndroidTool_Release_v2.35\\rockdev\\Image\\51\\"
remoteDir = "/home/rk3288/9d/lollipop/out/release/"
lDir = "C:\\Users\\Administrator\\Desktop\\out\\9d\\lollipop\\kernel\\arch\\arm\\boot\\dts\\"
rDir = "/home/rk3288/9d/lollipop/kernel/arch/arm/boot/dts/"

l1Dir = "C:\\Users\\Administrator\\Desktop\\drivers\\"

r1Dir = "/home/tmp2/"
######################################################################
def SSHConnect():
    print 'ssh connect ......' + ipAddr + "[" + str(port) + "]"
    client = paramiko.SSHClient() 
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
    client.connect(ipAddr, port, username, password, timeout=4) 
    print "ssh connect OK"
    #stdin, stdout, stderr = client.exec_command('ls -l /home') 
    #for std in stdout.readlines(): 
        #print std,
    return client
    
def SSHClose(client):
    client.close()
    
def openSftp(client):
    sftp = Sftp(client.open_sftp())
    return sftp

class Sftp():
    def __init__(self, sftp):
        print "Sftp init"
        self.sftp = sftp
    def GetRemoteFile(self, rdir, name, ldir):
        print 'ssh get ...... ' + rdir + name
        self.sftp.get(rdir + name, ldir + name)
        print ""+ ldir + name +"      OK"
    def PutLocalFile(self, ldir, name, rdir):
        print 'ssh put ...... ' + ldir + name
        self.sftp.put(ldir + name, rdir + name)
        print ""+ rdir + name +"      OK"
    #def PutLocalDirFiles(self, ldir, rdir):
        #print 'ssh put ...... ' + ldir
        #self.sftp.put(ldir, rdir)
        #print ""+ rdir +"      OK"
#sftp.mkdir('abc')


#########################################################
if __name__=='__main__':
    cl = SSHConnect()
    sftp = openSftp(cl)
    sftp.GetRemoteFile(remoteDir,'kernel.img',localDir)
    sftp.GetRemoteFile(remoteDir,'resource.img',localDir)
    #sftp.PutLocalFile(lDir, 'rk3288.dtsi', rDir)
    #sftp.PutLocalFile(l1Dir, 'clk.c', r1Dir)
    #sftp.PutLocalDirFiles(l1Dir, r1Dir)
    SSHClose(cl)
    #os.system("so.bat")
    #os.system("jar.bat")
    #os.system("test.bat")
    #os.system("apk.bat")
    #os.system("sleep3s.bat")
    #os.system("sleep3s.bat")
    #os.system("sleep3s.bat")
    #os.system("reboot.bat")
    
