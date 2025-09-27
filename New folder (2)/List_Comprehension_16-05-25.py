'''L=[ele for ele in range(5)]
print(L)

L=[ele+ele for ele in range(5)]
print(L)

L=['hello' for ele in range(5)]
print(L)

L=[num for num in range(1,11)]
print(L)

L=[for ele in range(5)]
print(L)'''

'''s='abcde'
out=[ch for ch in s]
print(out)

s='abcde'
res=[s[ind]*(ind+1) for ind in range(0,len(s))]
print(res)

num=4
print('\n'.join([ind*'*' for ind in range(1,num+1)]))

length=6
L=[int(input('enter the element:'))for num in range(length)]
print(L)

for val1 in range(1,4):
    for val2 in range(7,9):
        print([val1,val2])

L=[val1 for val1 in range(1,4)]
print(L)

L=[val2 for val in range(1,4)for val2 in range(7,9)]
print(L)

L=[[val1,val2] for val1 in range(1,4) for val2 in range(7,9)]
print(L)

L=['hello' for val1 in range(1,4)for val2 in range(7,9)]
print(L)

for val1 in range(1,5):
    for  val2 in range(val1+1,6):
        print(val1,val2)

L=[[val1,val2]for val1 in range(1,5)for val2 in range(val1+1,6)]
print(L)

s='abcde'
print([s[val1:val2]for val1 in range(0,len(s))for val2 in range(val1+1,len(s)+1)]

for val1 in range(1,5):
    for val2 in range(val1+1,6):
        for val3 in range(val2+1,8):
            print(val1,val2,val3)'''
