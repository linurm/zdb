def find_addr(addr):
    while True:
        addr = idc.PrevHead(addr)
        #addr = idc.PrevHead(addr)
        #print GetMnem(addr)
        #break
        if GetMnem(addr) == "MOV" and "R1" in GetOpnd(addr, 0):
            print "R1 at 0x%x" % addr
            print GetOperandValue(addr, 1)
            
        if 
            break


#find_addr(0x1d5d8)

for addr in XrefsTo(0x001D8D8, flags=0):
    #print hex(addr.frm)
    find_addr(addr.frm)