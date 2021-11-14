blimp=[]
for i in range(5):
    blimp.append(input())
sum=""
for j in range(5):
    if "FBI" in blimp[j]:
        sum=sum+str(j+1)
        sum=sum+" "
if sum=="":
    print("HE GOT AWAY!")
else: 
    print(sum)
