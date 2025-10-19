def Prime(num,val):
    if val==num+1:
        return 0
    if num%val==0:
        return 1+Prime(num,val+1)
    return 0+Prime(num,val+1)
num=6
val=1
print('Prime Number' if Prime(num,val)==2 else 'Not Prime')
