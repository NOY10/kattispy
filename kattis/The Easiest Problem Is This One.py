
while(True):
    num=input()
    if num=='0':
        break
    Nsum=list(map(int, num))
    Ns=sum(Nsum)
    i=11
    while(True):
        ans=int(num)*i
        y=[char for char in str(ans)]
        Ssum=list(map(int, y))
        Ss=sum(Ssum)
        if Ns==Ss:
            print(i)
            break
        i+=1
        


