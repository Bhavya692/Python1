def ArmStrong(num,length,dup,Sum=0):
    while num!=0:
        ld=num%10
        Sum=Sum+ld**length
        num//=10
    if dup == Sum:
        return "ArmStrongNumber"
    return "NotArmStrong"
num=153
#print(ArmStrong(num, len(str(num)),num))
print('ArmStrong Number' if num==ArmStrong(num,len(str(num))) else 'Not ArmStrong Number')
