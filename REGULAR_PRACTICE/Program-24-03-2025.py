num=194
pattern=str(num*1)+str(num*2)+str(num*3)
for val in range(1,10):
    if str(val) not in pattern:
        print('Not Fascinating Number')
        break
else:
    print('Fascinating Number')

num1=5
num2=8
if num1>num2:
    lcm=num
else:
    lcm=num2
while True:
    if lcm%num1==0 and lcm%num2==0:
        print(lcm)
        break
else:
    lcm+=1
