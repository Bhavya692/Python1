'''s=input('Enter the collection:').split()
out=[]
for i in s:
    count=0
    for j in i:
        if j in 'AEIOUaeiou':
            count+=1
    out+=[(i,count,i[1::2])]
print(out)'''

'''s=input('Enter the collection:').split()
out=s[::-1]
print(' '.join(out))'''

s=input('enter the collection:')
out=' '.join(s.split()[::-1])
print(out)
