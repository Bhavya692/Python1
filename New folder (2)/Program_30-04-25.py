'''s=input('Enter the String:')
out=s.replace(' ','*')
print(out)'''

s=input('Enter the String:')
out=''
for i in s:
    if i == ' ':
        out+='*'
    else:
         out+=i
print(out)
