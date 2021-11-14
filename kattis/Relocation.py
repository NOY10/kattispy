           
nq=input().split(" ")
for i in range(0,1):
  inilo=input().split(" ")
for i in range(0,int(nq[-1])):
  q=input().split(" ")
  if 1==int(q[0]):
    inilo[int(q[1])-1]=int(q[2])
  elif 2==int(q[0]):
      sum=0
      sum=int(inilo[int(q[2])-1])-int(inilo[int(q[1])-1])
      if sum<0:
          sum=sum*-1
      print(sum)
      

