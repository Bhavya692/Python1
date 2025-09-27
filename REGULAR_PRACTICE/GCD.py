num1=4
num2=8
if num1>num2:
    gcd=num2
else:
    gcd=num1
while True:
    if num1%gcd==0 and num2%gcd==0:
        print(gcd)
        break
    else:
        gcd-=1


num1=5
num2=4
num3=18
gcd=min(num1,num2,num3)
while True:
    if num1%gcd==0 and num2%gcd==0 and num3%gcd==0:
        print(gcd)
        break
    else:
        gcd-=1



num1=6
num2=8
gcd=min(num1,num2)
product=num1*num2
for val in range(gcd,0,-1):
    if num1%gcd==0 and num2%gcd==0:
        print(gcd)
        break
    else:
        gcd-=1
