num=int(input())
x=[]
y=[]
ans=[]
for i in range(num):
    x1, y1=list(map(float,input().split()))
    x.append(x1)
    y.append(y1)
for i in range(num-1):
    ansx=x[i+1]-x[i]
    ansy=(y[i+1]+y[i])/2
    ans.append((ansx*ansy)/1000)
sum=0
for i in range(num-1):
    sum+=ans[i]
print(sum)


