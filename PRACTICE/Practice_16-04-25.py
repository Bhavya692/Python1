def Factorial(num,fact=1):
    if num==0:
        return fact
    return Factorial(num-1,fact*num)
num=4
print(Factorial(num))
print('--------------------------------')
def Factorial(num):
    return 1 if num==0 or num==1 else num*(Factorial(num-1))
num=4
print(Factorial(num))
print('-----------------------')
def Factorial(num):
    if num==0 or num==1:
        return 1
    return num*(Factorial(num-1))
num=4
print(Factorial(num))
print('-----------------------')
def Factorial(num,val=1):
    if val==num+1:
        return 1
    return val*(Factorial(num,val+1))
num=5
print(Factorial(num))
print('-----------------------')
def Sum_digits(num):
    if num==0:
        return 0
    return (num%10)+Sum_digits(num//10)
num=234
print(Sum_digits(num))
print('-----------------------')
def Sum_digits(num):
    return 0 if num==0 else (num%10)+Sum_digits(num//10)
num=234
print(Sum_digits(num))
