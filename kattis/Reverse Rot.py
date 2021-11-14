def check(st,alpha):
    for a in range(len(alpha)):
        if st==alpha[a]:
            return a



alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','_','.']
ans=[]
while(True):
    rev=input().split(" ")
    if rev[0]=='0':
        break
    stri=[char for char in rev[1]]
    for i in range(len(stri)):
        alphano=check(stri[i],alpha)
        ans.append(alpha[(alphano+int(rev[0]))%28])
    ans.reverse()
    print("".join(ans))
    
    ans.clear()