nam = input()
vowels=['a','e','i','o','u','A','E','I','O','U']
sum=0
for i in nam:
    if i in vowels:
        sum+=1
print(sum)
