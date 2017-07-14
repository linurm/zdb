import paramiko
import os

ipAddr = '192.168.3.16'
port = 22
username = 'root'
password = '123456'

#win:\\
#unix:/
localDir = "G:\\platform-tools\\add"
remoteDir = "/home/rk3288/tmp"
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
def doShell(client):
    memCmd = 'cd /home/rk3288/9d/lollipop;./ztest'
    print memCmd,'    ...'
    stdin, stdout, stderr = client.exec_command(memCmd)
    memResult = stdout.read()
    if not memResult:
        memResult = stderr.read()
    print memResult
    
    if memResult.find('failed') != -1:
        print 'build error'
        memResult = stderr.read()
        print memResult
        return 1
    #if stdout.find('make failed to build some targets'):
        #return 1
    print 'build successfully'
    return 0
class Sftp():
    def __init__(self, sftp):
        print "Sftp init"
        self.sftp = sftp
    def Get(self, name):
        self.sftp.get(remoteDir + '/' + name, localDir + '\\' + name)
#sftp.mkdir('abc')

#sftp.put(r'c:\test.txt', test.txt)
class ConfigFile():
    def __init__(self, file):
        self.file = open(file, "r")
    def doFile(self, sftp):
        lines = self.file.readlines()  
        for line in lines:
            l = line.strip('\r\n')
            l = l.strip(' ')
            if l=='':
                #print '1'
                continue
            if l==' ':
                print '2'
                continue
            if l=='\n':
                print '3'
                continue
            print 'ssh get ('+ipAddr+')...... ' + l,
            sftp.Get(l)
            print "                   OK"
    def close(self):
        self.file.close()
    
#########################################################
if __name__=='__main__':
    #os.system("adbdevice.bat");
    while True:
        cl = SSHConnect()
        if doShell(cl) == 1:
            r = raw_input('error r(rebuild?) ')
            print r
            #raw_input('')
            if r == 'r':
                continue
            sys.exit()
        break
        
    #raw_input("wait")
    sftp = openSftp(cl)
    cf = ConfigFile("ftp51.txt")
    cf.doFile(sftp)
    cf.close()
    SSHClose(cl)
    #os.system("so.bat")
    #os.system("jar.bat")
    #os.system("test.bat")
    os.system("adbdevice.bat");
    os.system("apk.bat")
    os.system("so.bat")
    os.system("jar.bat")
    os.system("sleep3s.bat")
    os.system("sleep3s.bat")
    os.system("sleep3s.bat")
    os.system("adbdevice.bat");
    os.system("reboot.bat")
    
