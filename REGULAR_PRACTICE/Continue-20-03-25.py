print('-----------------------CONTROL STATEMENTS---------------------------')

num=189
temp=num
sum=0
while num!=0:
    ld=num%10
    sum=sum+ld
    num=num//10
if temp==num:
    print('Niven Number')
else:
    print('Not Niven Number')

num=323
length=len(str(num))
sum=0
temp=num
while num!=0:
    ld=num%10
    sum=sum+ld**length
    num=num//10
if temp==sum:
    print('Armstrong Number')
else:
    print('Not Armstrong Number')

num=135
length=len(str(num))
sum=0
temp=num
while num!=0:
    ld=num%10
    sum=sum+ld**length
    length=length-1
    num=num//10
if temp==sum:
    print('DiArum Number')
else:
    print('Not DisArum Number')

print('--------------------------BREAK--------------------------')
s='abcdef'
for ch in s:
    print(ch)
    if ch=='c':
        break
print('hello')

s='abcdef'
for ch in s:
    if ch=='c':
        print(ch)
    break
print('hello')

s='abcdef'
for ch in s:
    if ch=='c':
        break
    print(ch)
print('hello')

num=1
while num!=101:
    if num%5==0:
        print(num)
    num=num+1

num=28
if num>1:
    for val in range(2,num//2+1):
        if num%val==0:
            print('Not Prime')
            break
    else:
        print('Prime Number')
else:
    print('Not Prime')
