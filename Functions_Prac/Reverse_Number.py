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
