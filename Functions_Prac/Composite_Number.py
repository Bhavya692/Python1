def Comp(num):
    if num>3:
        count=0
        for val in range(1,num+1):
            if num%val==0:
                count+=1
        return count>2
num=8
print('Comp' if Comp(num) else 'Not Comp')

def Composite(num):
    count=0
    for val in range(1,num+1):
        if num%val==0:
            count+=1
    return count>2
num=6
print('Composite' if Composite(num) else 'Not Composite')
