def Factorial(num,fact=1):
    for val in range(1,num+1):
        fact=fact*val
    return fact
def Strong(num,result=0):
    while num!=0:
        digit=num%10
        result=result+Factorial(digit)
        num//=10
    return result
def check(num):
    return('Strong Number' if Strong(num)==num else 'Not Strong Number')
num=145
print(check(num))
