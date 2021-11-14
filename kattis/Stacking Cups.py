def check(di):
    mi=min(di)
    for t in range(len(di)):
        if mi==di[t]:
            di[t]=1000
            return t
    
    

num=int(input())
colour=[]
di=[]
col=[]
for i in range(num):
    cup=list(map(str,input().split()))
    cint=[x for x in cup[0] if x.isdigit()]
    cint2=[x for x in cup if x.isdigit()]

    if cint==[]:
        colour.append(cup[0])
        di.append(int(cint2[0]))
    else:
        colour.append(cup[1])
        ans=int(cint2[0])/2
        di.append(ans)
for j in range(num):
    name=check(di)
    col.append(colour[name])
for p in col:
    print(p)



