def Happy(num):
    while num>9:
        num=sq(num)
    return num==1 or num==7
def sq(num,result=0):
    while num!=0:
        ld=num%10
        result=result+ld**2
        num//=10
    return result
num=13
print('Happy Number' if Happy(num) else 'Not Happy Number')
