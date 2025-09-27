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
