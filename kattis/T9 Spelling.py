dict={'a':('2',1),'b':('2',2),'c':('2',3),'d':('3',1),'e':('3',2),'f':('3',3),'g':('4',1),'h':('4',2),'i':('4',3),
'j':('5',1),'k':('5',2),'l':('5',3),'m':('6',1),'n':('6',2),'o':('6',3),'p':('7',1),'q':('7',2),'r':('7',3),'s':('7',4),
't':('8',1),'u':('8',2),'v':('8',3),'w':('9',1),'x':('9',2),'y':('9',3),'z':('9',4),' ':('0',1)}


num=int(input())
for i in range(num):
    lis=[]
    last=-1
    s=''
    nam=input()
    for j in nam:
        t=dict[j]
        if t[0]==last:
            lis.append(" ")
        lis.append(t[0]*t[1])
        last=t[0]
    s+=''.join(lis)
    print(f'Case #{i+1}: {s}')
