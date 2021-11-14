num=int(input())
x=[]
y=[]
fans=[]
for i in range(num):
    x1,y1=list(map(int,input().split()))
    x.append(x1)
    y.append(y1)
for i in range(num-1):
    ax=x[i+1]-x[i]
    ay=y[i+1]-y[i]
    fans.append(ay//ax)
print(max(fans))