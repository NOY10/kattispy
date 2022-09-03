nam = input()
sum=0
arr=[]
for i in nam:
    if i == '|':
        sum+=1
    elif i == ')':
        arr.append(sum)
        sum=0
arr.append(sum)

if (arr[0] -arr[1]) == 0:
    print('correct')
else:
    print('fix')
