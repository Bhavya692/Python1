#Using Recurions in Binary search
def Binary_search(L,target,lind,hind):
    if lind>hind:
        return -1
    mind=(lind+hind)//2
    if L[mind]>target:
        return Binary_search(L,target,lind,mind-1)
    elif L[mind]<target:
        return Binary_search(L,target,mind+1,hind)
    else:
        return mind
L=[-3,0,7,10,11,88,420]
target=int(input('Enter element to search : '))
lind=0
hind=len(L)-1
print(Binary_search(L,target,lind,hind))
