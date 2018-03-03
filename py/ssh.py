import paramiko
import os

ipAddr = '192.168.1.16'
port = 22
username = 'root'
password = '123456'

# win:\\
# unix:/
localDir = "G:\\platform-tools\\add"
remoteDir = "/home/rk3288/9d/lollipop/kernel"


######################################################################
def SSHConnect():
    print 'ssh connect ......' + ipAddr + "[" + str(port) + "]"
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ipAddr, port, username, password, timeout=4)
    print "ssh connect OK"
    # stdin, stdout, stderr = client.exec_command('ls -l /home')
    # for std in stdout.readlines():
    # print std,
    return client


def SSHClose(client):
    client.close()


def openSftp(client):
    sftp = Sftp(client)
    return sftp


class Sftp():
    def __init__(self, client):
        print "Sftp init"
        self.client = client
        self.sftp = client.open_sftp()

    def Get(self, remote_name, local_name):
        self.sftp.get(remote_name, local_name)

    def Put(self, local_name, remote_name):
        self.sftp.put(local_name, remote_name)

    def exec_command(self, command):
        stdin, stdout, stderr = self.client.exec_command(command=command)
        result = stdout.read()
        return result


# sftp.mkdir('abc')

# sftp.put(r'c:\test.txt', test.txt)
class ConfigFile():
    def __init__(self, file):
        self.file = open(file, "r")

    def doFile(self, sftp):
        lines = self.file.readlines()
        for line in lines:
            l = line.strip('\r\n').strip('\n')
            files = l.split(' ')
            if files == '':
                # print '1'
                continue
            if files[0] == 'cmd':
                cmd = ' '.join(files[1:])
                print 'do command : ', cmd
                print sftp.exec_command(cmd)
            if files[0] == 'get':
                # print files.__len__()
                if files.__len__() == 3:
                    print 'get ...... ' + files[1], '  and  ', files[2],
                    sftp.Get(files[1], files[2])
                    print "                   OK"
                else:
                    print files[0], "param error"
            if files[0] == 'put':
                # print files.__len__()
                # print files
                if files.__len__() == 3:
                    print 'put ...... ' + files[1], '  and  ', files[2],
                    sftp.Put(files[1], files[2])
                    print "                   OK"
                else:
                    print files[0], "param error"

    def close(self):
        self.file.close()


#########################################################
if __name__ == '__main__':
    cl = SSHConnect()
    sftp = openSftp(cl)
    cf = ConfigFile("ftp.txt")
    cf.doFile(sftp)
    cf.close()
    SSHClose(cl)
    # os.system("cmd")
# os.system("reboot.bat")
