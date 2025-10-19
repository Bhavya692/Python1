num=4
print(map(lambda line:'* '*num,range(1,num+1)))
num=4
mobj=map(lambda line:'* '*num,range(1,num+1))
for val in mobj:
    print(val)
num=4
print(list(map(lambda line:'* '*num,range(1,num+1))))

num=4
L=list(map(lambda line:'* '*num,range(1,num+1)))
print('\n'.join(L))

print('\n'.join(list(map(lambda line:'* '*num,range(1,num+1)))))

num=5
print('\n'.join(list(map(lambda line:'* '*num,range(1,num+1)))))

num=4
print('\n'.join(list(map(lambda line:'* '*line,range(1,num+1)))))
num=4
print('\n'.join(list(map(lambda line:'* '*line,range(num,0,-1)))))

num=4
print('\n'.join(list(map(lambda space,line:'  '*space+'* '*line,range(num-1,-1,-1),range(1,num+1)))))

num=4
print('\n'.join(list(map(lambda space,line:'  '*space+'* '*line,range(0,num),range(num,0,-1)))))
