num1=5
num2=6
if num1>num2:
    lcm=num1
else:
    lcm=num2
while True:
    if (lcm%num1==0) and (lcm%num2==0):
        print(lcm)
        break
    else:
        lcm+=1

        
num1=5
num2=2
num3=3
lcm=max(num1,num2,num3)
while True:
    if (lcm%num1==0) and (lcm%num2==0) and(lcm%num3==0):
        print(lcm)
        break
    else:
        lcm+=1

num1=5
num2=8
num3=6
lcm=max(num1,num2,num3)
product=num1*num2*num3
for val in range(lcm,product+1):
    if val%num1==0 and val%num2==0 and val%num3==0:
        print(val)
        break


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
