def Sample(num):
    if num==6:
        return
    print(num)
    num+=1
    Sample(num)
num=1
print(Sample(num))
print('------------------')
def Sample(num):
    if num==6:
        return 500
    print(num)
    num+=1
    Sample(num)
num=1
print(Sample(num))
print('------------------')
def Sample(num):
    if num==6:
        return
    print(num)
    num+=1
    return Sample(num)
num=1
Sample(num)
print('------------------')
def Sample(num):
    if num==-11:
        return
    print(num)
    num-=1
    Sample(num)
num=-1
Sample(num)
print('------------------')
def Sample(num):
    if num==-11:
        return 400
    print(num)
    num-=1
    return Sample(num)
num=-1
Sample(num)
print('------------------')
def Sample(num):
    if num==9:
        return
    print(num)
    num-=1
    Sample(num)
num=20
Sample(num)
print('------------------')
def Sample(num):
    if num==12:
        return
    print(num)
    num+=1
    Sample(num)
num=1
Sample(num)
print('------------------')
def Sample(num):
    if num==12:
        return
    if num%2==0:
        print(num)
    num+=1
    Sample(num)
num=1
Sample(num)
print('------------------')
def Sample(num):
    if num==12:
        return
    if num%2==0:
        print(num)
    Sample(num+1)
num=1
Sample(num)
