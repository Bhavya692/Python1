num=24
print(list(map(lambda num:'even' if num%2==0 else 'odd',range(1,11))))

for ans in map(lambda num:'even' if num%2==0 else 'odd',range(1,11)):
    print(ans)
def Numbers(num):
    if num%2==0:
        return 'even'
    return 'odd'
print(list(map(Numbers,range(1,11))))
print(list(map(lambda num:num**2 if num%2==0 else num,[10,5,7,9,4,0])))

L1=[10,5,7,12]
L2=[1,2,3,4]
print(list(map(lambda num1,num2:num1+num2,[10,5,7,12],[1,2])))

L=['abcd','ab','','abc']
print(list(map(lambda ele:len(ele),L)))

print(list(map(len,L)))
print('-------------------------')
var=int(input())
print(var)
print(type(var))
print('-------------------------')
print('                        ')
var=input('Enter the value of var:')
print(var)
print(type(var))

print('                        ')
print('Hello')
print(var)
var=input('Enter the value of var:')
print(var)
print(type(var))

print('                        ')
n1=int(input('enter the value:'))
n2=int(input('enter the value:'))
print(n1+n2)


print('                        ')
length=int(input('enter the req length:'))
L=[]
for val in range(length):
    ele=int(input('enter the element:'))
    L.append(ele)
print(L)
