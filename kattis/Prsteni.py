num=int(input())
arr=list(map(int,input().split()))
for i in range(num-1):
    j=2
    k=arr[0]
    while(j<=arr[0]):
        if k%j==0 and arr[i+1]%j==0 and j!=1:
            k=k//j
            arr[i+1]=arr[i+1]//j
            j-=1
        else:
            j+=1
        
    print(f"{k}/{arr[i+1]}")
