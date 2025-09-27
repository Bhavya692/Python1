'''
#Using For Loop
L=[1,2,18,4,7,420,18,4]
target=int(input('Enter the element to search :'))
for ind in range(len(L)):
    if L[ind]==target:
        print(ind)
        break
else:
    print(-1)

#Using While Loop
L=[1,2,18,4,7,420,18,4]
target=int(input('Enter the element to search :'))
ind=0
while ind!=len(L):
    if L[ind]==target:
        print(ind)
        break
    ind+=1
else:
    print(-1)

#Using Functions For Loop
L=[1,2,18,4,7,420,18,4]
target=int(input('Enter the element to search :'))
def Linear_search(L,target):
    for ind in range(len(L)):
        if L[ind]==target:
            return ind
    return -1
print(Linear_search(L,target))

#Using Functions While Loop
L=[1,2,18,4,7,420,18,4]
target=int(input('enter element to search :'))
def list(L,target):
    ind=0
    while ind!=len(L):
        if L[ind]==target:
            return ind
        ind+=1
    return -1
print(list(L,target))

#Using Recursion
L=[1,2,18,4,7,420,18,4]
target=int(input('enter element to search :'))
def Linear_search(L,target,ind=0):
    if ind==len(L):
        return -1
    if L[ind]==target:
        return ind
    return Linear_search(L,target,ind+1)
print(Linear_search(L,target))

#Binary search Program
L=[-3,0,7,10,11,88,420]
target=7
lind=0
hind=len(L)-1
while lind<=hind:
    mind=(lind+hind)//2
    if L[mind]>target:
        hind=mind-1
    elif L[mind]<target:
        lind=mind+1
    elif L[mind]==target:
        print(mind)
        break
else:
    print(-1)

#Using Functions in Binary search
L=[-3,0,7,10,11,88,420]
target=7
hind=len(L)-1
def Binary_search(L,target,hind):
    lind=0
    while lind<=hind:
        mind=(lind+hind)//2
        if L[mind]>target:
            hind=mind-1
        elif L[mind]<target:
            lind=mind+1
        elif L[mind]==target:
            return mind
    return -1
print(Binary_search(L,target,hind))

#Using Recursions in Binary search
def Binary_search(lind,hind):
    if lind>hind:
        return -1
    mind=(lind+hind)//2
    if L[mind]<target:
       return Binary_search(mind+1,hind)
    elif L[mind]>target: 
       return Binary_search(lind,mind-1)
    elif L[mind]==target:
        return mind
L=[-3,0,7,10,11,88,420]
target=int(input('enter element to search : '))
lind=0
hind=len(L)-1
print(Binary_search(lind,hind))'''
