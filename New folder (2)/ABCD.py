num=5
space=num-1
for line in range(num-1,-1,-1):
    for sp in range(space):
        print(' ',end='')
    for val in range(num,line,-1):
        print(val,end='')
    print()
    space-=1

num=5
spaces=num-1
for line in range(num,0,-1):
    for sp in range(spaces):
        print(' ',end='')
    for val in range(line,num+1):
        print(val,end='')
    print()
    spaces-=1
