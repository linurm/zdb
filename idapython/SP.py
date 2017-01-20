def find_addr(addr):
    sp_value = GetOperandValue(addr, 1)
    print 'The SP value is 0x%x' % sp_value
    
    
    
    while True:
        addr = idc.PrevHead(addr)
        #addr = idc.PrevHead(addr)
        #print  GetOpnd(addr, 1)#GetMnem(addr)
        #break
        if GetMnem(addr) == "LDR" and "SP" in GetOpnd(addr, 1):
            print "at 0x%x" % addr
            print hex(GetOperandValue(addr, 1))
            break
        if GetOperandValue(addr, 1) == sp_value:# and GetMnem(addr) == "LDR":
            print "SP value at" % addr
            break
def displayCode(addr, sp_value):
    if GetOperandValue(addr, 1) == sp_value and "SP" in GetOpnd(addr, 1):
        global cur_addr
        if addr == cur_addr:
            print hex(addr),'        ',GetDisasm(addr),'==============='
        else:
            print hex(addr),'        ',GetDisasm(addr)#GetMnem(addr),GetOpnd(addr, 1)
        #print hex(addr)
        
global cur_addr                  
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
        while start < end :
            start = FindCode(start, SEARCH_DOWN|SEARCH_NEXT)
            displayCode(start, sp_value)
    else:
        Warning("no function found at 0x%x", addr)
    

#find_addr(0x1d5d8)

#for addr in XrefsTo(hex(here()), flags=0):
    #print hex(addr.frm)
a = hex(here())
print 'HERE ',a
addr = int(here())
getFunction(addr)
#find_addr(addr)

    
