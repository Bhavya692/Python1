def Elements(**kwargs):
    print(kwargs)
Elements(a=30,b=60,c=10)
print('-----------------------')
def Elements(**kwargs):
    print(kwargs)
Elements()
print('-----------------------')
def Elements(a,b,c):
    print(a)
    print(b)
    print(c)
Elements(11,c=22,b=33)
print('-----------------------')
def Elements(a,b,c,d='hello'):
    print(a)
    print(b)
    print(c)
    print(d)
Elements(11,c=22,b=33)
Elements(11,c=22,b=33,d='bye')
print('-----------------------')
def Elements(*args):
    print(args)
Elements(3,5,1)
print('-----------------------')
def Elements(*args,**kwargs):
    print(args)
    print(kwargs)
Elements(3,5,1)
print('-----------------------')
Elements(3,5,1,a=8,y=8)
print('-----------------------')
Elements(a=0,q=5)
print('-----------------------')
def ArmStrong(num,length,dup,Sum=0):
    while num!=0:
        ld=num%10
        Sum=Sum+ld**length
        num//=10
    if dup == Sum:
        return "ArmStrongNumber"
    return "NotArmStrong"
num=153
print(ArmStrong(num, len(str(num)),num))
print('-----------------------')
def ArmStrong(num,length,Sum=0):
    while num!=0:
        ld=num%10
        Sum=Sum+ld**length
        num//=10
    return Sum
num=144
print('ArmStrong Number' if num==ArmStrong(num,len(str(num))) else 'Not ArmStrong Number')
print('-----------------------')
def DisArum(num,length,Sum=0):
    while num!=0:
        ld=num%10
        Sum=Sum+ld**length
        length-=1
        num//=10
    return Sum
num=89
print('DisArum' if num==DisArum(num,len(str(num))) else 'Not DisArum')
print('-----------------------')
def Reverse(num,Pos,Sum=0):
    while num>0:
        ld=num%10
        Sum=Sum+ld*Pos
        Pos//=10
        num//=10
    return Sum
num=145
Pos=10**(len(str(num))-1)
print(Reverse(num, Pos) if num==Reverse(num, Pos) else num)
print('-----------------------')
def Reverse(num,Sum=0):
    while num!=0:
        ld=num%10
        Sum=Sum*10+ld
        num//=10
    return Sum
num=234
print(Reverse(num))  
print('-----------------------')
def Palindrome(num,Sum=0):
    while num!=0:
        ld=num%10
        Sum=Sum*10+ld
        num//=10
    return Sum
num=147
print('Palindrome' if Palindrome(num)==num else 'Not Palindrome')
print('-----------------------')
def Lcm(num1,num2):
        Lcm=max(num1,num2)
        while True:
            if (Lcm%num1==0) and (Lcm%num2==0):
                return Lcm
            Lcm+=1
num1=24
num2=26
print(Lcm(num1,num2))
