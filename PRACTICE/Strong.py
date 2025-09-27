def Factorial(num,fact=1):
    for val in range(1,num+1):
        fact*=val
    return fact
def Strong(num,rev=0):
    while num!=0:
        ld=num%10
        rev=rev+Factorial(ld)
        num//=10
    return rev
num=541
print('Strong' if Strong(num)==num else 'Not Strong')
