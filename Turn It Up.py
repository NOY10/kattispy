num = int(input())
volume = 7
name = []

for i in range(num):
    name.append(input())

for i in name:
    if i == 'Skru op!':
        volume+=1
        if (volume>=10):
            volume=10
    elif i == 'Skru ned!':
        volume-=1
        if (volume<=0):
            volume=0
print(volume)
