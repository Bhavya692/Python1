num=5
for sv in range(num+1,0,-1):
    for sp in range(sv-1):
        print(' ',end='')
    for val in range(sv,num+1):
        print(val,end='')
    print()

num=5
for ev in range(num,0,-1):
    for sp in range(ev-1):
        print(' ',end='')
    for  val in range(num,ev-1,-1):
        print(val,end='')
    print()

