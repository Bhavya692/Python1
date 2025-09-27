'''L=[-3,0,7,10,11,88,420]
target=11
lind=0
hind=len(L)-1
while lind<=hind and L[lind]<=target<=L[hind]:
    ind=int(lind+(hind-lind)/(L[hind]-L[lind])*(target-L[lind]))
    if L[ind]>target:
        hind=ind-1
    elif L[ind]<target:
        lind=ind+1
    elif L[ind]==target:
        print(ind)
        break
else:
    print(-1)

L=[-3,0,7,10,11,88,420]
target=11
lind=0
hind=len(L)-1
def Binary(L,target,lind=0,hind=len(L)-1):
    while lind<=hind and L[lind]<=target<=L[hind]:
        ind=int(lind+(hind-lind)/(L[hind]-L[lind])*(target-L[lind]))
        if L[ind]>target:
            hind=ind-1
        elif L[ind]<target:
            lind=ind+1
        elif L[ind]==target:
            return ind
    return -1
print(Binary(L,target))

#Using BUbble sort
L=[4,7,420,1,0,22]
for ind1 in range(len(L)-1):
    for ind2 in range(len(L)-1-ind1):
        if L[ind2]>L[ind2+1]:
            L[ind2],L[ind2+1]=L[ind2+1],L[ind2]
print(L)

#To get the Highest Number
L=[4,7,420,1,0,22]
for ind1 in range(3):
    for ind2 in range(len(L)-1-ind1):
        if L[ind2]>L[ind2+1]:
            L[ind2],L[ind2+1]=L[ind2+1],L[ind2]
print(L[-3])

#To get the Lowest Number
L=[4,7,420,1,0,22]
for ind1 in range(4):
    for ind2 in range(len(L)-1-ind1):
        if L[ind2]<L[ind2+1]:
            L[ind2],L[ind2+1]=L[ind2+1],L[ind2]
print(L[-4])

#To get the Highest Element without sorting Method
L=[4,7,420,1,0,22]
highv=L[0]
for ind in range(1,len(L)):
    if highv<L[ind]:
        highv=L[ind]
print(highv)

#To get the Highest Element without sorting Method
L=[4,7,420,1,0,22]
leastv=L[0]
for ind in range(1,len(L)):
    if leastv>L[ind]:
        leastv=L[ind]
print(leastv)'''

#Using Selection sort
L=[4,7,420,1,7,22]
leastind=L[0]
for ind1 in range(len(L)-1):
    leastind1=ind1
    for ind2 in range(ind1+1,len(L)):
        if L[leastind]>L[ind2]:
            leastind=ind2
    L[leastind],L[ind1]=L[ind1],L[leastind]
print(L)

#Using Selection sort
L=[4,7,420,1,7,22]
leastind=L[0]
for ind1 in range(len(L)-1):
    leastind1=ind1
    for ind2 in range(ind1+1,len(L)):
        if L[leastind]<L[ind2]:
            leastind=ind2
    L[leastind],L[ind1]=L[ind1],L[leastind]
print(L[1])
