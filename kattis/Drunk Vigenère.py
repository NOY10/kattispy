c=input()
c=[char for char in c]
k=input()
k=[char for char in k]
encode=[]
for i in range(len(k)):
    k1=ord(k[i])-65
    if i%2==0:
       encode.append(chr(65 + ((ord(c[i])-65) - k1) % 26))
    else:
       encode.append(chr(65 + ((ord(c[i])-65) + k1)) % 26)
print("".join(encode))
# encode.append(chr(ord('A') + ((ord(c[i])-ord('A')) + (ord(k[i])-ord('A'))) % 26))