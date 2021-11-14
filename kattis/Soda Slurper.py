p, d, new=list(map(int,input().split()))
tot=p+d
ans=0
rem=0
drink=0
while(new<=tot):
  ans=tot//new
  rem=tot%new
  tot=ans+rem
  drink+=ans
print(drink)
    
