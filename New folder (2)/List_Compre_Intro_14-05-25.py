'''s='4 8 12 6 3'
print(list(map(int,s.split())))'''

'''
#Using Built-in-Methods
L=[4,6,2,3,1,9]
L.reverse()
print(L)'''

'''
#Using Slicing
L=[4,6,2,3,1,9]
print(L[::-1])'''

'''
#Using Negative Indexing
L=[4,6,2,3,1,9]
ans=[]
for ind in range(-1,-len(L)-1,-1):
    ans.append(L[ind])
print(ans)'''

'''
#Using Positive Indexing
L=[4,6,2,3,1,9]
ans=[]
for ind in range(len(L)-1,-1,-1):
    ans.append(L[ind])
print(ans)'''

'''
#Without Using Built-In-Method
L=[4,6,2,3,1,9]
res=[]
for ele in L:
    res=[ele]+res
print(res)'''

'''
Two-Pointer Method
L=[4,6,2,3,1,9]
for ind in range(len(L)//2):
    L[ind],L[-ind-1]=L[-ind-1],L[ind]
print(L)'''

'''L=[3,1,5,9,2,4,6]
target=7
for ind1 in range(0,len(L)-1):
    for ind2 in range(ind1+1,len(L)):
        if(L[ind1]+L[ind2])==target:
            print(L[ind1],L[ind2])'''

'''L=[3,1,5,9,2,4,6]
target=7
ind1=0
while ind1!=len(L)-1:
    ind2=ind1+1
    while ind2!=len(L):
        if(L[ind1]+L[ind2])==target:
            print(L[ind1],L[ind2])
        ind2+=1
    ind1+=1'''

L=[3,1,5,9,2,4,6]
for ele in L:
    count=0
    for num in range(1,ele+1):
        if ele%num==0:
            count+=1
    if count==2:
        print(ele)
