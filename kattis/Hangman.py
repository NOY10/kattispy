p1=input()
per=input()
win=0
lose=0
for i in range(len(per)):
    if per[i] in p1:
        win=win+p1.count(per[i])
    if win==len(p1):
        print("WIN")
        break
    if per[i] not in p1:
        lose+=1
    if lose==10:
        print("LOSE")
        break
