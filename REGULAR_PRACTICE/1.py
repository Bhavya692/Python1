print('----------------------FOR LOOP-----------------------------')
L=[44,'abcd',[44,33,22],False]
for ele in L:
    print(ele)
print(ele)

s={4,'abcd',False,(44,33,22),'hello'}
for ele in s:
    print(ele)

D = {4: 'abcd', True: False, (44, 33, 22): 'hello'}
for val in D.values():
    print(val)

D = {4: 'abcd', True: False, (44, 33, 22): 'hello'}
for key,value in D.items():
    print(f'{key}:{value}')

s='holi'
for ch1 in s:
    print(ch1)
    for ch2 in s:
        print(ch2)
    print('Iteration done')

s='abc'
for ch1 in s:
    print(ch1)
    for ch2 in s:
        print(ch2)
        for ch3 in s:
            print(ch3)
