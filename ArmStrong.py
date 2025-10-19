def ArmStrong(num,length,Sum=0):
    while num!=0:
        ld=num%10
        Sum=Sum+ld**length
        num//=10
    return Sum
num=153
print('ArmStrong' if num==ArmStrong(num,len(str(num))) else 'Not ArmStrong')

def ArmStrong(num,length,dup,Sum=0):
    while num!=0:
        ld=num%10
        Sum=Sum+ld**length
        num//=10
    if dup==Sum:
        return 'ArmStrong'
    return 'Not ArmStrong'
num=153
print(ArmStrong(num,len(str(num)),num))

def DisArum(num,length,dup,Sum=0):
    while num!=0:
        ld=num%10
        Sum=Sum+ld**length
        length-=1
        num//=10
    if dup==Sum:
        return 'DisArum'
    return 'Not DisArum'
num=153
print(DisArum(num,len(str(num)),num))

def DisArum(num,length,Sum=0):
    while num!=0:
        ld=num%10
        Sum=Sum+ld**length
        length-=1
        num//=10
    return Sum
num=153
print('DisArum' if num==DisArum(num,(len(str(num)))) else 'Not DisArum')
        
