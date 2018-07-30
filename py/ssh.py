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
        # print local_dir
        if local_dir.startswith('.\\'):
            local = local_dir
            # print 'local1:', local
            local_mask = '.'
        else:
            len = local_dir.split('\\').__len__()
            local = local_dir.split('\\')[len - 1]
            local_mask = local_dir.rfind('\\')
            local_mask = local_dir[:local_mask]
            # print local_mask
            # print 'local2:', local

        aaa = os.path.join(remote_dir, local).replace('\\', '/')
        # print '---:', aaa
        # print 'local_dir:', local_dir
        # /home/linurm/3288/9d/lollipop/./kernel0.
        self.__ismkdir__(aaa)
        # remote_dir = aaa
        try:
            for root, dirs, files in os.walk(local_dir):
                root2 = '.' + root.split(local_mask)[1]
                # root2 = root[root.rfind(local_mask):]
                # print 'root2:', root2
                for name in dirs:
                    # print 'root:', root
                    local_path = os.path.join(root2, name)
                    # a = local_path.replace('\\', '/')
                    # print '@@@local path', local_path
                    remote_path = os.path.join(remote_dir, local_path)
                    remote_path = remote_path.replace('\\', '/')
                    # print '@@@mkdir remote path', remote_path
                    self.__ismkdir__(remote_path)
                for file in files:
                    remote_path = os.path.join(remote_dir, root2)
                    # print remote_path, ' remote_path'
                    local_file = os.path.join(root2, file)
                    # print local_file, '-------local file-----------'
                    # print file
                    remote_file = os.path.join(remote_path, file).replace('\\', '/')
                    # print remote_file, '--------remote file----------'
                    try:
                        self.sftp.put(local_file, remote_file)
                    except Exception, e:
                        self.sftp.mkdir(os.path.split(remote_file)[0])
                        self.sftp.put(local_file, remote_file)

                    print "upload %s   =====>   %s" % (local_file, remote_file)

        except Exception, e:
            print e

    def __isdir__(self, path):
        return

    def download(self, local_dir, remote_dir, remote_path):
        print " d            ,", remote_dir + '/' + remote_path
        stattmp = self.sftp.stat(remote_dir + '/' + remote_path)
        if stat.S_IFMT(stattmp.st_mode) == stat.S_IFREG:

            local_file = local_dir + "\\" + remote_path.replace('./', '').replace('/', '\\')
            local_file_dir = local_file[:local_file.rfind('\\')]
            if os.path.isdir(local_file_dir) == False:
                if os.path.exists(local_file_dir) == False:
                    print "mkdirs ", local_file_dir
                    os.makedirs(local_file_dir)

            remote_file = remote_dir + '/' + remote_path
            print remote_file + " ======> " + local_file
            # dir
            # self.download(local_dir, remote_dir + "/" + f.)
            try:
                self.sftp.get(remote_file, local_file)
            except Exception as err:
                print(err)
            return
        else:
            files = self.sftp.listdir_attr(remote_dir + '/' + remote_path)

        # Todo
        # print files
        for f in files:
            if stat.S_IFMT(f.st_mode) == stat.S_IFDIR:
                # if f.startwith('d'):
                tmpdir = (local_dir + "\\" + remote_path + "\\" + f.filename).replace('/', '\\')
                if os.path.exists(tmpdir) == False:
                    print "mkdirs ", tmpdir
                    os.makedirs(tmpdir)
                self.download(local_dir, remote_dir, remote_path + "/" + f.filename)

                # print f.filename
            if stat.S_IFMT(f.st_mode) == stat.S_IFREG:
                local_file = local_dir + "\\" + remote_path.replace('./', '').replace('/', '\\')
                if os.path.isdir(local_file) == False:
                    if os.path.exists(local_file) == False:
                        print "mkdirs ", local_file
                        os.makedirs(local_file)

                remote_file = remote_dir + '/' + remote_path + "/" + f.filename
                print remote_file + " ======> " + local_file + "\\" + f.filename
                # dir
                # self.download(local_dir, remote_dir + "/" + f.)
                try:
                    self.sftp.get(remote_file, local_file + "/" + f.filename)
                except Exception as err:
                    print(err)


import ConfigParser


# sftp.mkdir('abc')
class cfgFile():
    def __init__(self, file):
        self.file = file
        self.config = ConfigParser.RawConfigParser()
        self.config.read(self.file)

    def getSectionOptionValue(self, section, option, def_value):
        try:
            return self.config.get(section, option)
        except ConfigParser.NoSectionError:
            self.config.add_section(section)
            self.config.set(section, option, def_value)
        except ConfigParser.NoOptionError:
            self.config.set(section, option, def_value)
        with open(self.file, 'wb') as configfile:
            self.config.write(configfile)
        return def_value

    def setSectionOptionValue(self, section, option, value):
        try:
            self.config.set(section, option, value)
        except ConfigParser.NoSectionError:
            self.config.add_section(section)
            self.config.set(section, option, value)
        except ConfigParser.NoOptionError:
            self.config.set(section, option, value)
        with open(self.file, 'wb') as configfile:
            self.config.write(configfile)


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
            if files[0] == 'putdir':
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

    try:
        cl = SSHConnect()
        sftp = openSftp(cl)
    except Exception as e:
        print e
        exit(-1)

    while True:

        # cf = ConfigFile("ftp.txt")
        # cf.doFile(sftp)
        # cf.close()

        cfg = cfgFile("conf.cfg")

        localdir = cfg.getSectionOptionValue("putdir", "localdir", "")
        remotedir = cfg.getSectionOptionValue("putdir", "remotedir", "")
        work = cfg.getSectionOptionValue("putdir", "work", "off")

        if work == "on" and localdir != "" and remotedir != "":
            print 'putdir ...... ' + localdir, '  --->  ', remotedir
            sftp.upload(localdir, remotedir)
            print " OK !!!"
        else:
            print "putdir param error"

        localdir = cfg.getSectionOptionValue("getdir", "localdir", "")
        remotedir = cfg.getSectionOptionValue("getdir", "remotedir", "")
        remotepath = cfg.getSectionOptionValue("getdir", "remotepath", "")
        work = cfg.getSectionOptionValue("getdir", "work", "off")

        remotefile = remotedir + "/" + remotepath
        if work == "on" and localdir != "" and remotefile != "":
            print 'getdir ...... ' + localdir, '  <----  ', remotedir, '/', remotepath
            sftp.download(localdir, remotedir, remotepath)
            print " OK !!!"
        else:
            print "getdir param error"

        print cfg.getSectionOptionValue("put", "localdir", "")
        print cfg.getSectionOptionValue("put", "remotedir", "")
        print cfg.getSectionOptionValue("get", "localdir", "")
        print cfg.getSectionOptionValue("get", "remotedir", "")
        print cfg.getSectionOptionValue("cmd", "num", "1")
        # exit(-1)
        print cfg.getSectionOptionValue("cmd", "cmd", "")

        cmdnum = cfg.getSectionOptionValue("cmd", "num", "1")
        for i in range(1,int(cmdnum)+1):
            cmd = cfg.getSectionOptionValue("cmd", "cmd"+str(i), "ls")
            print cmd
            if sftp.exec_command(cmd[1:-1]) != 0:
                break
        getnum = cfg.getSectionOptionValue("get", "num", "1")
        for i in range(1, int(getnum) + 1):
            localfile = cfg.getSectionOptionValue("get", "localfile" + str(i), "ls")
            remotefile = cfg.getSectionOptionValue("get", "remotefile" + str(i), "ls")
            print localfile
            print remotefile
            print 'get ...... ' + remotefile, '  ---->  ', localfile,
            sftp.Get(remotefile, localfile)
        input_value = 'q'  # raw_input('q:quit, other:continue')
        if input_value == 'q':
            break
        if input_value == 'Q':
            break

    SSHClose(cl)
    # os.system("cmd")
# os.system("reboot.bat")
