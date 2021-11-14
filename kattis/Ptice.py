A=['A','B','C','A','B','C']
B=['B','A','B','C']
G=['C','C','A','A','B','B']
name=['Adrian','Goran','Bruno']
def check(score,mi):
    for i in range(3):
        if score[i]==mi:
            score[i]=0
            return name[i]

num=int(input())
mul=input()
mul=[char for char in mul]
a,b,g,c=0,0,0,0
score=[]
for i in range(num):
    if mul[i]==A[c]:
        a+=1
    if mul[i]==G[c]:
        g+=1
    if c==5:
        c=-1
    c+=1
score.append(a)
score.append(g)
c=0
for i in range(num):
    if mul[i]==B[c]:
        b+=1
    if c==3:
        c=-1
    c+=1
score.append(b)
mi=max(score)
x=score.count(mi)
sort=[]
if x==3:
    print(mi)
    name.sort()
    for i in name:
        print(i)
else:
    print(mi)
    for i in range(x):
        sort.append(check(score,mi))
    sort.sort()
    for i in sort:
        print(i)
        
        



