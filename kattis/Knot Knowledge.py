num = int(input())
n = list(map(int,input().split()))
n2 = list(map(int,input().split()))
for i in n:
    if i in n2:
        continue
    else:
        print(i)