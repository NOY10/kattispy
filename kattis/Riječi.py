num=int(input())
a=0
b=1
for i in range(1,num):
    tempa=a
    a=b
    b=tempa+b
print(a,b)
