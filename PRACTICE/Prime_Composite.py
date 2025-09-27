num=7
def Prime(num):
    if num>1:
        count=0
        for val in range(1,num+1):
            if num%val==0:
                count+=1
            if count==2:
                return 'Prime Number'
            return 'Not Prime Number'
print(Prime(num))

num=12
def Prime(num):
    if num>1:
        count=0
        for val in range(1,num+1):
            if num%val==0:
                count+=1
        return count==2
print('Prime' if Prime(num) else 'Not Prime')

num=6
def Composite(num):
    if num>3:
        count=0
        for val in range(1,num+1):
            if num%val==0:
                count+=1
        return count>2
print('Composite' if Composite(num) else 'Not Composite')
