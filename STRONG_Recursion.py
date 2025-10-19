def Factorial(num):
    if num==0 or num==1:
        return 1
    return num*Factorial(num-1)
def Strong(num):
    if num==0:
        return 0
    return Factorial(num%10)+Strong(num//10)
num=18
print(Strong(num))
def Factorial(num):
    if num==0 or num==1:
        return 1
    return num*Factorial(num-1)
def Strong(num):
    if num==0:
        return 0
    return Factorial(num%10) + Strong(num//10)
num=145
print(Strong(num))
