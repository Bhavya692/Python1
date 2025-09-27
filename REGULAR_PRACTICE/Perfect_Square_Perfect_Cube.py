num=89
val=0
while val*val<=num:
    if val*val==num:
        print('Perfect Square')
        break
    val=val+1
else:
    print('Not Perfect Square')


num=27
val=0
while val*val*val<=num:
    if val*val*val==num:
        print('Perfect Cube')
        break
    val=val+1
else:
    print('Not Perfect Cube')
