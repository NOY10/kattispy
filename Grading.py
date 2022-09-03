grade = list(map(int,input().split()))
num = int(input())

if (100>= num >= grade[0]):
    print("A")
elif(grade[0] > num >= grade[1]):
    print("B")
elif(grade[1] > num >= grade[2]):
    print("C")
elif(grade[2] > num >= grade[3]):
    print("D")
elif(grade[3] > num >= grade[4]):
    print("E")
elif(grade[4] > num ):
    print("F")
