num = list(map(str,input()))
CV = [4,3,2,7,6,5,4,3,2,1]
num.remove('-')
sum=0
for i in range(len(num)):
    pro = int(num[i]) * CV[i]
    sum=sum+pro

if (sum%11==0):
    print("1")
else:
    print("0")
