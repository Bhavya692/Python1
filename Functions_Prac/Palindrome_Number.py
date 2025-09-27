def Palindrome(num,Sum=0):
    while num!=0:
        ld=num%10
        Sum=Sum*10+ld
        num//=10
    return Sum
num=147
print('Palindrome' if Palindrome(num)==num else 'Not Palindrome')
