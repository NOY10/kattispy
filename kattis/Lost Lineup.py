num=int(input())
emp=list(" "*(num-1))
space=list(map(int,input().split()))
for i in range(1,num):
    pp=space[i-1]
    emp[pp]=f"{i+1}"
print(f"{1} {' '.join(emp)}")
