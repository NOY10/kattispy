p,d=list(map(int,input().split()))
arr=[]
x=set()
y=0
wa=0
wb=0
tot=0
for i in range(p):
    arr.append(input())
    x.add(arr[i][0:1])
for i in range(len(x)):
    a,b=0,0
    flag=False
    r=arr[i].split(" ")
    r = [int(i) for i in r]
    a=r[1]
    b=r[2]
    for j in range(i,p-1):
        if arr[i][0:1]==arr[j+1][0:1]:
            flag=True
            t=arr[j+1].split(" ")
            t = [int(j) for j in t]
            a=t[1]+a
            b=t[2]+b
            arr[j+1]='0'
    
    if arr[i][0:1]!='0' or flag:
        tot=tot+a+b
        if a<b:
            lv=((a+b)//2)+1
            ans=b-lv
            wa=wa+ans
            wb=wb+a
            print(f"B {a} {ans}")
        else:
            lv=((a+b)//2)+1
            ans=a-lv
            wb=wb+ans
            wa=wa+b
            print(f"A {ans} {b}")
q=wa-wb
if q<0:
    q=q*-1
ans=q/tot
print(ans)
        

        
    
            