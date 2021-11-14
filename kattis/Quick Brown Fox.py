import string
num=int(input())
check=[]
for i in range(num):
    flag=False
    nam=input().lower()
    for letter in string.ascii_lowercase:
        if letter not in nam:
            check.append(letter)
            flag=True
    if flag:
        check.sort()
        st=''.join(check)
        print(f"missing {st}") 
        
    else:
        print('pangram')
    check.clear()
        
        