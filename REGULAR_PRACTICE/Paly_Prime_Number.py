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
