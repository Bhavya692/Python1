def Palindrome(num,Sum=0):
    while num!=0:
        ld=num%10
        Sum=Sum*10+ld
        num//=10
    return Sum
num=143
print('Palindrome' if Palindrome(num)==num else 'Not Palindrome')
def Reverse(num,rev=0):
    while num!=0:
        ld=num%10
        rev=rev*10+ld
        num//=10
    return rev
num=154
print(Reverse(num))

def reverse(num,pos,Sum=0):
    while num!=0:
        ld=num%10
        Sum=Sum+ld*(pos)
        pos//=10
        num//=10
    return Sum
num=154
pos=10**(len(str(num))-1)
print(reverse(num,pos))
