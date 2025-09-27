num=194
pattern=str(num*1)+str(num*2)+str(num*3)
for val in range(1,10):
    if str(val) not in pattern:
        print('Not Fascinating Number')
        break
else:
    print('Fascinating Number')
