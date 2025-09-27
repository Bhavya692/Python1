'''S=input('Enter the string collection:')
out=''
out1=''
for char in S:
    if 'a'<=char<='z':
        out+=char
    else:
        out1+=char
print(out)'''

'''S=input('Enter the string collection:')
out=''
out1=''
out2=''
for char in S:
    if 'a'<=char<='z':
        out+=char
    elif 'A'<=char<='Z':
        out1+=char
    elif '0'<=char<='9':
        out2+=char
print(out)
print(out1)
print(out2)'''

'''S=input('Enter the string collection:')
out=''
for char in S:
    if char in 'AEIOUaeiou':
        out+=char
print(out)'''

'''S=input('Enter the string collection:')
out=S[::-1]
print(out)'''

S=input('Enter the string collection:')
out=''
out1=''
for char in S:
    if 'a'<=char<='z':
        out+=char(ord(char)-32)
    else:
        out1+=char
print(out)
