num=int(input())
check=[]
for i in range(num):
    q=input().split(" ")
    t=q[1].split("/")
    nume=int(t[0])
    deno=int(t[1])
    
    while(nume>1 or deno>1):
        if (nume>deno):
            nume-=deno
            check.append("R")
        else:
            deno-=nume
            check.append("L")
    check.reverse()
    y=1 
    for che in check:
        y*=2
        if che=="R":
            y+=1
    check.clear()
    print(i+1,y)
    
