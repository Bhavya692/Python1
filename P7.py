
num=5
for ev in range(num+1,1,-1):
    for val in range(1,ev):
        print(val,end='')
    print()
num=5
ev=num
while ev>0:
    val=1
    while val<=ev:
        print(val,end='')
        val+=1
    print()
    ev-=1
