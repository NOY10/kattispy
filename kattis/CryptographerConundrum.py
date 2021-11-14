nam=input("")
leng=len(nam)
sum=0
for i in range(0,leng,3):
 if nam[i:i+1]=="P":
   sum=sum+1
 if nam[i+1:i+2]=="E":
   sum+=1
 if nam[i+2:i+3]=="R":
   sum+=1
print(leng-sum)