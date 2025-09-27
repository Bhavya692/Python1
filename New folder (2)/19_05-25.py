M=[[0,2,4],[1,2,7],[5,3,2]]
res=[]
for ind1 in range(len(M)-1,-1,-1):
    sublist=[]
    for ind2 in range(len(M)):
        sublist.append(M[ind2][ind1])
    res.append(sublist)
print(res)
