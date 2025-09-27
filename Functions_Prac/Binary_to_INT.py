def integer(num,power=0,decimal=0):
    while num!=0:
        ld=num%10
        decimal=decimal+ld*(2**power)
        num//=10
        power+=1
    return decimal
num=1000
print(integer(num))
