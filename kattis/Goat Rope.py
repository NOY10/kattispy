x,y,x1,y1,x2,y2=list(map(int,input().split()))
s=0
import math
if (x > x1 and x < x2 and y > y2):
    d = y - y2
elif(x > x2 and y > y2):
    d = math.hypot(x - x2, y - y2)
elif (x > x2 and y > y1 and y < y2):
    d = x - x2
elif (x > x2 and y < y1):
    d = math.hypot(x - x2, y1 - y)
elif (x > x1 and x < x2 and y < y1):
    d = y1 - y
elif (x < x1 and y < y1):
    d = math.hypot(x1 - x, y1 - y)
elif (x < x1 and y > y1 and y < y2):
    d = x1 - x
elif (x < x1 and y > y2):
    d = math.hypot(x1 - x, y - y2)
print(d)
