import os
import sys


if __name__=='__main__':
    ###############################################################
    in_data_pre = raw_input("input data (01 02 02 03 ... hex)")
    #in_data_pre = "B3 2E 0E CE 0E C7 03 85 E2 7B 5E C7 88 67 32 27 07 D2 3A 74 F6 FD B2 61 0C 43 7B D7 62 1E 7C 00"
    pp = []
    dd = []
    for tt in in_data_pre.splitlines():
        tt = tt.rstrip('\n')
        tt = tt.split(' ')
        pp = pp + tt
        #print tt
    for i in range(len(pp)):
        if pp[i] == '':
            print i
        else:
            dd.append(pp[i])
    print dd
    #print in_data_pre.split(" ")
    raw_input('')
    