mess=input()
lent=int(len(mess)/2)
sumF=0
sumS=0
first=[char for char in mess[0:lent]]
second=[char for char in mess[lent:len(mess)]]
for i in range(lent):
    sumF=sumF+(ord(first[i])-65)
    sumS=sumS+(ord(second[i])-65)
newF=[]
newS=[]
encode=[]
for i in range(lent):
    newF.append(chr(65+((ord(first[i])-65)+sumF) % 26))
    newS.append(chr(65+((ord(second[i])-65)+sumS)%26))
    t1=ord(newS[i])-65
    encode.append(chr(65+((ord(newF[i])-65)+t1)%26))
print("".join(encode))