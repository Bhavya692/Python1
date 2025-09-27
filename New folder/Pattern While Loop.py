num=5
line=1
while line!=num+1:
    col=1
    while col!=line+1:
        print(col,end='')
        col+=1
    print()
    line+=1

num=5
line=1
while line!=num+1:
    col=line
    while col>0:
        print(col,end='')
        col-=1
    print()
    line+=1

num=5
line=num
while line>0:
    col=1
    while col<=line:
        print(col,end='')
        col+=1
    print()
    line-=1

num=5
line=num
while line>0:
    col=1
    while col<=line:
        print(line,end='')
        col+=1
    print()
    line-=1

num=5
for line in range(num,0,-1):
    for val in range(line):
        print(line,end='')
    print()

num=5
line=num
while line>0:
    col=line
    while col>0:
        print(col,end='')
        col-=1
    print()
    line-=1

num=5
line=num
while line>0:
    col=line
    while col<=num:
        print(col,end='')
        col+=1
    print()
    line-=1

num=5
line=1
while line<=num:
    col=num
    while col>=num-line+1:
        print(col,end='')
        col-=1
    print()
    line+=1

num=5
line=1
while line<=num:
    print(' '*(num-line),end='')
    col=1
    while col<=line:
        print(col,end='')
        col+=1
    print()
    line+=1

num=5
line=num
while line>0:
    col=1
    while col<=line:
        print(col,end='')
        col+=1
    print()
    line-=1
