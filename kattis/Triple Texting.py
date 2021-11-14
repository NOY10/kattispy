nams=input()
div=len(nams)//3
nam=[]
for i in range(0,len(nams),div):
    nam.append(nams[i:i+div])
if nam[0]==nam[1]: 
    print(nam[0])
elif nam[0]==nam[2]:
    print(nam[0]) 
elif nam[1]==nam[2]:
    print(nam[1])


