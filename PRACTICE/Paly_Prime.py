def Palindrome(num,rev=0):
    while num!=0:
        ld=num%10
        rev=rev*10+ld
        num//=10
    return rev
def Prime(num,count=0):
    for val in range(1,num+1):
        if num%val==0:
            count+=1
    return count==2
num=131
print('PalyPrime' if (Prime(num) and Palindrome(num)==num) else 'Not PalyPrime')
