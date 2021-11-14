num=int(input())
for i in range(num):
    num1=int(input())
    arr=list(map(int,input().split()))
    x=set()
    for j in range(num1):
        if arr[j] in x:
            x.remove(arr[j])
        else:
            x.add(arr[j])
    print(f"Case #{i+1}: {x.pop()}")
