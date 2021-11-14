num=int(input())
ans=[]
for i in range(2,(num//2)+2):
    remainder = num%(2 * i -1)
    if(remainder == 0 or remainder - i == 0):
        ans.append(f'{i},{i-1}')
    remainder = num % i
    if(remainder == 0):
        ans.append(f'{i},{i}')
print(f"{num}:")         
for j in ans:
    print(j)
