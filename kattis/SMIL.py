nam = input()
eyes = [':',';'] 

for i in range(len(nam)):
    if nam[i] in eyes:
        if len(nam) > i+1:
            if nam[i+1]=='-':
                if len(nam) > i+2:
                    if nam[i+2] == ')':
                        print(i)
            elif nam[i+1]==')':
                print(i)