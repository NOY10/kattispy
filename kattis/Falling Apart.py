num=int(input())
numbers=list(map(int,input().split()))
numbers.sort()
numbers.reverse()
a=0
b=0
for i in range(num):
    if i%2==0:
        a+=numbers[i]
    else:
        b+=numbers[i]
print(f"{a} {b}")
