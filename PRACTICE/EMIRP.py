def reverse(num,rev=0):
    while num!=0:
        ld=num%10
        rev=rev*10+ld
        num//=10
    return rev!=num
def prime(num,count=0):
    for val in range(1,num+1):
        if num%val==0:
            count+=1
        return count==2
num=13
print('EMIRP Number' if prime(num) and prime(reverse(num)!=num) else 'Not EMIRP Number')
