pw1 = input()
pw2 = input()
pro=1
for i in range(4):
    if pw1[i] != pw2[i]:
        pro=pro*2
print(pro)