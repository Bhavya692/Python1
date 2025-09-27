num=89
val=0
while val*val<=num:
    if val*val==num:
        print('Perfect Square')
        break
    val=val+1
else:
    print('Not Perfect Square')


num=27
val=0
while val*val*val<=num:
    if val*val*val==num:
        print('Perfect Cube')
        break
    val=val+1
else:
    print('Not Perfect Cube')

num=148
pos=10**(len(str(num))-1)
sum=0
while num!=0:
    ld=num%10
    sum=sum+ld*(pos)
    num=num//10
    pos=pos//10
print(sum)

num=7
pos=10**(len(str(num))-1)
rev=0
temp=num
while num!=0:
    ld=num%10
    rev=rev+ld*pos
    pos=pos//10
    num=num//10
if temp==rev:
    print('Palindrome')
else:
    print('Not Palindrome')

num=143
val=0
while num!=0:
    ld=num%10
    val=val*10+ld
    num=num//10
print(val)

num=11
if bin(num)[-1]=='0':
    print('Even')
else:
    print('Odd')

num=0
if (num//2)*2==num:
    print('Even')
else:
    print('Odd')
