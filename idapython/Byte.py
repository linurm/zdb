#in_data_pre = "97 0B 28 E9 26 EE 29 AE CE 56 70 E8 B8 56 00 14 A2 D7 ED B2 62 F0 77 96 15 DF 4A 0C C7 0C 86 CA"
#in_data_pre = "7A 14 37 F6 39 F1 36 B1 D1 49 6F F7 A7 49 1F 0B"
in_data_pre = "68 65 6C 6C 30 2C 20 61 6C 69 62 61 62 61 21 21"
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

addr = int(here())
for i in range(len(pp)):
    PatchByte(addr+i, int(pp[i],16))
#print hex(PatchByte(here(),0x10))