num=155
dup=num
result=0
while num!=0:
    rem=num%10
    fact=1
    val=1
    while val!=rem+1:
        fact=fact*val
        val=val+1
    result=result+fact
    num=num//10
if result==dup:
    print('Strong Number')
else:
    print('Not Strong Number')
