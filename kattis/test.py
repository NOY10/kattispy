s=0
i=0
y=0
y1=0
c=0
mar=[]
gra=[]
rw=[]
while(True):
    p=input()
    if p=="-1":
      break
    t=p.split(" ")
    mar.append(t[0])
    gra.append(t[1])
    rw.append(t[2])
    if rw[i]=="right":
        s=s+int(mar[i])
        y=gra.count(gra[i])-1
        if y!=0:
           y1=y1+y
        c+=1
    i+=1
print(f"{c} {s+(20*(y1))}")
