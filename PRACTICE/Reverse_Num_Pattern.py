num=5
for line in range(num,0,-1):
    for col in range(num):
        print(line,end='')
    print()
print('----------------------')
num=5
line=num
while line!=0:
    col=0
    while col!=num+1:
        print(line,end='')
        col+=1
    print()
    line-=1
