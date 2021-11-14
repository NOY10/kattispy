arr=list(map(int,input().split()))
ans=[]
for i in range(2):
    ans.append(arr[i+1]-arr[i])
print(max(ans)-1)

