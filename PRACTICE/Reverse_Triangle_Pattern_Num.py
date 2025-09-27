num=5
for line in range(num,0,-1):
    for col in range(num-line+1):
        print(line,end='')
    print()
print('                      ')
num=5
line=num
while line>0:
    col=1
    while col<=num-line+1:
        print(line,end='')
        col+=1
    print()
    line-=1
        
