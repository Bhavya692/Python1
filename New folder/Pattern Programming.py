num=5
for val in range(num):
    print('*')

num=5
for val in range(num):
    print('*',end='')

num=5
val=1
while val!=num+1:
    print('*')
    val+=1

num=5
while num!=0:
    print('*',end='')
    num-=1

num=5
for line in range(num):
    for col in range(num):
        print('*',end='')
    print()
print('-----------------------------------------------------------------------------')
num=5
line=0
while line!=num:
    col=0
    while col!=num:
        print('*',end='')
        col+=1
    line+=1
    print()

num=5
for line in range(1,num+1):
    for col in range(1,line+1):
        print('*',end='')
    print()

num=5
line=1
while line!=num+1:
    col=0
    while col!=line:
        print('*',end='')
        col=col+1
    print()
    line+=1

print('---------------------------------------------------------------------')

num=5
for line in range(num,0,-1):
    for col in range(line):
        print('*',end='')
    print()

num=5
line=num
while line!=0:
    col=1
    while col!=line+1:
        print('*',end='')
        col+=1
    line-=1
    print()

print('-------------------------------------------------------')

num=5
for line in range(1,num+1):
    for sp in range(num-line):
        print(' ',end='')
    for st in range(line):
        print('*',end='')
    print()
            
num=5
spaces=4
stars=1
for line in range(1,num+1):
    for  sp in range(spaces):
        print(' ',end='')
    for st in range(stars):
        print('*',end='')
    print()
    spaces-=1
    stars+=1

print('-------------------------------------------------------')

num=4
spaces=num-1
stars=1
for line in range(1,num+1):
    for sp in range(spaces):
        print(' ',end='')
    for st in range(stars):
        print('*',end='')
    print()
    spaces-=1
    stars+=2

num=4
for line in range(1,num+1):
    for sp in range(num-line):
        print(' ',end='')
    for st in range(2*line-1):
        print('*',end='')
    print()

print('------------------------------------------------------------')


num=4
for line in range(num):
    for sp in range(line):
        print(' ',end='')
    for st in range(2*(num-line)-1):
        print('*',end='')
    print()

print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')


num=4
spaces=0
stars=2*num-1
for line in range(num):
    for sp in range(spaces):
        print(' ',end='')
    for st in range(stars):
        print('*',end='')
    print()
    spaces+=1
    stars-=2

print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')

num=5
spaces=num//2
stars=1
for line in range(1,num+1):
    for sp in range(spaces):
        print(' ',end='')
    for st in range(stars):
        print('*',end='')
    print()
    if line<num//2+1:
        spaces-=1
        stars+=2
    else:
        spaces+=1
        stars-=2

print('--=============================================================--')

num=5
spaces=num//2
stars=1
line=1
while line!=num+1:
    sp=0
    while sp!=spaces:
        print(' ',end='')
        sp+=1
    st=0
    while st!=stars:
        print('*',end='')
        st+=1
    print()
    if line<num//2+1:
        spaces-=1
        stars+=2
    else:
        spaces+=1
        stars-=2
    line+=1


print('###################################################################')

num=5
spaces=0
stars=num
for line in range(1,num+1):
    for sp in range(spaces):
        print(' ',end='')
    for st in range(stars):
        print('*',end='')
    print()
    if line<num//2+1:
        spaces+=1
        stars-=2
    else:
        spaces-=1
        stars+=2
    line+=1

print('----------------------------------------------------')
num=5
spaces=0
stars=num
line=1
while line<=num:
    sp=0
    while sp<spaces:
        print(' ',end='')
        sp+=1
    st=0
    while st<stars:
        print('*',end='')
        st+=1
    print()
    if line<num//2+1:
        spaces+=1
        stars-=2
    else:
        spaces-=1
        stars+=2
    line+=1
