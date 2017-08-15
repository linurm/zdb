import os
import sys

########################################################

CONST_7085 = [
              '70', '85', '7B', 'D3', '82', 'EC', 'FA', '20', 'EE', '4E', '2C', 'F7', '86', 'B6', '0D', '25',
              '3F', '52', '44', '97', 'BD', 'BE', 'BE', 'B7', '53', 'F0', '92', '40', 'D5', '46', '9F', '65',
              '67', '89', '09', '94', 'DA', '37', 'B7', '23', '89', 'C7', '25', '63', '5C', '81', 'BA', '06',
              '6F', '7D', '66', 'DE', 'B5', '4A', 'D1', 'FD', '3C', '8D', 'F4', '9E', '60', '0C', '4E', '98',
              '99', '52', '20', '0E', '2C', '18', 'F1', 'F3', '10', '95', '05', '6D', '70', '99', '4B', 'F5',
              '67', 'E1', 'C6', '5F', '4B', 'F9', '37', 'AC', '5B', '6C', '32', 'C1', '2B', 'F5', '79', '34',
              'A1', '57', 'DE', 'AE', 'EA', 'AE', 'E9', '02', 'B1', 'C2', 'DB', 'C3', '9A', '37', 'A2', 'F7',
              '7B', '6D', 'B6', '16', '91', 'C3', '5F', '14', '20', '01', '84', 'D7', 'BA', '36', '26', '20',
              'FE', '9A', '01', 'E2', '6F', '59', '5E', 'F6', '4F', '58', 'DA', '21', 'F5', '6E', 'FC', '01',
              '7A', '2A', '7D', '04', '15', '73', '23', 'F2', '5A', '2B', 'F9', 'D3', 'AF', '45', '05', 'D2',
              '22', '41', 'C8', '7D', '37', '32', 'EB', '8F', '6D', '19', '12', '5C', 'C2', '5C', '17', '8E',
              '88', 'EE', 'C1', 'BE', '63', '7C', '77', '7B', 'F2', '6B', '6F', 'C5', '30', '01', '67', '2B',
              'FE', 'D7', 'AB', '76', 'CA', '82', 'C9', '7D', 'FA', '59', '47', 'F0', 'AD', 'D4', 'A2', 'AF',
              '9C', 'A4', '72', 'C0', 'B7', 'FD', '93', '26', '36', '3F', 'F7', 'CC', '34', 'A5', 'E5', 'F1',
              '71', 'D8', '31', '15', '04', 'C7', '23', 'C3', '18', '96', '05', '9A', '07', '12', '80', 'E2',
              'EB', '27', 'B2', '75', '09', '83', '2C', '1A', '1B', '6E', '5A', 'A0', '52', '3B', 'D6', 'B3',
              '29', 'E3', '2F', '84', '53', 'D1', '00', 'ED', '20', 'FC', 'B1', '5B', '6A', 'CB', 'BE', '39']

############################################################
def re_fun_B700(array_in):
    length = len(array_in)
    array = [0] * length
    for i in range(0, length):
        #print i
        a = int(array_in[i], 16)
        array[i] = (a^(i+0x7e))
        #print array[i]
        array[i] = int2hex(array[i])
        #print array[i]
    return array
def fun_B700(array_in):
    length = len(array_in)
    array = [0] * length

    for i in range(0, length):
        #print i
        a = int(array_in[i], 16)
        array[i] = (a^(i+0x7e))&0xff
        #print array[i]
        array[i] = int2hex(array[i])
    return array
############################################################
def strip_0x(array_in):
    array_out = array_in
    if array_in.startswith('0x'):
        array_out = array_in[2:]
    array_out = array_out.upper()
    if len(array_out) == 1:
        array_out = '0' + array_out
    return array_out
############################################################
'''index1=['0','d','a','7','4','1','e','b','8','5','2','f','c','9','6','3']
def fun_BBF0_BD68(array_in):
    length = len(array_in)
    array = [0] * length
    for i in range(0, 4):
        for j in range(0, 4):
            a = int(array_in[i + j * 4], 16)
            array[int(index1[i + j * 4], 16)] = CONST_637C[a]
        #print array[i]
        #print ()
    return array'''
############################################################
def re_change2ascii(array_in):
    length = len(array_in)
    array=''

    for i in range(0, length):
        print (chr(int(array_in[i], 16))),
    print ''
    return array
############################################################
def change2ascii(array_in):
    length = len(array_in)
    array = [0] * length

    for i in range(0, length):
        a = hex(ord(array_in[i]))
        array[i] = strip_0x(a)
    return array
############################################################
CONST_637C=[
 '63', '7C', '77', '7B', 'F2', '6B', '6F', 'C5',
 '30', '01', '67', '2B', 'FE', 'D7', 'AB', '76',
 'CA', '82', 'C9', '7D', 'FA', '59', '47', 'F0',
 'AD', 'D4', 'A2', 'AF', '9C', 'A4', '72', 'C0',
 'B7', 'FD', '93', '26', '36', '3F', 'F7', 'CC',
 '34', 'A5', 'E5', 'F1', '71', 'D8', '31', '15',
 '04', 'C7', '23', 'C3', '18', '96', '05', '9A',
 '07', '12', '80', 'E2', 'EB', '27', 'B2', '75',
 '09', '83', '2C', '1A', '1B', '6E', '5A', 'A0',
 '52', '3B', 'D6', 'B3', '29', 'E3', '2F', '84',
 '53', 'D1', '00', 'ED', '20', 'FC', 'B1', '5B',
 '6A', 'CB', 'BE', '39', '4A', '4C', '58', 'CF',
 'D0', 'EF', 'AA', 'FB', '43', '4D', '33', '85',
 '45', 'F9', '02', '7F', '50', '3C', '9F', 'A8',
 '51', 'A3', '40', '8F', '92', '9D', '38', 'F5',
 'BC', 'B6', 'DA', '21', '10', 'FF', 'F3', 'D2',
 'CD', '0C', '13', 'EC', '5F', '97', '44', '17',
 'C4', 'A7', '7E', '3D', '64', '5D', '19', '73',

 '60', '81', '4F', 'DC', '22', '2A', '90', '88',
 '46', 'EE', 'B8', '14', 'DE', '5E', '0B', 'DB',
 'E0', '32', '3A', '0A', '49', '06', '24', '5C',
 'C2', 'D3', 'AC', '62', '91', '95', 'E4', '79',
 'E7', 'C8', '37', '6D', '8D', 'D5', '4E', 'A9',
 '6C', '56', 'F4', 'EA', '65', '7A', 'AE', '08',
 'BA', '78', '25', '2E', '1C', 'A6', 'B4', 'C6',
 'E8', 'DD', '74', '1F', '4B', 'BD', '8B', '8A',
 '70', '3E', 'B5', '66', '48', '03', 'F6', '0E',
 '61', '35', '57', 'B9', '86', 'C1', '1D', '9E',
 'E1', 'F8', '98', '11', '69', 'D9', '8E', '94',
 '9B', '1E', '87', 'E9', 'CE', '55', '28', 'DF',
 '8C', 'A1', '89', '0D', 'BF', 'E6', '42', '68',
 '41', '99', '2D', '0F', 'B0', '54', 'BB', '16']
############################################################
table_D85C =[
 'D8', '5C', '88', '65', '82', 'EC', 'FA', '20',
 'EE', '4E', '2C', 'F7', '86', 'B6', '0D', '25',
 '97', '8B', 'B7', '21', '15', '67', '4D', '01',
 'FB', '29', '61', 'F6', '7D', '9F', '6C', 'D3',
 '4E', 'DB', 'D1', 'DE', '5B', 'BC', '9C', 'DF',
 'A0', '95', 'FD', '29', 'DD', '0A', '91', 'FA',
 '2D', '5A', 'FC', '1F', '76', 'E6', '60', 'C0',
 'D6', '73', '9D', 'E9', '0B', '79', '0C', '13',
 '93', 'A4', '81', '34', 'E5', '42', 'E1', 'F4',
 '33', '31', '7C', '1D', '38', '48', '70', '0E',
 'D1', 'F5', '2A', '33', '34', 'B7', 'CB', 'C7',
 '07', '86', 'B7', 'DA', '3F', 'CE', 'C7', 'D4',
 '7A', '33', '62', '46', '4E', '84', 'A9', '81',
 '49', '02', '1E', '5B', '76', 'CC', 'D9', '8F',
 '71', '06', '11', '7E', '3F', '82', 'B8', 'FF',
 '76', '80', 'A6', 'A4', '00', '4C', '7F', '2B',
 'D8', 'D4', 'E0', '1D', 'E7', '56', '58', 'E2',
 '91', 'D6', 'FE', '46', '91', '9A', '81', '6D',
 '7B', 'D8', 'DC', '9C', '9C', '8E', '84', '7E',
 '0D', '58', '7A', '38', '9C', 'C2', 'FB', '55',
 '68', 'D7', '20', '42', 'F4', '59', 'A4', '3C',
 'F9', '01', 'DE', '04', '65', 'C3', '25', '51',
 'A8', 'BE', '99', 'BE', '63', '7C', '77', '7B',
 'F2', '6B', '6F', 'C5', '30', '01', '67', '2B',
 'FE', 'D7', 'AB', '76', 'CA', '82', 'C9', '7D',
 'FA', '59', '47', 'F0', 'AD', 'D4', 'A2', 'AF',
 '9C', 'A4', '72', 'C0', 'B7', 'FD', '93', '26',
 '36', '3F', 'F7', 'CC', '34', 'A5', 'E5', 'F1',
 '71', 'D8', '31', '15', '04', 'C7', '23', 'C3',
 '18', '96', '05', '9A', '07', '12', '80', 'E2',
 'EB', '27', 'B2', '75', '09', '83', '2C', '1A',
 '1B', '6E', '5A', 'A0', '52', '3B', 'D6', 'B3']
table_R10 = [
 '70', '85', '7B', 'D3', '82', 'EC', 'FA', '20',
 'EE', '4E', '2C', 'F7', '86', 'B6', '0D', '25'

]
'''def fun_B9F8_BBF0(array_in, j):
    array = [0] * 16
    for i in range(0, 16):
        array[i] = int2hex(int(array_in[i], 16) ^ int(table_D85C[i + (j * 16)%0x100], 16))

    return array'''
############################################################
'''def fun_BD6C(array_in):
    array = [0] * 16
    #print array_in[0:4]
    for i in range(0, 4):
        array[i*4:(i+1)*4] = fun_BD7C(array_in[i*4:(i+1)*4])
    #array[0:4] = fun_5D7C(array_in[0:4])
    #array[4:8] = fun_5D7C(array_in[4:8])
    #array[8:12] = fun_5D7C(array_in[8:12])
    #array[12:16] = fun_5D7C(array_in[12:16])

    return array
def fun_BD7C(array_in):
    array = [0] * 4

    a0 = int(array_in[0], 16)
    a1 = int(array_in[1], 16)
    a2 = int(array_in[2], 16)
    a3 = int(array_in[3], 16)

    b = a0 ^ a1 % 0x100
    if b > 127:
        d = 0x1B
    else:
        d = 0
    array[0] = a1 ^ a2 ^ a3 ^ d ^ ((a0 ^ a1) * 2) % 0x100


    d = a2 ^ a1 % 0x100
    if d > 127:
        f = 0x1B
    else:
        f = 0
    array[1] = a0 ^ a2 ^ a3 ^ f ^ ((a2 ^ a1) * 2) % 0x100

    d = a3 ^ a2 % 0x100
    if d > 127:
        g = 0x1B
    else:
        g = 0
    array[2] = a3 ^ a0 ^ a1 ^ g ^ ((a3 ^ a2) * 2) % 0x100

    b = a3 ^ a0 % 0x100
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
def fun_BD7C_y(array_in):
    array = [0] * 4

    a0 = int(array_in[0], 16)
    a1 = int(array_in[1], 16)
    a2 = int(array_in[2], 16)
    a3 = int(array_in[3], 16)

    b = a0 ^ a1 % 0x100
    if b > 127:
        d = 0x1B
    else:
        d = 0
    array[0] = a1 ^ a2 ^ a3 ^ d ^ (a0 ^ a1 * 2) % 0x100


    d = a2 ^ a1 % 0x100
    if d > 127:
        f = 0x1B
    else:
        f = 0
    array[1] = a0 ^ a2 ^ a3 ^ f ^ (a2 ^ a1 * 2) % 0x100

    d = a3 ^ a2 % 0x100
    if d > 127:
        g = 0x1B
    else:
        g = 0
    array[2] = a3 ^ a0 ^ a1 ^ g ^ (a3 ^ a2 * 2) % 0x100

    b = a3 ^ a0 % 0x100
    if b > 127:
        d = 0x1B
    else:
        d = 0
    array[3] = a0 ^ a1 ^ a2 ^ d ^ (a3 ^ a0 * 2) % 0x100

    array[0] = int2hex(array[0])
    array[1] = int2hex(array[1])
    array[2] = int2hex(array[2])
    array[3] = int2hex(array[3])
    return array
'''
    #for i in range(0, length):
############################################################
def int2hex(intv):
    return strip_0x(hex(int(intv)))
############################################################
def AND0xFF(t):
    c = int(t, 16) % 256
    a = strip_0x(hex(c))
    return a
def XOR(a0,a1):
    a = hex(int(a0,16)^int(a1,16))
    b = strip_0x(a)
    return b

############################################################
'''def fun_BE14_BF2C(array_in):
    array = [0] * 16
    for i in range(0, 16):
        array[i] = XOR(table_D85C[0xA0 + i], array_in[i])
    return array'''
############################################################
'''def fun_B7B0_BBF0(array_in):
    array = [0] * 16
    for i in range(0, 16):
        array[i] = XOR(table_D85C[i], array_in[i])
    return array'''
############################################################
'''def fun_BF2C_B7B0(array_in):
    array = [0] * 16
    t = ['10'] * 16
    for i in range(0, 16):
        array[i] = XOR(t[i], array_in[i])
        array[i] = XOR(array[i],table_D85C[i])

    return array'''
############################################################
def fun_CAE0_E2C0(array_in):
    length = len(array_in)
    array = [0] * length
    #t = ['10'] * 16
    for i in range(0, length):
        array[i] = int2hex((i + 0x21)^int(array_in[i], 16))

    return array
############################################################
def fun_E2C0_EF1C(array_in):
    length = len(array_in)
    array = [0] * length
    #t = ['10'] * 16
    for i in range(0, length):
        array[i] = int2hex((i + 0x40)^int(array_in[i], 16))

    return array
############################################################
def fun_17B7C_17E3C(array_in):
    length = len(array_in)
    array = [0] * length
    #t = ['10'] * 16
    for i in range(0, length):
        array[i] = int2hex((i + 0x23)^int(array_in[i], 16))

    return array
############################################################
def fun_17E3C_18028(array_in):
    length = len(array_in)
    array = [0] * length
    #t = ['10'] * 16
    for i in range(0, length):
        array[i] = XOR(array_in[i], CONST_7085[i])

    return array
############################################################
def re_fun_17E3C_18028(array_in):
    length = len(array_in)
    array = [0] * length
    #t = ['10'] * 16
    for i in range(0, length):
        array[i] = XOR(array_in[i], CONST_7085[i])

    return array
############################################################
'''index2=['0','d','a','7','4','1','e','b','8','5','2','f','c','9','6','3']
def fun_18028_184B0(array_in):
    array = [0] * 16
    for i in range(0, 16):
        array[int(index2[i], 16)] = CONST_637C[int(array_in[i], 16)]

    return array
'''
############################################################
def re_fun_184BC_18560(array_in):
    array = [0] * 16
    for i in range(0, 4):
        array[i * 4: (i + 1) * 4] = re_fun_184BC_1855C(array_in[i * 4: (i + 1) * 4])
    return array
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
                        #print '@@@@@@@@@@@@@@@@@@@@@@@'
                        #break_flag = 1
                    else:
                        continue

    array[0] = int2hex(array[0])
    array[1] = int2hex(array[1])
    array[2] = int2hex(array[2])
    array[3] = int2hex(array[3])
    return array
############################################################################
def fun_184BC_18560(array_in):
    array = [0] * 16
    #print array_in[0:4]
    for i in range(0, 4):
        array[i * 4: (i + 1) * 4] = fun_184BC_1855C(array_in[i * 4: (i + 1) * 4])
    return array
def fun_184BC_1855C(array_in):
    array = [0] * 4
    a0 = int(array_in[0], 16)
    a1 = int(array_in[1], 16)
    a2 = int(array_in[2], 16)
    a3 = int(array_in[3], 16)

    r0 = (a1 ^ a0) % 0x100
    if r0 > 127:
        r0 = 0x1B
    else:
        r0 = 0
    array[0] = (a1) ^ a2 ^ a3 ^ r0 ^ (((a1 ^ a0) * 2) % 0x100)

    r1 = (a1 ^ a2) % 0x100
    if r1 > 127:
        r1 = 0x1B
    else:
        r1 = 0
    array[1] = (a0) ^ a2 ^ a3 ^ r1 ^ (((a2 ^ a1) * 2) % 0x100)

    r2 = (a3 ^ a2) % 0x100
    if r2 >127:
        r2 = 0x1B
    else:
        r2 = 0
    array[2] = a3 ^ a1 ^ a0 ^ r2 ^ (((a3 ^ a2) * 2) % 0x100)

    r3 = (a3 ^ a0) % 0x100
    if r3 >127:
        r3 = 0x1B
    else:
        r3 = 0
    array[3] = a1 ^ a0 ^ a2 ^ r3 ^ (((a3 ^ a0) * 2) % 0x100)

    array[0] = int2hex(array[0])
    array[1] = int2hex(array[1])
    array[2] = int2hex(array[2])
    array[3] = int2hex(array[3])
    return array

############################################################
re_index3=['0','5','a','f','4','9','e','3',
           '8','d','2','7','c','1','6','b']
def re_fun_637C(array_in):
    array = [0] * 16
    for j in range(0, 16):
        for i in range(0, 256):
            if CONST_637C[i] == array_in[j]:
                array[int(re_index3[j],16)] = int2hex(i)

    return array
def re_fun_18148_1833C_for(array_in, j):
    array = [0] * 16

    array = fun_18148_1833C_for(array_in, j)

    return array
############################################################
def fun_18148_1833C_for(array_in, j):
    array = [0] * 16
    for i in range(0, 16):
        array[i] = XOR(array_in[i], CONST_7085[i+0x10*j])
    return array
'''def fun_18148_1833C(array_in, i):
    array = [0] * 16
    #for i in range(0, 16):

    array = fun_18148_1833C_for(array_in, i)


    print_hex(array)
    array = fun_637C(array)
    #print array
    return array'''

index3=['0','d','a','7','4','1','e','b',
        '8','5','2','f','c','9','6','3']

def fun_637C(array_in):
    array = [0] * 16
    for i in range(0, 16):
        array[int(index3[i], 16)] = CONST_637C[int(array_in[i], 16)]
        #print array[i]
        #print ()
    return array

############################################################
def fun_18568_1867C(array_in):
    array = [0] * 16
    for i in range(0, 16):
        array[i] = XOR(array_in[i], CONST_7085[i + 0xA0])
    return array
############################################################
def re_fun_18568_1867C(array_in):
    array = [0] * 16
    for i in range(0, 16):
        array[i] = XOR(array_in[i], CONST_7085[i + 0xA0])
    return array
############################################################
'''def re_fun_18568_1867C(array_in):
    array = [0] * 16
    for i in range(0, 16):
        array[i] = XOR(array_in[i], CONST_7085[i + 0xA0])
    return array'''
############################################################
def fun_17EAC_18144(array_in, xor_array):
    array = [0] * 16
    t = xor_array
    for i in range(0, 16):
        array[i] = XOR(t[i], array_in[i])
        array[i] = XOR(array[i], CONST_7085[i])
    return array
############################################################
def re_fun_17EAC_18144(array_in, xor_array):
    array = [0] * 16
    t = xor_array
    for i in range(0, 16):

        array[i] = XOR(array_in[i], CONST_7085[i])
        array[i] = XOR(t[i], array[i])
    return array
############################################################
def fun_19DE0_19ED4(array_in1,array_in2):
    array = [0] * 32
    for i in range(0, 16):
        array[i] = XOR(int2hex(i + 0x24), array_in1[i])
    for i in range(16, 32):
        array[i] = XOR(int2hex(i + 0x24), array_in2[i - 16])
    return array
############################################################
def re_fun_19DE0_19ED4(array_in):
    array = [0] * 32
    for i in range(0, 32):
        array[i] = XOR(int2hex(i + 0x24), array_in[i])
    return array
############################################################
def fun_1C110_1C29C(array_in):
    array = [0] * 32
    for i in range(0, 32):
        array[i] = XOR(int2hex(i + 0x25), array_in[i])
    return array
############################################################
def re_fun_1C110_1C29C(array_in):
    array = [0] * 32
    for i in range(0, 32):
        array[i] = XOR(int2hex(i + 0x25), array_in[i])
    return array
############################################################
def fun_8A4(array_in):
    array = [0] * 16
    for i in range(0, 16):
        array[i] =  XOR(array_in[i], table_D85C[i])
    return array
############################################################
COMPARE_STRING=['96', '08', '29', 'E6', '27', 'ED', '28', 'A9',
                'CF', '55', '71', 'F7', 'B9', '55', '01', '13',
                '32', 'E4', '0D', '4C', 'CF', 'C7', '89', '5D',
                '31', '7D', '44', '97', '23', '5C', '3F', '44']
COM_STRING_2=['CE','E9', 'BB', 'BB', '29', '6E', 'DD', '27',  '28', 'AB', '0E', '95', '1E', '19', '6F', 'F2',
'3F', '92', '8B', '3D', 'D2', '05', 'C5', '7B',  '31', 'DA', 'B3', 'C4', '0D', 'D9', '09', '51']
############################################################

def print_hex(array_in):
    print ' '.join(array_in)
if __name__=='__main__':
    ###############################################################
    '''in_data_pre = raw_input("input data (01 02 02 03 ... hex)")
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
    '''
    ###############################################################

    #in_data_pre='ttttttttttttttttt'
    in_data_pre='hell0, alibaba!!!'
    len_data = len(in_data_pre)
    #print len_data
    XOR_ARRAY = [strip_0x(hex(0x20 - len_data))]*(0x20 - len_data)
    #print XOR_ARRAY
    #in_data_pre='ffffffffffffffff'
    in_data = change2ascii(in_data_pre)
    print in_data

    in_array = in_data#.split(" ")
    #in_array = ['5F', '32', '16', '02', '71', '0C', '6D', '71', '68', '24', '39', '42', '51', '60', '1D', '50']
    #in_array=['68', '65', '6C', '6C', '30', '2C', '20', '61', '6C', '69', '62', '61', '62', '61', '21', '21']
    #in_array = in_data.split(" ")
    #len_array = len(in_array)
    #print in_array
    in_array1 = fun_B700(in_array)
    in_arrayA = in_array1
    print ' B700:  ^= (i + 0x7e)'
    print_hex(in_array1)

    #raw_input('')

    #in_array4 = fun_8A4(in_arrayA)
    #print ' :  ^= {D8 5C ...}'
    #print_hex(in_array4)

    ########################################################

    in_array2 = fun_CAE0_E2C0(in_arrayA)
    print ' CAE0:  ^= (i + 0x21)'
    print_hex(in_array2)

    in_array2 = fun_E2C0_EF1C(in_array2)
    print ' E2C0:  ^= (i + 0x40)'
    print_hex(in_array2)

    #fun_EF1C_17B7C()

    in_array2 = fun_17B7C_17E3C(in_array2)
    print ' 17B7C:  ^= (i + 0x23)'
    print_hex(in_array2)

    #raw_input()

    #in_array3 = fun_17E3C_18028(in_array2)
    #print ' 17E3C:  ^= {70 85 ...}'
    #print_hex(in_array3)
    
    sec_len = len_data - 0x10
    sec_data = []
    if sec_len > 0:
        sec_data = in_array2[0x10:len_data]
    sec_data = sec_data + XOR_ARRAY
    print sec_data

    for j in range(1, 11):
        print ' ++++++++++++++++++++',j

        in_array2 = fun_637C(in_array2)
        print ' [x] = 637C[i]'
        print_hex(in_array2)
        if j == 10:
            break

        in_array2 = fun_184BC_18560(in_array2)
        print ' xor function'
        print_hex(in_array2)


        in_array2 = fun_18148_1833C_for(in_array2, j)
        print ' ^= 7085[i + %d * 0x10]'%j
        print_hex(in_array2)
    #print_hex(in_array2)
    in_arrayff = fun_18568_1867C(in_array2)
    print ' 18568:  ^= 7085[i + 0xA0]'
    #print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'

    #in_arrayff = ['97', '0B', '28', 'E9', '26', 'EE', '29', 'AE', 'CE', '56', '70', 'E8', 'B8', '56', '00', '14']
    #in_arrayff = ['38', 'C0', '94', '48', '9C', '3F', '37', '0E', '42', '0E', '41', '4C', 'F3', 'B3', '15', 'B0']
    print_hex(in_arrayff)
    in_array2 = fun_17EAC_18144(in_arrayff, sec_data)
    print ' 17EAC:  ^= 0x10 ^ 7085[i]'
    #in_array2 = ['1A', '81', '5C', '35', 'AB', '0D', 'DC', '81', '2F', '17', '53', '10', '31', 'EF', '02', '3E']
    print_hex(in_array2)
    #raw_input('')
    for j in range(1, 11):
        print ' ++++++++++++++++++++',j

        in_array2 = fun_637C(in_array2)
        print ' [x] = 637C[i]'
        print_hex(in_array2)
        if j == 10:
            break

        in_array2 = fun_184BC_18560(in_array2)
        print ' xor function'
        print_hex(in_array2)


        in_array2 = fun_18148_1833C_for(in_array2, j)
        print ' ^= 7085[i + %d * 0x10]'%j
        print_hex(in_array2)
    #print_hex(in_array2)
    #in_array2 = ['11', 'A6', 'C4', '3E', 'F9', 'F6', '63', 'D5', '5D', '67', '57', 'B4', 'E0', '03', '29', 'CD']
    in_arrayss = fun_18568_1867C(in_array2)
    print ' 18568:  ^= 7085[i + 0xA0]'
    #in_arrayff = ['97', '0B', '28', 'E9', '26', 'EE', '29', 'AE', 'CE', '56', '70', 'E8', 'B8', '56', '00', '14']
    print_hex(in_arrayff + in_arrayss)
    #in_arrayss = ['33', 'E7', '0C', '43', 'CE', 'C4', '88', '5A', '30', '7E', '45', 'E8', '22', '5F', '3E', '43']
    #print_hex(in_arrayss)
    #print ' 1867C'

    in_array2 = fun_19DE0_19ED4(in_arrayff, in_arrayss)
    print ' 19DE0:  ^= (i + 0x24)'
    print_hex(in_array2)

    #print '1C110'
    in_array3 = fun_1C110_1C29C(in_array2)
    print ' 1C110:  ^= (i + 0x25)'
    print '----------------------------------------'
    print_hex(in_array3)
    #print '1C29C'
    print ' compare string'
    print_hex(COMPARE_STRING)
    print '----------------------------------------'
    #raw_input('')
    #in_array3 = re_fun_1C110_1C29C(in_array3)

    #in_array3 = re_fun_1C110_1C29C(COM_STRING_2)

    #
    #
    in_array3 = re_fun_1C110_1C29C(COMPARE_STRING)
    print ' 1C110:  ^= (i + 0x25)'
    print_hex(in_array3)
    in_array3 = re_fun_19DE0_19ED4(in_array3)
    print ' 19DE0:  ^= (i + 0x24)'
    print_hex(in_array3)
    first_data = in_array3[0:16]
    in_array2 = in_array3[16:32]
    #in_array2 = ['1A', '81', '5C', '35', 'AB', '0D', 'DC', '81', '2F', '17', '53', '10', '31', 'EF', '02', '3E']
    in_array3 = re_fun_18568_1867C(in_array2)
    print ' 18568:  ^= 7085[i + 0xA0]'
    print_hex(in_array3)

    #raw_input('')
    for j in range(9, -1, -1):

        in_array3 = re_fun_637C(in_array3)
        print ' [x] = 637C[i]'
        print_hex(in_array3)
        if j == 0:
            break

        in_array3 = re_fun_18148_1833C_for(in_array3, j)
        print ' ^= 7085[i + %d * 0x10]'%j
        print_hex(in_array3)

        in_array3 = re_fun_184BC_18560(in_array3)
        print ' xor function'
        print_hex(in_array3)

        print ' ------------------',j

    #print_hex(in_array3)
    in_array2 = re_fun_17EAC_18144(in_array3, first_data)
    print ' 17EAC:  ^= 0x10 ^ 7085[i]'
    print_hex(in_array2)
    
    sec_len = int(in_array2[len(in_array2) - 1], 16)
    if sec_len == 0:
        sec_len = 0
    else:
        sec_len = 0x10 - sec_len

    #raw_input('')
    sec_data = in_array2[0:sec_len]
    print sec_data
    print ' @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'

    in_array3 = re_fun_18568_1867C(first_data)
    print ' 18568:  ^= 7085[i + 0xA0]'
    print_hex(in_array3)

    for j in range(9, -1, -1):

        in_array3 = re_fun_637C(in_array3)
        print ' [x] = 637C[i]'
        print_hex(in_array3)
        if j == 0:
            break

        in_array3 = re_fun_18148_1833C_for(in_array3, j)
        print ' ^= 7085[i + %d * 0x10]'%j
        print_hex(in_array3)

        in_array3 = re_fun_184BC_18560(in_array3)
        print ' xor function'
        print_hex(in_array3)

        print ' ------------------',j
    #print_hex(in_array3)
    in_array3 = in_array3 + sec_data
    in_array3 = fun_17B7C_17E3C(in_array3)
    print ' 17B7C:  ^= (i + 0x23)'
    print_hex(in_array3)
    in_array3 = fun_E2C0_EF1C(in_array3)
    print ' E2C0:  ^= (i + 0x40)'
    print_hex(in_array3)
    in_array3 = fun_CAE0_E2C0(in_array3)
    print ' CAE0:  ^= (i + 0x21)'
    print_hex(in_array3)
    in_array3 = re_fun_B700(in_array3)
    print ' B700:  ^= (i + 0x7e)'
    print_hex(in_array3)
    print re_change2ascii(in_array3)
    #print_hex(in_array3)

    raw_input('')








