first=input()
second=input()
x=[char for char in first]
y=[char for char in second]
x1=x.count("a")
y1=y.count("a")
if x1<y1:
    print("no")
else:
    print("go")