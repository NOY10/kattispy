nam = input().split()
vow = ['a','i','o','u']
lastN=nam[0][len(nam[0])-1:len(nam[0])]
ex=nam[0][len(nam[0])-2:len(nam[0])]

if (lastN=='e'):
    lastN = f"{nam[0]}x{nam[1]}"
elif (lastN=='x'):
    if(ex=='ex'):
        lastN = nam[0]+ nam[1]

elif( lastN in vow):
    lastN = f"{nam[0][0:len(nam[0])-1]}ex{nam[1]}"
else:
    lastN = lastN = f"{nam[0]}ex{nam[1]}"

print(lastN)