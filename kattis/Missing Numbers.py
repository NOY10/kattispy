num=int(input())
y=[]
for i in range(num):
    y.append(int(input()))
t=0
c=0
for j in range(1,y[-1]+1):
    if y[t]==j:
        t+=1
    else:
        c+=1
        print(j)
if c==0:
    print("good job")
