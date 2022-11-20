digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def int2str(x, base):
    if x < 0:
        return "-" + int2str(-x, base)
    return ("" if x < base else int2str(x//base, base)) + digits[x % base]
    
    

print(int2str(45, 2))
