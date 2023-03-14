num = int(input())
arr= []
bff = []
Fname=[]
for i in range(num):
    arr.append(input().split()) 
for i in range(num):
    if (arr[i][2] not in bff):
        for j in range(num-1):
            if(arr[i][2] == arr[j+1][2]):
                if(int(arr[i][1]) < int(arr[j+1][1])):
                    arr[i][1] = arr[j+1][1] 
                    arr[i][0] = arr[j+1][0]    
        bff.append(arr[i][2])
        Fname.append(arr[i][0])

print(len(Fname))
Fname.sort()
for i in Fname:
    print(i)