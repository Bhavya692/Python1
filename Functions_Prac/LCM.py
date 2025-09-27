def Lcm(num1,num2):
        Lcm=max(num1,num2)
        while True:
            if (Lcm%num1==0) and (Lcm%num2==0):
                return Lcm
            Lcm+=1
num1=24
num2=26
print(Lcm(num1,num2))
