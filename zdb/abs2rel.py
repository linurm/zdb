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
        print ("base addr : 0x" + l)
        break


def abs2rel(abs_addr):
    a = int(abs_addr, 16)
    b = a - base_addr_t
    c = hex(b)
    #print c
    return c
####################################################################

if __name__=='__main__':

    getBaseAddr()
    while True:
        abs_addr = raw_input("input the abstract address 0x")
        global base_addr_t
        rel_addr = abs2rel(abs_addr)
        print("the relative address is                    0x"+rel_addr)

    

