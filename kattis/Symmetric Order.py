def check(name,nameL,co):
    for i in range(len(name)):
        if nameL[i]==co:
            nameL[i]=26
            return name[i]
pp=0
while(True):
    num=int(input())
    name=[]
    nameL=[]
    setc=set()
    name.clear()
    nameL.clear()
    if  num==0:
        break
    sys=list(' '*num)
    for i in range(num):
        name.append(input())
        nameL.append(len(name[i]))
        setc.add(nameL[i])
    loop=len(setc)
    fir=0
    sec=num-1
    ly=0

    for p in range(loop):
        minv=min(nameL)
        coun=nameL.count(minv)
        if coun>1:
            coun=coun//2
            for i in range(coun):
                
                sys[fir]=check(name,nameL,minv)
                sys[sec]=check(name,nameL,minv)
                fir+=1
                sec-=1
        minv=min(nameL)
        coun=nameL.count(minv)
        if coun==1:
            if ly%2==0:
               sys[fir]=check(name,nameL,minv)
               fir+=1

            else:
               sys[sec]=check(name,nameL,minv)
               sec-=1
            ly+=1
    pp+=1
    print(f'SET {pp}') 
    for j in sys:
        print(j)





