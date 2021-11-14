Num=int(input())
for i in range(Num):
    num=list(input())
    num = [int(i) for i in num]
    num.reverse()
    ans=[]
    for j in range(len(num)):
        if j%2==0:
            ans.append(num[j])
        else:
            pro=num[j]*2
            if pro>9:
                proq=str(pro)
                x=list(proq)
                x= [int(i) for i in x]
                ans.append(sum(x))
            else:
                ans.append(pro)
    totsum=sum(ans)
    ans.clear()
    if totsum%10==0:
        print("PASS")
    else:
        print("FAIL")

