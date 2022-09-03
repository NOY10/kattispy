nam = input()
num = 0
for i in nam:
    if 'a' == i:
        break
    num+=1
print(nam[num:len(nam)])

