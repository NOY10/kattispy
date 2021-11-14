card=input()
arr=[]
leng=len(card)
div=leng//3
d=[]
falg=True

for i in range(0,len(card),3):
    arr.append(card[i:i+3])
for j in arr:
    c=arr.count(j)
    if c>=2:
        falg=False
    d.append(j[0:1])
p=d.count('P')
k=d.count('K')
h=d.count('H')   
t=d.count('T')
if not falg:
    print("GRESKA")
else:
    print(f"{13-p} {13-k} {13-h} {13-t}")
    
        
