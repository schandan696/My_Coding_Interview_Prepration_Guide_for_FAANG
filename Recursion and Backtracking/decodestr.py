m = {"0":"", "1":"a", "2":"b","3":"c","4":"d","5":"e",
     "6":"f","7":"g","8":"h", "9":"i", "10":"j","11":"k",
     "12":"l","13":"m","14":"n","15":"o","16":"p", "17":"q",
     "18":"r","19":"s","20":"t","21":"u","22":"v","23":"w",
     "24":"x","25":"y","26":"z"}

def getCodes(string):
    length = len(string)
    l = []
    if length==0:
        return l
    if length==1:
        l.append(m[string])
        return l
    
    elif string in m:
        l.append(m[string])
        
    l1 = getCodes(string[1:])
    code0 = m[string[0]]
    for code in l1:
        l.append(code0 + code)
    if string[0:2] in m:
        code01 = m[string[0:2]]
        l2 = getCodes(string[2:])
        for code in l2:
            l.append(code01 + code)
    return l

print(getCodes('1123'))