num=5
for sv in range(1,num+1):
    for val in range(sv,0,-1):
        print(val,end='')
        val+=1
    print()
    sv+=1

num=5
line=1
while line!=num+1:
    col=line
    while col>0:
        print(col,end='')
        col-=1
    print()
    
    line+=1
