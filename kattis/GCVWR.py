num = list(map(int,input().split()))
num2 = list(map(int,input().split()))
sum= sum(num2)
GT = ((num[0] - num[1]) * 90)/100
print(int(GT-sum))