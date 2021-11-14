num=int(input())
for i in range(num):
    x,y=list(map(int,input().split()))
    s=0
    for t in range(0,y+1):
        s=s+t
    pro=y**2
    sum=pro+y
    print(f"{x} {s} {pro} {sum}")
    

