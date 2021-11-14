num=int(input())
stop=[]
for i in range(num):
    stop.append(int(input()))
    s=0
    for j in range(stop[i]):
        s=(s+.5)*2
    print(s)

      