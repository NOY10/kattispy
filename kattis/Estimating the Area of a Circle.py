
# while(True):
#     num=[float(i) for i in input().split()]
#     act=3.141592654*(num[0]**2)
#     Lc=num[2]/num[1]
#     exp=num[0]*Lc*4
#     print(act, exp)
#     if num[0]==0 and num[1]==0 and num[2]==0:
#         break
lst = [float(i) for i in input().split()]
while(lst[0] != 0 and lst[1] != 0 and lst[2] != 0):
  areaOfSquare = pow((lst[0]*2),2)
  areaOfCircle = lst[0]*lst[0]*3.141592654
  estimatedCircle = areaOfSquare*(lst[2]/lst[1])
  print(areaOfCircle, estimatedCircle)
  lst = [float(i) for i in input().split()]