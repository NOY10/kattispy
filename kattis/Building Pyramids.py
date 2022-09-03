num = int(input())
sum = 0
i = 1
c=0
while(num>sum):
    sum = sum + pow(i,2)
    if (num>=sum):
        i+=2
        c+=1
        
print(c)