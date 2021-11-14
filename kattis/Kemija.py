nam=list(input())

vowels=['a','e','i','o','u']
fans=[]
i=0
while(True):
    if i==len(nam):
       break
    if nam[i] in vowels:
        fans.append(nam[i])
        i+=2
    else:
        fans.append(nam[i])
    i+=1
print(''.join(fans))



