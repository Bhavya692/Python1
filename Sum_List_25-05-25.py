L1=list(map(int,input('enter for L1:')))
L2=list(map(int,input('enter for L2:')))
print(list(map(lambda ele1,ele2:ele1+ele2,L1,L2)))

print(list(map(lambda ele1,ele2:ele1+ele2,list(map(int,input('enter for L1:').split())),list(map(int,input('enter for L2:').split())))))

print(list(map(float,input().split())))
