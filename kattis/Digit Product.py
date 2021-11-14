num=input()
while(len(num)>1):
    x=1
    for n in num:
        if n!="0":
            x*=int(n)
    num=str(x)
print(num)

