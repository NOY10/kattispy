num=int(input())
arr=[]
for i in range(num):
    arr.append(input().lower())
s=0
for j in range(num):
    if "pink" in arr[j] or "rose" in arr[j]:
        s+=1
if s==0:
    print("I must watch Star Wars with my daughter")
else:
    print(s)
