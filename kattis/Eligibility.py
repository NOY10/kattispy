num=int(input())
for i in range(num):
    nam=list(input().split())
    pss=nam[1].split('/')
    sb=nam[2].split('/')
    if int(pss[0])>=2010:
        e=1
    elif int(sb[0])>=1991:
        e=1
    elif  int(nam[3])>40:
        e=0
    else:
        e=2
    if e==1:
        print(f"{nam[0]} eligible")
    elif e==0:
         print(f"{nam[0]} ineligible")
    else:
        print(f"{nam[0]} coach petitions")