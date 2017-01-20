import os
import sys
#############################################################

def strip_0x(array_in):
    array_out = array_in
    if array_in.startswith('0x'):
        array_out = array_in[2:]
    array_out = array_out.upper()
    if len(array_out) == 1:
        array_out = '0' + array_out
    return array_out
############################################################
def int2hex(intv):
    return strip_0x(hex(int(intv)))
############################################################
def re_fun_184BC_1855C(array_in):
    array = [0] * 4
    b0 = int(array_in[0], 16)
    b1 = int(array_in[1], 16)
    b2 = int(array_in[2], 16)
    b3 = int(array_in[3], 16)

    A = b1 ^ b2 ^ b3 ^ b0
    
    break_flag = 0
    
    for a0 in range(0, 256):
        if break_flag == 1:
            break
        for a1 in range(0, 256):
            if break_flag == 1:
                break
            if a0 ^ a1 > 127:
                r0 = 0x1b
            else:
                r0 = 0
            if b0 == A ^ a0 ^ r0 ^ (((a0 ^ a1) * 2)%0x100):
                r0 = r0#print int2hex(a0),int2hex(a1)
            else:
                continue
            for a2 in range(0, 256):
                if break_flag == 1:
                    break
                if a2 ^ a1 > 127:
                    r1 = 0x1b
                else:
                    r1 = 0
                if b1 == A ^ a1 ^ r1 ^ (((a2 ^ a1) * 2)%0x100):
                    r1 = r1#print int2hex(a0),int2hex(a1)
                else:
                    continue
                for a3 in range(0, 256):
                    if break_flag == 1:
                        break
                    if a2 ^ a3 > 127:
                        r2 = 0x1b
                    else:
                        r2 = 0
                    if b2 == A ^ a2 ^ r2 ^ (((a2 ^ a3) * 2)%0x100):
                        r2 = r2#print int2hex(a0),int2hex(a1)
                    else:
                        continue
                    if a0 ^ a3 > 127:
                        r3 = 0x1b
                    else:
                        r3 = 0
                    if b3 == A ^ a3 ^ r3 ^ (((a0 ^ a3) * 2)%0x100):
                        array[0]=(a0)
                        array[1]=(a1)
                        array[2]=(a2)
                        array[3]=(a3)
                        break_flag = 1
                    else:
                        continue

    array[0] = int2hex(array[0])
    array[1] = int2hex(array[1])
    array[2] = int2hex(array[2])
    array[3] = int2hex(array[3])
    return array
    
def fun_184BC_1855C(array_in):
    array = [0] * 4
    a0 = int(array_in[0],16)
    a1 = int(array_in[1], 16)
    a2 = int(array_in[2], 16)
    a3 = int(array_in[3], 16)

    r0 = (a1 ^ a0) % 0x100
    if r0 > 127:
        r0 = 0x1B
    else:
        r0 = 0
    array[0] = (a1 ^ a2 ^ a3 ^ r0 ^ ((a1 ^ a0) * 2)) % 0x100
    
    r1 = (a2 ^ a1) % 0x100
    if r1 > 127:
        r1 = 0x1B
    else:
        r1 = 0
    array[1] = (a0 ^ a2 ^ a3 ^ r1 ^ ((a2 ^ a1) * 2)) % 0x100
    
    r2 = (a3 ^ a2) % 0x100
    if r2 >127:
        r2 = 0x1B
    else:
        r2 = 0
    array[2] = (a3 ^ a1 ^ a0 ^ r2 ^ ((a3 ^ a2) * 2)) % 0x100

    r3 = (a3 ^ a0) % 0x100
    if r3 >127:
        r3 = 0x1B
    else:
        r3 = 0
    array[3] = (r3 ^ a1 ^ a0 ^ a2 ^ ((a3 ^ a0) * 2)) % 0x100

    array[0] = int2hex(array[0])
    array[1] = int2hex(array[1])
    array[2] = int2hex(array[2])
    array[3] = int2hex(array[3])
    return array
def fun_184BC_1855C_t(array_in):
    array = [0] * 4

    a0 = int(array_in[0], 16)
    a1 = int(array_in[1], 16)
    a2 = int(array_in[2], 16)
    a3 = int(array_in[3], 16)

    b = (a0 ^ a1) % 0x100
    if b > 127:
        d = 0x1B
    else:
        d = 0
    array[0] = a1 ^ a2 ^ a3 ^ d ^ ((a0 ^ a1) * 2) % 0x100

    d = (a2 ^ a1) % 0x100
    if d > 127:
        f = 0x1B
    else:
        f = 0
    array[1] = a0 ^ a2 ^ a3 ^ f ^ ((a2 ^ a1) * 2) % 0x100

    d = (a3 ^ a2) % 0x100
    if d > 127:
        g = 0x1B
    else:
        g = 0
    array[2] = a3 ^ a0 ^ a1 ^ g ^ ((a3 ^ a2) * 2) % 0x100

    b = (a3 ^ a0) % 0x100
    if b > 127:
        d = 0x1B
    else:
        d = 0
    array[3] = a0 ^ a1 ^ a2 ^ d ^ ((a3 ^ a0) * 2) % 0x100

    array[0] = int2hex(array[0])
    array[1] = int2hex(array[1])
    array[2] = int2hex(array[2])
    array[3] = int2hex(array[3])
    return array


FO=['67', 'CD', 'D6', 'EE', 'C7', 'CC', 'E7', '42',
    'C2', '5D', '26', '20', 'C0', '8A', '72', '90']
    
CS=['BA', '69', '34', '75', '7F', '34', '18', 'FD',
    '7E', '32', 'B3', '66', 'FC', 'C9', '05', '98']
############################################################
if __name__=='__main__':
    ###############################################################
    print FO
    array = fun_184BC_1855C(FO)
    print array
    print cmp(array,CS[0:4])
    array = fun_184BC_1855C(FO[4:8])
    print array
    print cmp(array,CS[4:8])
    array = fun_184BC_1855C_t(FO[4:8])
    print array
    print cmp(array,CS[4:8])
    array = fun_184BC_1855C(FO[8:12])
    print array
    print cmp(array,CS[8:12])
    array = fun_184BC_1855C(FO[12:16])
    print array
    print cmp(array,CS[12:16])
    print CS
    print '**********************************'
    print re_fun_184BC_1855C(CS)
    
    print '**********************************'
    print int2hex(0xba^0x69^0x34^0x75)
    print int2hex(0xba^0x34)
    print int2hex(0x67^0xd6^((0x67^0xee)*2))
    raw_input('')

   







    
