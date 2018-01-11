
def isValidPsnStr(psn):
    size = len(psn)
    if size != 32:
        print("PSN码位数必须为32个字符" )
        return False
    elif psn.startswith('0000000300000000') is False:
        print("PSN码必须以000000030000000开头")
        return False
    return True
#main
DIY_PSN = '0000000300000000C38008119CB4E0C6'

if(isValidPsnStr(DIY_PSN)):
    #b = bytes().fromhex(DIY_PSN)
    #bs = bytearray(b)
    bs = bytearray().fromhex(DIY_PSN)
    _sum = 0
    for bt in bs:
        tmp = bt & 0xff
        _sum += tmp
    _sum = _sum >> 1
    _sum |= (0x8000)
    check = hex(_sum)
    if check.startswith('0x'):
        check = check[2:]

    print("PSN码为:%s\n校验码为:%s" % (DIY_PSN, check.upper()))



