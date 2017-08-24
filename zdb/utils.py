import os
from device import *
from AGDBDir import AGDB
import sys
import subprocess
import time
########################################################
def split_lines(s):
    """Splits lines in a way that works even on Windows and old devices.

    Windows will see \r\n instead of \n, old devices do the same, old devices
    on Windows will see \r\r\n.
    """
    # rstrip is used here to workaround a difference between splineslines and
    # re.split:
    # >>> 'foo\n'.splitlines()
    # ['foo']
    # >>> re.split(r'\n', 'foo\n')
    # ['foo', '']
    return re.split(r'[\r\n]+', s.rstrip())
def error(msg):
    print("ERROR: {}".format(msg))
    raw_input("")
    sys.exit("ERROR: {}".format(msg))
    
def getDevice(serial=None, product=None, adb_path='adb'):
    device = None
    try:
        device = get_device(serial, product, adb_path)
        print device
    except (DeviceNotFoundError, NoUniqueDeviceError, RuntimeError):
            # Don't error out if we can't find a device.
        device = None
        print ("Could not find a unique connected device/emulator.")
    return device

def getVersion(device):
    adb_version = subprocess.check_output(device.adb_cmd + ["version"])
    return adb_version
   
def get_processes(device):
    """Return a dict from process name to list of running PIDs on the device."""

    # Some custom ROMs use busybox instead of toolbox for ps. Without -w,
    # busybox truncates the output, and very long package names like
    # com.exampleisverylongtoolongbyfar.plasma exceed the limit.
    #
    # Perform the check for this on the device to avoid an adb roundtrip
    # Some devices might not have readlink or which, so we need to handle
    # this as well.
    #
    # Gracefully handle [ or readlink being missing by always using `ps` if
    # readlink is missing. (API 18 has [, but not readlink).

    ps_script = """
        if $(ls /system/bin/readlink >/dev/null 2>&1); then
          if [ $(readlink /system/bin/ps) == "toolbox" ]; then
            ps;
          else
            ps -w;
          fi
        else
          ps;
        fi
    """
    ps_script = " ".join([line.strip() for line in ps_script.splitlines()])

    output, _ = device.shell([ps_script])

    return parse_ps_output(output)

def parse_ps_output(output):
    processes = dict()
    
    output = split_lines(output.replace("\r", ""))
    #print (output)

    columns = output.pop(0).split()
    #print (output.pop(0))
    #print columns
    try:
        pid_column = columns.index("PID")
    except ValueError:
        pid_column = 1
    while output:
        columns = output.pop().split()
        process_name = columns[-1]
        #print process_name
        pid = int(columns[pid_column])
        #print pid,process_name
        if process_name in processes:
            processes[process_name].append(pid)
        else:
            processes[process_name] = [pid]

    return processes


def get_pids(device, process_name):
    processes = get_processes(device)
    print "get_pids ",process_name
    return processes.get(process_name, [])

def adbForward(device):
    port = "23946"
    str = "tcp:{}".format(port)
    print ("adb forward {}".format(str))
    device.forward(str, str)
    
def jdb_connect(jdb_port):
    jdb_cmd = ["jdb", "-connect",
               "com.sun.jdi.SocketAttach:hostname=localhost,port={}".format(jdb_port)]
    windows = sys.platform.startswith("win")
    flags = subprocess.CREATE_NEW_PROCESS_GROUP if windows else 0
    jdb = subprocess.Popen(jdb_cmd,
                           stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT,
                           creationflags=flags)
    jdb.stdin.write("exit\n")
    jdb.wait()
    print ("JDB finished unblocking application.")
    
def getDeviceLoop(serial=None, product=None, adb_path='adb'):
    while(True):
        dev = getDevice(adb_path='adb')
        if dev == None:
            time.sleep(3)
        else:
            return dev
    
def mkdir(path):    
    cmd = path
    if os.path.isdir(cmd):
        print cmd
    else:
        os.makedirs(cmd)
        print 'mkdir {}'.format(cmd)