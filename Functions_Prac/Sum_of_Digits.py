def add_digits(num):
    result=0
    while num!=0:
        ld=num%10
        result=result+ld
        num//=10
    return result
num=2420
print(add_digits(num))
