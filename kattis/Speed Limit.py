x=[]
y=[]
while(True):
    num=int(input())
    if num==-1:
        break
    for i in range(num):
        x1,y1=list(map(int,input().split()))
        x.append(x1)
        y.append(y1)
    s=0
    for j in range(num-1):
        t=y[j+1]-y[j]
        s=s+t*x[j+1]
    s=s+x[0]*y[0]
    del x[:num]
    del y[:num]
    print(f"{s} miles")

