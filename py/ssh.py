import paramiko
import os
import stat

ipAddr = '192.168.2.100'
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
        channel = stderr.channel
        status = channel.recv_exit_status()
        # print status

        if status == 0:
            result = stdout.read()
            print result
        else:
            result = stderr.read()
            print result
        return status

    def __get_all_files_in_remote_dir(self, sftp, remote_dir):
        all_files = list()

        if remote_dir[-1] == '/':
            remote_dir = remote_dir[0:-1]

        files = sftp.listdir_attr(remote_dir)
        for x in files:
            filename = remote_dir + '/' + x.filename
            if stat.S_ISDIR(x.st_mode):
                all_files.extend(self.__get_all_files_in_remote_dir(sftp, filename))
            else:
                all_files.append(filename)
        return all_files

    def __ismkdir__(self, path):
        try:
            self.sftp.stat(path)
        except Exception, e:
            print "mkdir path %s" % path
            self.sftp.mkdir(path)
            # print e, '2...........'+path+'.............'

    def upload(self, local_dir, remote_dir):
        self.__ismkdir__(remote_dir)

        aaa = os.path.join(remote_dir, local_dir).replace('\\', '/')
        # print aaa
        self.__ismkdir__(aaa)
        try:
            for root, dirs, files in os.walk(local_dir):
                for name in dirs:
                    local_path = os.path.join(root, name)

                    # a = local_path.replace('\\', '/')
                    # print a
                    remote_path = os.path.join(remote_dir, local_path)
                    remote_path = remote_path.replace('\\', '/')
                    # print remote_path
                    self.__ismkdir__(remote_path)
                for filespath in files:
                    local_file = os.path.join(root, filespath)
                    print local_file, '------------------'
                    a = local_file.replace('\\', '/')
                    remote_file = os.path.join(remote_dir, a).replace('\\', '/')
                    try:
                        self.sftp.put(local_file, remote_file)
                    except Exception, e:
                        self.sftp.mkdir(os.path.split(remote_file)[0])
                        self.sftp.put(local_file, remote_file)

                    print "upload %s to remote %s" % (local_file, remote_file)

        except Exception, e:
            print e

    def __isdir__(self, path):
        return

    def download(self, local_dir, remote_dir):
        files = self.sftp.listdir_attr(remote_dir)
        print remote_dir
        # Todo
        for f in files:
            print f
            '''try:
                self.sftp.get(os.path.join(remote_dir, f), os.path.join(local_dir, f))
            except Exception as err:
                print(err)'''


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
                continue
            if files[0] == 'cmd':
                cmd = ' '.join(files[1:])
                print 'do command : ', cmd
                # cmd = 'cd /home/work/vm/ascendmanager/zr ; pwd'
                if sftp.exec_command(cmd) != 0:
                    return
            if files[0] == 'get':
                # print files.__len__()
                if files.__len__() == 3:
                    print 'get ...... ' + files[1], '  ---->  ', files[2],
                    sftp.Get(files[1], files[2])
                    print " OK !!!"
                else:
                    print files[0], "param error"
            if files[0] == 'put':
                # print files.__len__()
                # print files
                if files.__len__() == 3:
                    print 'put ...... ' + files[1], '  --->  ', files[2],
                    sftp.Put(files[1], files[2])
                    print " OK !!!"
                else:
                    print files[0], "param error"
            if files[0] == 'getdir':
                # print files.__len__()
                if files.__len__() == 3:
                    print 'getdir ...... ' + files[1], '  <----  ', files[2]
                    sftp.download(files[1], files[2])
                    print " OK !!!"
                else:
                    print files[0], "param error"
            if files[0] == 'puts':
                # print files.__len__()
                # print files
                if files.__len__() == 3:
                    print 'putdir ...... ' + files[1], '  --->  ', files[2]
                    sftp.upload(files[1], files[2])
                    print " OK !!!"
                else:
                    print files[0], "param error"

    def close(self):
        self.file.close()


#########################################################
if __name__ == '__main__':
    cl = SSHConnect()
    sftp = openSftp(cl)
    while True:
        cf = ConfigFile("ftp.txt")
        cf.doFile(sftp)
        cf.close()
        input_value = raw_input('q:quit, other:continue')
        if input_value == 'q':
            break
        if input_value == 'Q':
            break

    SSHClose(cl)
    # os.system("cmd")
# os.system("reboot.bat")
