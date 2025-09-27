def Prime(num):
    for val in range(2,num//2+1):
        if num%val==0:
            return False
        return True
print(list(filter(Prime,range(10,20))))

def ArmStrong(num,Sum=0):
    power=len(str(num))
    dup=num
    while num!=0:
        ld=num%10
        Sum=Sum+ld**power
        num//=10
    return Sum==dup
print(list(filter(ArmStrong,range(1,500))))
def ArmStrong(num,Sum=0):
    power=len(str(num))
    dup=num
    while num!=0:
        ld=num%10
        Sum=Sum+ld**power
        num//=10
    return Sum==dup
fobj=filter(ArmStrong,range(1,500))
for val in fobj:
    print(val)
print(tuple(filter(lambda num:True if num%2==0 else False,range(10,21))))
print(tuple(filter(lambda num:num%2==0,range(10,21))))

def Happy(num):
    while num>9:
        Sum=0
        while num!=0:
            ld=num%10
            Sum=Sum+ld**2
            num//=10
        num=Sum
    return num==1 or num==7
print(list(filter(Happy,range(1,100))))   
