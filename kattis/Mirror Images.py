num=int(input())
for pp in range(num):
    s=""
    r,c=list(map(int,input().split()))
    for j in range(r):
        name=input()
        s+=name
    s=[char for char in s]
    s.reverse()
    mirr=[]
    count=0
    for i in range(r):
        a=[]
        for j in range(c):      
            a.append(s[count])
            count+=1
        mirr.append(a)
    print(f"Test {pp+1}")
    for x in range(r):
        for y in range(c):
            print(mirr[x][y], end = "")
        print()
    mirr.clear()
    a.clear()
        
    
            
