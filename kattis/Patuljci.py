def check(dif,hei):
    for i in range(len(hei)):
        j=i+1
        while(True):
            if j==len(hei):
                break
            sum=hei[i]+hei[j]
            if sum==dif:
                return hei[i],hei[j]
            j+=1
            
    return 0

hei=[]
s=0
for i in range(9):
    num=int(input())
    hei.append(num)
    s=s+num
dif=s-100
x,y=check(dif,hei)
swd=[]
for i in range(9):
    if x==hei[i] or y==hei[i]:
        continue
    swd.append(hei[i])
for j in swd:
    print(j)


