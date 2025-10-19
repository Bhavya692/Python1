num=5
spaces=0
stars=num
for line in range(1,num+1):
    for sp in range(spaces):
        print(' ',end='')
    for st in range(stars):
        print('*',end='')
    print()
    if line < num//2+1:
        spaces+=1
        stars-=2
    else:
        spaces-=1
        stars+=2
    line+=1

num=5
spaces=0
stars=num
line=1
while line <= num:
    sp=0
    while sp < spaces:
        print(' ',end='')
        sp+=1
    st=0
    while st < stars:
        print('*',end='')
        st+=1
    print()
    if line < num//2+1:
        spaces+=1
        stars-=2
    else:
        spaces-=1
        stars+=2
    line+=1
