def rectangle(x1,y1,x2,y2,x,y):
    return x1<=x<=x2 and y1<=y<=y2
def circle(x1,y2,radius,x,y):
    return (x1-x)**2 + (y2-y)**2<=radius**2


num=int(input())
shape=[]
for i in range(num):
    shape.append(list(input().split()))
target=int(input())

for j in range(target):
    c=0
    x,y=list(map(int,input().split()))
    for points in shape:
        if points[0]=='rectangle' and rectangle(int(points[1]),int(points[2]),int(points[3]),int(points[4]),x,y):
            c+=1
        if points[0]=='circle' and circle(int(points[1]),int(points[2]),int(points[3]),x,y):
            c+=1
    print(c)

