def add_digits(num):
    result=0
    while num!=0:
        ld=num%10
        result=result+ld
        num//=10
    return result
num=2420
print(add_digits(num))

def Niven(num):
    result=0
    copy=num
    while num!=0:
        result=result+(num%10)
        num//=10
    return copy%result==0
num=18
print('Niven' if Niven(num) else 'Not Niven')

def Niven(num):
    result=0
    copy=num
    while num!=0:
        result=result+(num%10)
        num//=10
    return result
num=24
print('Niven Number' if num%Niven(num)==0 else 'Not Niven Number')
