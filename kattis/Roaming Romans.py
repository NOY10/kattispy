num=float(input(""))
p=1000*5280/4854
if num==1:
  print(round(p))
else:
  print(round(p*num))