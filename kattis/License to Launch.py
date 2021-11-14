num=int(input())
x=list(map(int,input().split()))
m=min(x)
for i in range(num):
    if x[i]==m:
        print(i)
        break