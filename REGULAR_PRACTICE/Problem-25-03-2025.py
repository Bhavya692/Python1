num=13
val=1
count=0
while val!=num+1:
    if num%val==0:
        count=count+1
    val=val+1
if count==2:
    temp=num
    rev=0
    while temp!=0:
        ld=num%10
        rev=rev*10
        temp=temp//10
    if temp==rev:
        print('PalyPrime Number')
    else:
        print('Not PalyPrime')
else:
    print('Not PalyPrime')


num=41
copy=num
rev=0
while num!=0:
    ld=num%10
    rev=rev*10+ld
    num=num//10
if rev!=copy:
    count1=0
    val=1
    while val!=copy+1:
        if copy%val==0:
            count1=count1+1
        val=val+1
    if count1==2:
        count2=0
        val=1
        while val!=rev+1:
            if rev%val==0:
                count2+=1
            val+=1
        if count2==2:
            print('EMIRP Number')
        else:
            print('Not EMIRP')
    else:
        print('Not EMIRP')
else:
    print('Not EMIRP')


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
