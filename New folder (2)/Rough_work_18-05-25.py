'''def Even(num):
    if num%2==0:
        return 'even'
    return 'odd'
print(Even(11))
print(Even)

def Even(num):
    if num%2==0:
        return 'even'
    return 'odd'
print(Even(11))
print(Even(24))

num=14
def Prime(num):
    if num>1:
        count=0
        for val in range(1,num+1):
            if num%val==0:
                count+=1
        return count==2
print('Prime' if Prime(num) else 'not prime')

def composite(num):
    count=0
    for val in range(1,num+1):
        if num%val==0:
            count+=1
    return count>2
num=1,-5,6
print('composite' if composite(num) else 'not composite')

def Details(a,n,g):
    print(n)
    print(g)
    print(a)
Details(n='user',a=100,g='Male')

def Element(a,b,c=100):
    print(a)
    print(b)
    print(c)
Element(10,20)
Element(1,2,3)
Element(5,3)

def Elements(a,b=1,c='hello',d=0):
    print(a)
    print(b)
    print(c)
    print(d)
Elements(6)
print('--------------------')
Elements(22,33)
print('-----------------')
Elements(44,55,66,77)
print('-------------------')
Elements(a=6)
print('----------------------')
Elements(c=6,a=420)

def Elements(*args):
    print(args)
Elements(4,5,6)
Elements()
Elements(22,33,44,11,66,55,7)
Elements(6)

def Elements(**kwargs):
    print(kwargs)
Elements(a=20,b=60,c=10)
Elements()
Elements(a=20,b=60,c=10)

def Elements(a,b,c):
    print(a)
    print(b)
    print(c)
Elements(11,c=22,b=33)
Elements(11,b=22,c=33)

def Elements(a,b,c,d='hello'):
    print(a)
    print(b)
    print(c)
    print(d)
Elements(11,c=22,b=33)
Elements(11,c=22,b=33,d='bye')
def Elements(*args):
    print(args)
Elements(3,5,1)'''

def Elements(*args,**kwargs):
    print(args)
    print(kwargs)
Elements(3,5,1)
Elements(3,5,1,a=8,y=8)
Elements(a=0,q=5)
