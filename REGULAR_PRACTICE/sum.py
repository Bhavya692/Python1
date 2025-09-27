num = 45678
sum=0
while num!=0:
    rem=num%10
    if rem%2==0:
        sum=sum+rem
    num=num//10
print(sum)

num=456789
sumadd=0
while num !=0:
    ld=num%10
    sumadd=sumadd+ld
num=num//10
