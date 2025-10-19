def Sum_digits(num):
    if num==0:
        return 0
    return (num%10)+Sum_digits(num//10)
num=234
print(Sum_digits(num))
