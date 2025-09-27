'''s='pyTH@23oN'
count=0
ind=0
while ind!=len(s):
    if s[ind].isdigit():
        count+=1
    ind+=1
print(count)'''

'''s='pyTH@23oN'
count=0
ind=0
while ind!=len(s):
    if not('a'<=s[ind]<='z' or 'A'<=s[ind]<='Z' or '0'<=s[ind]<='9'):
        count+=1
    ind+=1
print(count)'''

'''s1='ant'
s2='tan'
if len(s1)==len(s2):
    for ch in s1:
        if (ch not in s2) or (s1.count(ch)!=s2.count(ch)):
            print('Not Anagram')
            break
    else:
        print('Anagram')
else:
    print('Not Anagram')'''

s='a quick brown fox jumps over the lazy dog'
for ascii in range(ord('a'),ord('z')+1):
    if chr(ascii) not in s:
        print('Not Panagram')
        break
else:
    print('Panagram')
