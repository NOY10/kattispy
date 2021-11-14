X=set()
Y=set()
x=[]
y=[]
for i in range(3):
    num1, num2=list(map(int,input().split()))
    x.append(num1)
    y.append(num2)
    if x[i] in X:
        X.remove(x[i])
    else:
        X.add(x[i])
    if y[i] in Y:
        Y.remove(y[i])
    else:
        Y.add(y[i])
print(X.pop(), Y.pop())