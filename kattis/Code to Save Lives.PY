num = int(input())

for i in range(num):
    sum = 0
    fin =''
    aa = input().replace(" ","")
    bb = input().replace(" ","")
    sum = int(aa) + int(bb)
    for j in str(sum):
        fin = fin +j +' '
    print(fin)

