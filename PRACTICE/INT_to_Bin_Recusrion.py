def binary(num,place=1):
    if num==0:
        return 0
    return(num%2)*place+binary(num//2,place*10)
num=13
print(binary(num))

def integer(num,power=0):
    if num==0:
        return 0
    return (num%10)*(2**power)+integer(num//10,power+1)
num=1000
print(integer(num))
