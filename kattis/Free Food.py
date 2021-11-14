num=int(input())
s=set()
for i in range(num):
    x, y=list(map(int,input().split()))
    for j in range(x,y+1):
        s.add(j)
print(len(s))
