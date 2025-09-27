def Factorial(num,fact=1):
    if num==0:
        return fact
    fact=fact*num
    return Factorial(num-1,fact)
num=4
print(Factorial(num))

def Factorial(num,fact=1):
    if num==0:
        return fact
    return Factorial(num-1,fact*num)
num=5
print(Factorial(num))

def Factorial(num,fact=1):
    return 1 if num==1 or num==0 else num*(Factorial(num-1))
num=5
print(Factorial(num))
