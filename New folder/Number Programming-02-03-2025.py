num=5
for line in range(1,num+1):
    for col in range(num):
        print(line,end='')
    print()

print('--------------------------------------------------')

num=5
line=1
while line!=num+1:
    col=0
    while col!=num:
        print(line,end='')
        col+=1
    print()
    line+=1

print('--------------------------------------------------')

num=5
for line in range(num,0,-1):
    for col in range(num):
        print(line,end='')
    print()

print('--------------------------------------------------')

num=5
line=num
while line!=0:
    col=0
    while col!=num+1:
        print(line,end='')
        col+=1
    print()
    line-=1
print('--------------------------------------------------')

num=5
for line in range(1,num+1):
    for col in range(line):
        print(line,end='')
    print()
    line+=1
print('--------------------------------------------------')

num=5
line=1
while line!=num+1:
    col=1
    while col!=line+1:
        print(line,end='')
        col+=1
    print()
    line+=1
    
print('--------------------------------------------------')

num=5
for line in range(num,0,-1):
    for col in range(num-line+1):
        print(line,end='')
    print()

print('--------------------------------------------------')

num=5
line=num
while line>0:
    col=1
    while col<=num-line+1:
        print(line,end='')
        col+=1
    print()
    line-=1

num=5
for ev in range(1,num+2):
    for val in range(1,ev):
        print(val,end='')
    print()

num=5
for sv in range(1,num+1):
    for val in range(sv,0,-1):
        print(val,end='')
    print()

num=5
for ev in range(num+1,1,-1):
    for val in range(1,ev):
        print(val,end='')
    print()
    
num=5
for sv in range(num,0,-1):
    for val in range(sv,0,-1):
        print(val,end='')
    print()

num=5
for sv in range(num,0,-1):
    for val in range(sv,num+1):
        print(val,end='')
    print()

num=5
for ev in range(num):
    for val in range(num,num-ev-1,-1):
        print(val,end='')
    print()

num=5
spaces=num-1
for ev in range(2,num+2):
    for sp in range(spaces):
        print(' ',end='')
    for val in range(1,ev):
        print(val,end='')
    print()
    spaces-=1

num=5
spaces=0
for ev in range(num+1,1,-1):
    for sp in range(spaces):
        print(' ',end='')
    for val in range(1,ev):
        print(val,end='')
    print()
    spaces+=1

num=5
spaces=num-1
for sv in range(num+1):
    for sp in range(spaces):
        print(' ',end='')
    for val in range(sv,num+1):
        print(val,end='')
    print()
    spaces-=1
