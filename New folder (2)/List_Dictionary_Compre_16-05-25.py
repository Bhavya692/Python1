'''print([val for val in range(10,30)if val%2==0])

print([val for val in range(10,30)if val%2!=0])

print([val for val in range(10,30)if val%2==0 and val%3==0])

s='we will attend class everyday'
print(''.join([ch for ch in s if(ch in'aeiouAEIOU')]))

s='we will attend class everyday'
print(''.join([ch for ch in s if(('a'<=ch<='z' or 'A'<=ch<='Z') and (ch not in 'aeiouAEIOU'))]))

s='we will attend class everyday'
print([s[ind]for ind in range(0,len(s),2)])

s='we will attend class everyday'
print([s[ind]for ind in range(len(s))if ind%2==0])


print(['even' if val%2==0 else 'odd' for val in range(10,20)])
print([val**2 if val%2==0 else val**3 for val in range(1,10)])
print(val for val in range(1,6))

num=13
print(len([val for val in range(1,num+1)if num%val==0])) 

num=15
print('prime'if(len([val for val in range(1,num+1)if num%val==0])==2)else 'not prime')'''

print({ele for ele in range(-10,10)})
print({ele:ele*2 for ele in range(3,9)})

s='sunday'
print({s[ind]:ind for ind in range(0,len(s))})

s='we will attend class everyday'
print({ind:s[ind] for ind in range(0,len(s))if s[ind] in 'aeiouAEIOU'})

print({ind:'even' if ind%2==0 else 'odd' for ind in range(1,10)})
