num=5
for line in range(1,num+1):
    for col in range(line):
        print(line,end='')
    print()
print('----------------------')
num=5
line=1
while line!=num+1:
    col=1
    while col!=line+1:
        print(line,end='')
        col+=1
    print()
    line+=1
