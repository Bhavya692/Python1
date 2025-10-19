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
print('--------------------------------')
def Reverse(num,rev=0):
    while num!=0:
        ld=num%10
        rev=rev*10+ld
        num=num//10
    return rev
def Prime(num,count=0):
    for val in range(1,num+1):
        if num%val==0:
            count+=1
    return count==2
num=7
print('PalyPrime' if(Prime(num) and Reverse(num)==num) else 'Not PalyPrime')
print('-------------------------------')
def Reverse(num,rev=0):
    while num!=0:
        ld=num%10
        rev=rev*10+ld
        num=num//10
    return rev
def Prime(num,count=0):
    for val in range(1,num+1):
        if num%val==0:
            count+=1
    return count==2
num=14
print('EMIRP Number' if(Prime(num) and Prime(Reverse(num))!=num) else 'Not EMIRP Number')
