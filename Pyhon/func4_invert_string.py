def invert(string):
    invertedstr = ''
    for i in range(len(string)-1,-1,-1):
        invertedstr += string[i]
       
    return invertedstr

print(invert('python'))
