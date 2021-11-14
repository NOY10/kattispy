R,C,Xr,Xc=list(map(int,input().split()))
matrix=[]
for i in range(R):
    s=""
    nam=list(input())
    for i in range(len(nam)):
        for j in range(Xc):
            s+=nam[i]

    for k in range(Xr):
        matrix.append(s)
for p in matrix:
    print(p)
           



