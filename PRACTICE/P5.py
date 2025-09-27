num=5
for line in range(1,num+2):
    for col in range(1,line):
        print(col,end='')
    print()

num=5
line=1
while line!=num+1:
    col=1
    while col!=line+1:
        print(col,end='')
        col+=1
    print()
    line+=1
