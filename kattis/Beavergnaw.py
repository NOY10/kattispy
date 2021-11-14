import math
while(True):
    D,V=list(map(int,input().split()))
    if D==0 and V==0:
        break
    ans=D**3-6*V/math.pi
    print(math.pow(ans,1/3))