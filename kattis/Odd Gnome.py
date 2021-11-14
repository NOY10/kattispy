num=int(input())
for j in range(num):
    arr=list(map(int,input().split()))
    mem=arr[1]-1
    for i in range(arr[0]):
        if mem+1==arr[i+1]:
            mem+=1
        else:
            print(i+1)
            break
            