num=5
for line in range(num,0,-1):
    for col in range(line,0,-1):
        print(col,end='')
    print()
num=5
line=num
while line!=0:
    col=line
    while col!=0:
        print(col,end='')
        col-=1
    print()
    line-=1
