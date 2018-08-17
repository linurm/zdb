import binascii
import datetime
import os
import sys
import thread
import time

import matplotlib.patches as patches
import matplotlib.path as path
import matplotlib.pyplot as plt
import numpy as np
import serial
import serial.tools.list_ports
import time
import zcfg

def show_time(fn):
    print ('time_it is executed')
    def new_fn(*args):
        start = time.time()
        result = fn(*args)
        end = time.time()
        duration = end - start
        print('%s seconds are consumed in executing function: %s%r'\
              %(duration, fn.__name__, args))
        return result

    return new_fn

def ByteToHex(bins):
    return ' '.join([" %02X" % x for x in bins])


def HexToByte(hexStr):
    return bytes.fromhex(hexStr)


def uart_data_handle(port, baudrate):
    serial_handle(port, baudrate)
    thread.exit_thread()


def show_handle(name, ax, fig):
    global pre_left
    global pre_right
    global pre_bottom
    global pre_top
    global no_data
    global data
    global add_data
    global test_times
    global serial_run
    try:
        for i in range(test_times):
            while no_data:
                time.sleep(0.01)
            print 'next data ', i
            # plt.close()
            no_data = True

            data = np.concatenate((data, add_data), axis=0)
            # print data
            n, bins = np.histogram(data, 20)
            left = np.array(bins[:-1])
            right = np.array(bins[1:])
            bottom = np.zeros(len(left))
            top = bottom + n

            if ((pre_left == left).all()) and ((pre_right == right).all()) and ((pre_bottom == bottom).all()) and ((
                    pre_top == top).all()):
                top = top
            else:
                pre_left = left
                pre_right = right
                pre_bottom = bottom
                pre_top = top
                # we need a (numrects x numsides x 2) numpy array for the path helper
                # function to build a compound path
                # print ' add value'
                XY = np.array([[left, left, right, right], [bottom, top, top, bottom]]).T

                # get the Path object
                barpath = path.Path.make_compound_path_from_polys(XY)
                # make a patch out of it
                patch = patches.PathPatch(barpath)
                ax.cla()
                ax.add_patch(patch)
                # update the view limits
                ax.set_xlim(left[0], right[-1])
                ax.set_ylim(bottom.min(), top.max())
                ax.set_title('Voltage vs. times ' + str(test_times), color='0.3')
                plt.draw()
                # plt.show()

        # nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        # savefile = os.getcwd() + '\\' + nowTime + '.png'
        # print savefile
        #
        # fig.savefig('fig-.png')
        # fig.savefig('fig.png')
        # plt.savefig(savefile)
        serial_run = False
        plt.close()
        # fig.savefig('11.png')
        # plt.close()
    except:
        print "Error: unable to start 3"
    # exit(0)
    print 'thread exit'
    thread.exit_thread()


def recv(serial):
    poll = True
    while poll:
        try:
            data = serial.read(6)
            if data == '':
                continue
            else:
                poll = False
        except:
            poll = False
        # sleep(0.02)
    return data

@show_time
def select_serial_prot():
    plat = sys.platform.lower()
    print plat
    baudrate_code = [1200, 2400, 4800, 9600, 14400, 19200, 38400, 56000, 57600, 115200]

    cfg = zcfg.zcfgFile("serial.cfg")
    port = cfg.getSectionOptionValue("serial", "port", "")
    baudrate = cfg.getSectionOptionValue("serial", "baudrate", "")

    if (port != '' and baudrate != ''):
        flag = raw_input('Open ' + port + ' with baudrate ' + baudrate + ' ? (y/n): ')
        if (flag == 'y'):
            print 'y'
        else:
            # print 'n'
            port = ''
            baudrate = ''

    port_list = list(serial.tools.list_ports.comports())
    if len(port_list) == 0:
        print('can not find serial')
        return -1, -1;
    else:
        print len(port_list), ' serial coms have been found'
        found = False
        for i in range(0, len(port_list)):
            if port_list[i].device == port:
                found = True
        if found == False:
            print '' + port + ' have not been found'
            return -1, -1

    if (port == '' or baudrate == ''):

        for i in range(0, len(port_list)):
            print i, (port_list[i].device)
        num = raw_input('please input COM:  ')
        if int(num) >= len(port_list):
            return -1, -1
        port = port_list[int(num)].device
        cfg.setSectionOptionValue("serial", "port", port)
        print 'please input baudrate!'

        for i in range(len(baudrate_code)):
            print i, ": ", baudrate_code[i]
        num = raw_input(':  ')
        if int(num) >= len(baudrate_code):
            return -1, -1
        baudrate = str(baudrate_code[int(num)])
        cfg.setSectionOptionValue("serial", "baudrate", baudrate)
        print str(baudrate_code[int(num)])

    return port, baudrate


serial_run = True


def serial_handle(port, baudrate):
    global no_data
    global add_data
    global serial_run

    try:
        ser = serial.Serial(port, int(baudrate), timeout=0.5)
        if ser.isOpen():
            print("open success")
        else:
            print("open failed")
            serial_run = False
    except:
        print 'could not open port ', port
        serial_run = False
    while serial_run:
        data = recv(ser)
        if data != b'':
            # print("receive : ", data)
            ret = binascii.b2a_hex(data)
            for i in range(len(ret)):
                if i % 2 == 1:
                    print (ret[i - 1:i + 1]).upper(),
                    print '',
            print ''
            add_data = [int(binascii.b2a_hex(data[4]), 16) * 256 + int(binascii.b2a_hex(data[3]), 16)]
            no_data = False
    ser.close()
    return -1


add_data = []
no_data = True
data = []
test_times = 0
########################################
# plt.ion()
#########################################################
if __name__ == '__main__':
    port, baudrate = select_serial_prot()
    if port == -1 or baudrate == -1:
        exit(-1)
    test_times = int(raw_input('test times:  '))
    fig, ax = plt.subplots()

    # Fixing random state for reproducibility
    np.random.seed(80801)

    # histogram our data with numpy
    a = []
    data = np.array(a)
    n, bins = np.histogram(data, 20)
    # np.random.randn(1)
    pre_left = np.array(bins[:-1])
    pre_right = np.array(bins[1:])
    pre_bottom = np.zeros(len(pre_left))
    pre_top = pre_bottom + n

    try:
        thread.start_new_thread(uart_data_handle, (port, baudrate,))
    except:
        print "Error: unable to start uart_data_handle"
    # raw_input('')
    try:
        thread.start_new_thread(show_handle, ("show", ax, fig))
    except:
        print "Error: unable to start show_handle"

    # get the corners of the rectangles for the histogram
    left = np.array(bins[:-1])
    right = np.array(bins[1:])
    bottom = np.zeros(len(left))
    top = bottom + n

    # we need a (numrects x numsides x 2) numpy array for the path helper
    # function to build a compound path
    XY = np.array([[left, left, right, right], [bottom, top, top, bottom]]).T

    # get the Path object
    barpath = path.Path.make_compound_path_from_polys(XY)

    # make a patch out of it
    patch = patches.PathPatch(barpath)
    ax.cla()
    ax.add_patch(patch)

    # update the view limits
    ax.set_xlim(left[0], right[-1])
    ax.set_ylim(bottom.min(), top.max())
    ax.set_title('Voltage vs. time chart' + str(test_times), color='0.3')
    # ax.set_title(r'Histogram of Serial ' + str(test_times) + ' times : $\mu=100$, $\sigma=15$')
    fig.tight_layout()
    try:
        plt.show()
        nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        savefile = os.getcwd() + '\\' + nowTime + '.png'
        print savefile
        fig.savefig(savefile)
    except:
        print 'exit'
    exit(0)
    # plt.close()
    # plt.savefig(savefile)
    # plt.savefig('plt.png')
    # fig.savefig('G:\\ssh\\1.png')
