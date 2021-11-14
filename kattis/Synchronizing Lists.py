while(True):
    num=int(input())
    if num==0:
        break
    list1=[]
    list2=[]
    sort1=[]
    for i in range(num*2):
        if i < num:
            list1.append(int(input()))
            sort1.append(list1[i])
        else:
            list2.append(int(input()))
    sort1.sort()
    list2.sort()
    for i in range(num):
        for j in range(num):
            if list1[i]==sort1[j]:
                print(list2[j])
    print("\n")

        
