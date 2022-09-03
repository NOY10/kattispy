num = list(map(int,input()))
binary = [1,2,4,8]
final = []
def draw(bi):
    bi.reverse()
    sum=""
    for i in range(len(bi)):
        if bi[i] == '1':
            sum = sum + "*"
        else:
            sum = sum + "."
    for i in range(4-len(bi)):
        sum = sum + "."
    print(sum )
    final.append(sum)



for i in num:
    draw(list(format(i, "b")))
print(final)






