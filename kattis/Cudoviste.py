rows, colunms=list(map(int, input().split()))
car0=0
car1=0
car2=0
car3=0
car4=0
arr=[]
for i in range(rows):
    arr.append(input())
for row in range(rows-1):
    for col in range(colunms-1):
        chars=arr[row][col:col+2]+arr[row+1][col:col+2]
        if "#" in chars:
            continue
        c=0
        for char in chars:
            if char=="X":
                c+=1
        if c==0:
            car0+=1
        elif c==1:
            car1+=1
        elif c==2:
            car2+=1
        elif c==3:
            car3+=1
        elif c==4:
            car4+=1
print(f"{car0}\n{car1}\n{car2}\n{car3}\n{car4}")

