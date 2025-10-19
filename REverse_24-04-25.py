def reverse(num,length=0):
    if num==0:
        return 0
    return (num%10)*(10**length)+reverse(num//10,length-1)
def Prime(num,val=1):
    if val==num+1:
        return 0
    if num%val==0:
        return 1+Prime(num,val+1)
    return 0+Prime(num,val+1)
num=10
print('PalyPrime Number' if reverse(num,length) and Prime(num)==2 else 'Not PalyPrime Number')
