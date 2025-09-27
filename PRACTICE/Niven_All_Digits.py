def Sum_digits(num):
    result=0
    for val in range(1,num+1):
        ld=num%10
        result=result+ld
        num//=10
    return result
num=1234
print(Sum_digits(num))

def Niven(num):
    temp=num
    result=0
    for val in range(1,num+1):
        ld=num%10
        result=result+ld
        num//=10
    return result
num=18
print('Niven' if num%Niven(num)==0 else 'Not Niven')

