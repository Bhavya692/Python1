num=19
def Happy(num):
    while num>9:
        num=Sq(num)
    return num==1 or num==7
def Sq(num,Sum=0):
    while num!=0:
        ld=num%10
        Sum=Sum+ld**2
        num//=10
    return Sum
print('Happy Number' if Happy(num) else 'Not Happy Number')
print('-------------------------')
num=192
def Fascinating(num,result):
    for val in range(1,10):
        if str(val) not in result:
            return 'Not Fascinating Number'
    return 'Fascinating Number'
result=str(num*1)+str(num*2)+str(num*3)
print(Fascinating(num,result))
print('---------------------')
num=9
def Perfect(num,val=0):
    while val*val<=num:
        if val*val == num:
            return 'Perfect Square'
        val+=1
    return 'Not Perfect Square'
print(Perfect(num))
print('---------------------')
def Sample():
    global val
    val=val+5
    print(val)
val=5
Sample()
print(val)
print('---------------------')
def Sample():
    global val
    val=5
    print(val)
Sample()
print(val)
print('---------------------')
def Sample():
    val=5
    print(val)
Sample()
print(val)
print('---------------------')
def Sample():
    global val
    val=5
    print(val)
val=10
Sample()
print(val)
Sample()
print('---------------------')
def Sample():
    global val
    val=5
    print(f'Local Space:{val}')
val=10
print(f'global Space:{val}')
Sample()
print(f'global Space:{val}')
print('---------------------')
a=10
a=5
print(a)
