def DisArum(num,length):
    if num==0:
        return 0
    return(num%10)**length+DisArum(num//10,length-1)
num=135
print('DisArum' if num==DisArum(num,len(str(num))) else 'Not DisArum')
