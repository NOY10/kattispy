num=list(map(int,input().split()))
arr=[1,2,3,4,5]
while(True):
    for i in range(4):
      if num[i]>num[i+1]:
        temp=num[i]
        num[i]=num[i+1]
        num[i+1]=temp
        print(f"{num[0]} {num[1]} {num[2]} {num[3]} {num[4]}")
    if arr==num:
        break
