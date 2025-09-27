def binary(num,place=1):
    if num==0:
        return 0
    return (num%2)*place+binary(num//2,place*10)
num=13
print(binary(num))
print('----------------------------')
num=1011
def Integer(num,power=0):
    if num==0:
        return 0
    return (num%10)*(2**power)+Integer(num//10,power+1)
print(Integer(num))
print('-----------------------------')
def Happy(num):
    if num>9:
        num=sq(num)
        return 'Happy Number'
    else:
        return num
def sq(num):
    if num==0:
        return 0
    return(num%10)**2+sq(num//10)
num=6
res=Happy(num)
print('Happy Number' if num==res else 'Not Happy Number')
print('----------------------------')
def Prime(num,val):
    if val==num+1:
        return 0
    if num%val==0:
        return 1+Prime(num,val+1)
    return 0+Prime(num,val+1)
num=6
val=1
print('Prime Number' if Prime(num,val)==2 else 'Not Prime Number')
print('------------------------------')
def reverse(num,length):
    if num==0:
        return 0
    return (num%10)*(10**length)+reverse(num//10,length-1)
def Prime(num,val=1):
    if val==num+1:
        return 0
    if num%10==0:
        return 1+Prime(num,val+1)
    return 0+Prime(num,val+1)
num=10
print('PalyPrime Number' if reverse(num) and Prime(num)==2 else 'Not PalyPrime Number')
print('-------------------------')
def reverse(num,length):
    if num==0:
        return 0
    return (num%10)*(10**length)+reverse(num//10,length-1)

num=234
print('reverse number'if reverse(num,len(str(num))-1) == num else 'not reverse number')
