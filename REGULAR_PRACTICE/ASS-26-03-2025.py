num=12
while num>9:
    sum=0
    while num!=0:
        ld=num%10
        sum=sum+ld**2
        num//=10
    num=sum
if num==1 or num==7:
    print('Happy Number')
else:
    print('Not Happy Number')

num=5
for val in range(num):
    print('*')
    
num=5
for val in range(num):
    print('*',end='')

num=5
line=0
while num!=0:
    col=0
    while col!=line+1:
        print('*')
