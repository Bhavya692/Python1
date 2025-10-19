num=5
line=1
while line!=num+1:
    col=0
    while col!=num:
        print(line,end='')
        col=col+1
    line+=1
    print()
print('----------------------')
num=5
for line in range(1,num+1):
    for col in range(num):
        print(line,end='')
    print()
