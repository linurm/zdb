def find_addr(addr):
    #while True:
    addr = idc.PrevHead(addr)
        #addr = idc.PrevHead(addr)
        #print GetMnem(addr)
        #break
    if GetMnem(addr) == "LDR" and "R0" in GetOpnd(addr, 0):
        print "at 0x%x" % addr
        print GetDisasm(addr)# LDR R0,[R2,R6];off_950804
        print GetOpnd(addr, 0)# R0
        print GetOpnd(addr, 1)# [R2,R6]
        print GetOperandValue(addr, 0)# 0
        print GetOperandValue(addr, 1)# 2
        type = GetOpType(addr, 0)# 1
        print type
        type = GetOpType(addr, 1)# 1
        print type
        
        
        #if type == 3:
            
        return 0xffffffff
    return addr
        
            #break
def getFunction(addr):
    global cur_addr
    cur_addr = addr
    funs = GetFunctionAttr(addr, FUNCATTR_START)
    #print hex(funs)
    if (funs != -1):
        end = GetFunctionAttr(addr, FUNCATTR_END)
        print hex(funs),'---->',hex(end)
        start = funs
        sp_value = GetOperandValue(addr, 1)
        while addr > start and addr < end :
            addr = find_addr(addr)
            #displayCode(start, sp_value)
    else:
        Warning("no function found at 0x%x", addr)
    

#find_addr(0x6eaaa0)
#a = hex(here())
#print 'HERE ',a
addr = int(here())
#addr = 0x6eaaa0
getFunction(addr)