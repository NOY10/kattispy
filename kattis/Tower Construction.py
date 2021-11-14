num=int(input())
brick=list(map(int,input().split()))
s=0
for i in range(num-1):
    if brick[i]<brick[i+1]:
        s+=1
print(s+1)

