num=int(input())
a=[]
sum=0
for i in range(num):
    a.append(int(input()))
    if i==0:
        sum=sum+a[i]
    else:
       sum=sum+((4/5)**i)*a[i]
avg=0
for i in range(num):
    fg=0
    g=0
    temp=a[i]
    a.remove(a[i])
    g=g+a[0]
    for j in range(1,num-1):
       g=g+((4/5)**j)*a[j]
    fg=(fg+g)/5
    avg=avg+fg
    a.insert(i,temp)
print(f"{sum/5} {avg/num}")



