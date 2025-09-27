def DisArum(num,length,Sum=0):
    while num!=0:
        ld=num%10
        Sum=Sum+ld**length
        length-=1
        num//=10
    return Sum
num=89
print('DisArum' if num==DisArum(num,len(str(num))) else 'Not DisArum')
