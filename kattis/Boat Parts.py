parts, days=list(map(int,input().split()))
arr=[]
w=set()
for i in range(days):
    arr.append(input())
for j in range(days):
    w.add(arr[j])
    if len(w)==parts:
        print(j+1)
        break
if len(w)>parts or len(w)<parts and len(w)!=parts:
    print("paradox avoided")
    
        
    


