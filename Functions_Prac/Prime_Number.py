num=2
def Prime(num):
    if num>1:
        count=0
        for val in range(1,num+1):
            if num%val==0:
                count+=1
        if count==2:
            return 'Prime Number'
        return 'Not Prime'
print(Prime(num))

num=11
def Prime(num):
    if num>1:
        count=0
        for val in range(1,num+1):
            if num%val==0:
                count+=1
        return count==2
print('Prime' if Prime(num) else 'Not Prime')
