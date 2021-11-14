num=int(input())
import math
day=[]
for i in range(num):
    cal=int(input())
    bol=cal/400
    day.append(int(math.ceil(bol)))

for j in day:
    print(j)