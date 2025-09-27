Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
L=[3,2,'a']
L.append('aaaa')
L
[3, 2, 'a', 'aaaa']
L.append((12,23,'aaa',78))
L
[3, 2, 'a', 'aaaa', (12, 23, 'aaa', 78)]
L.append({12,78,'abc',True,False,4+9j})
L
[3, 2, 'a', 'aaaa', (12, 23, 'aaa', 78), {False, True, 'abc', 12, 78, (4+9j)}]
L.append({'a':234,5+6j:34,True:False})
L
[3, 2, 'a', 'aaaa', (12, 23, 'aaa', 78), {False, True, 'abc', 12, 78, (4+9j)}, {'a': 234, (5+6j): 34, True: False}]
L.append([12,'a','b',5+6j,True,{12,'k',89}])
L
[3, 2, 'a', 'aaaa', (12, 23, 'aaa', 78), {False, True, 'abc', 12, 78, (4+9j)}, {'a': 234, (5+6j): 34, True: False}, [12, 'a', 'b', (5+6j), True, {'k', 89, 12}]]
L.append(12,3444)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    L.append(12,3444)
TypeError: list.append() takes exactly one argument (2 given)
L.append()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    L.append()
TypeError: list.append() takes exactly one argument (0 given)
L.insert()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    L.insert()
TypeError: insert expected 2 arguments, got 0
L.insert(12)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    L.insert(12)
TypeError: insert expected 2 arguments, got 1
L.insert(5,'aaa')
L
[3, 2, 'a', 'aaaa', (12, 23, 'aaa', 78), 'aaa', {False, True, 'abc', 12, 78, (4+9j)}, {'a': 234, (5+6j): 34, True: False}, [12, 'a', 'b', (5+6j), True, {'k', 89, 12}]]
L=[32,89,'g']
L.insert(2,'aaa')
L
[32, 89, 'aaa', 'g']
L.insert(-2,'kkkk')
L
[32, 89, 'kkkk', 'aaa', 'g']
L.insert(0,7+2j)
L
[(7+2j), 32, 89, 'kkkk', 'aaa', 'g']
L.insert(4,8+3j)
L
[(7+2j), 32, 89, 'kkkk', (8+3j), 'aaa', 'g']
L.insert(5,89)
L
[(7+2j), 32, 89, 'kkkk', (8+3j), 89, 'aaa', 'g']
L.insert(-1,24444444)
L
[(7+2j), 32, 89, 'kkkk', (8+3j), 89, 'aaa', 24444444, 'g']
L.insert(-7,True)
L
[(7+2j), 32, True, 89, 'kkkk', (8+3j), 89, 'aaa', 24444444, 'g']
L.insert(-14,False)
L
[False, (7+2j), 32, True, 89, 'kkkk', (8+3j), 89, 'aaa', 24444444, 'g']
L.insert(100000,TRue)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    L.insert(100000,TRue)
NameError: name 'TRue' is not defined. Did you mean: 'True'?
L.insert(100000,True)

L
[False, (7+2j), 32, True, 89, 'kkkk', (8+3j), 89, 'aaa', 24444444, 'g', True]
L.insert('True')
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    L.insert('True')
TypeError: insert expected 2 arguments, got 1
L.insert(-1,'True')
L
[False, (7+2j), 32, True, 89, 'kkkk', (8+3j), 89, 'aaa', 24444444, 'g', 'True', True]
L.extend((12,456),['abc',23,True],{'a':23,'g':0})
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    L.extend((12,456),['abc',23,True],{'a':23,'g':0})
TypeError: list.extend() takes exactly one argument (3 given)
L.extend((12,45,'a'))
L
[False, (7+2j), 32, True, 89, 'kkkk', (8+3j), 89, 'aaa', 24444444, 'g', 'True', True, 12, 45, 'a']
L.extend({'a':8,'b':23})
L
[False, (7+2j), 32, True, 89, 'kkkk', (8+3j), 89, 'aaa', 24444444, 'g', 'True', True, 12, 45, 'a', 'a', 'b']
L.append(12,78)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    L.append(12,78)
TypeError: list.append() takes exactly one argument (2 given)
L.append(12
        )
L
[False, (7+2j), 32, True, 89, 'kkkk', (8+3j), 89, 'aaa', 24444444, 'g', 'True', True, 12, 45, 'a', 'a', 'b', 12]
L=[23,90,100]
L.append(1)
L
[23, 90, 100, 1]
L.extend(1)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    L.extend(1)
TypeError: 'int' object is not iterable
L.extend(12,34,78)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    L.extend(12,34,78)
TypeError: list.extend() takes exactly one argument (3 given)
L.extend((21,'a'))
L
[23, 90, 100, 1, 21, 'a']
L.insert(6,(12,'a',True))
L
[23, 90, 100, 1, 21, 'a', (12, 'a', True)]
L.insert(1,{'a':20,'b':12})
L
[23, {'a': 20, 'b': 12}, 90, 100, 1, 21, 'a', (12, 'a', True)]
L.insert(2,True)
L
[23, {'a': 20, 'b': 12}, True, 90, 100, 1, 21, 'a', (12, 'a', True)]
L.remove(23)
L
[{'a': 20, 'b': 12}, True, 90, 100, 1, 21, 'a', (12, 'a', True)]
L.remove({'a':20,'b':12})
L
[True, 90, 100, 1, 21, 'a', (12, 'a', True)]
L.remove(True,21)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    L.remove(True,21)
TypeError: list.remove() takes exactly one argument (2 given)
L.remove(21)
L
[True, 90, 100, 1, 'a', (12, 'a', True)]
L.remove(12)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    L.remove(12)
ValueError: list.remove(x): x not in list
L.remove('a')
L
[True, 90, 100, 1, (12, 'a', True)]
L.remove('a')
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    L.remove('a')
ValueError: list.remove(x): x not in list
L.remove()
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    L.remove()
TypeError: list.remove() takes exactly one argument (0 given)
L.clear()
L
[]
L=[3,8,9,10]
L.pop()
10
L.pop(1)
8
L.pop(4)
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    L.pop(4)
IndexError: pop index out of range
L.pop(3,9)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    L.pop(3,9)
TypeError: pop expected at most 1 argument, got 2
L.copy()
[3, 9]
dup=L.copy()
dup
[3, 9]
id(dup)
1663385647936
L
[3, 9]
id(L)
1663380578688
L.count()
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    L.count()
TypeError: list.count() takes exactly one argument (0 given)
L.count(1)
0
L.count(3)
1
''.join(L)
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    ''.join(L)
TypeError: sequence item 0: expected str instance, int found
L=['a','c','h']
''.join(L)
'ach'
'Z'.join(L)
'aZcZh'
'Z '.join(L)
'aZ cZ h'
' Z '.join(L)
'a Z c Z h'
L.sort()
L
['a', 'c', 'h']

L.sort(reverse=True)
L
['h', 'c', 'a']
L.sortt(reverse=False)
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    L.sortt(reverse=False)
AttributeError: 'list' object has no attribute 'sortt'. Did you mean: 'sort'?
L.sort(reverse=False)
L
['a', 'c', 'h']
L.sort(reverse=True)
L
['h', 'c', 'a']
L.max()
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    L.max()
AttributeError: 'list' object has no attribute 'max'
L=[86,90,100]
L
[86, 90, 100]
max(L)
100
min(L)
86
T=(3+9j,12,'a')
T
((3+9j), 12, 'a')
lenT)
SyntaxError: unmatched ')'
len(T)
3
T.index(1)
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    T.index(1)
ValueError: tuple.index(x): x not in tuple
T.index('a')
2
T.index(3+9j)
0
T.count('a',1,3)
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    T.count('a',1,3)
TypeError: tuple.count() takes exactly one argument (3 given)
T.index('a',1,3)
2
T.index('a',3,5)
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    T.index('a',3,5)
ValueError: tuple.index(x): x not in tuple
T.index('a',2,6)
2
T.index('a',1,6)
2
T.index('a',1,4)
2
T.index('a',3,5)
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    T.index('a',3,5)
ValueError: tuple.index(x): x not in tuple
T.index('a')
2
T.count()
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    T.count()
TypeError: tuple.count() takes exactly one argument (0 given)
T.count('a')
1
max(T)
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    max(T)
TypeError: '>' not supported between instances of 'int' and 'complex'
T
((3+9j), 12, 'a')
max(T)
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    max(T)
TypeError: '>' not supported between instances of 'int' and 'complex'
T.insert(12)
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    T.insert(12)
AttributeError: 'tuple' object has no attribute 'insert'
T=(12,'a',78,100)
max(T)
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    max(T)
TypeError: '>' not supported between instances of 'str' and 'int'
T=(24,89,56)
max(T)
89
miin(T)
Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    miin(T)
NameError: name 'miin' is not defined. Did you mean: 'min'?
min(T)
24
sum(T)
169
len()
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    len()
TypeError: len() takes exactly one argument (0 given)
s=set()
s.add(24)
s
{24}
s.add('a')
s
{24, 'a'}
s.add(3+5j)
s
{24, (3+5j), 'a'}
s.add(0.8)
s
{24, 0.8, (3+5j), 'a'}
s.add((12,43))
s
{0.8, 'a', (3+5j), 24, (12, 43)}
s.add([23,'a',24])
Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    s.add([23,'a',24])
TypeError: unhashable type: 'list'
s.add('abcd')
s
{0.8, 'abcd', 'a', (3+5j), 24, (12, 43)}
s.add({'a':24,'b':100})
Traceback (most recent call last):
  File "<pyshell#157>", line 1, in <module>
    s.add({'a':24,'b':100})
TypeError: unhashable type: 'dict'
s.add([12,24,48)]
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
s.add([12,24,48])
Traceback (most recent call last):
  File "<pyshell#159>", line 1, in <module>
    s.add([12,24,48])
TypeError: unhashable type: 'list'
s.add({24,10,True})
Traceback (most recent call last):
  File "<pyshell#160>", line 1, in <module>
    s.add({24,10,True})
TypeError: unhashable type: 'set'
s.update(24)
Traceback (most recent call last):
  File "<pyshell#161>", line 1, in <module>
    s.update(24)
TypeError: 'int' object is not iterable
s.update((24,12))
s
{0.8, 'abcd', 12, 'a', (3+5j), 24, (12, 43)}
s.update([12,'a')]
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
s.update([12,'a'])
s
{0.8, 'abcd', 12, 'a', (3+5j), 24, (12, 43)}
s.update({'a':20,'b':10})
s
{0.8, 'b', 'abcd', 12, 'a', (3+5j), 24, (12, 43)}
s.update('abcd')
s
{0.8, 'b', 'c', 'abcd', 12, 'a', 'd', (3+5j), 24, (12, 43)}
s.update(3+9j)
Traceback (most recent call last):
  File "<pyshell#171>", line 1, in <module>
    s.update(3+9j)
TypeError: 'complex' object is not iterable
s.remove()
Traceback (most recent call last):
  File "<pyshell#172>", line 1, in <module>
    s.remove()
TypeError: set.remove() takes exactly one argument (0 given)
s.remove({'a':20,'b':10})
Traceback (most recent call last):
  File "<pyshell#173>", line 1, in <module>
    s.remove({'a':20,'b':10})
TypeError: unhashable type: 'dict'
s.remove('a','b')
Traceback (most recent call last):
  File "<pyshell#174>", line 1, in <module>
    s.remove('a','b')
TypeError: set.remove() takes exactly one argument (2 given)
s.remove('a')

s
{0.8, 'b', 'c', 'abcd', 12, 'd', (3+5j), 24, (12, 43)}
s.remove('b')
s
{0.8, 'c', 'abcd', 12, 'd', (3+5j), 24, (12, 43)}
s.remove('d')
s.remove(3+5j)
s
{0.8, 'c', 'abcd', 12, 24, (12, 43)}
s.remove((12,43))
s
{0.8, 'c', 'abcd', 12, 24}
s.discard()
Traceback (most recent call last):
  File "<pyshell#185>", line 1, in <module>
    s.discard()
TypeError: set.discard() takes exactly one argument (0 given)
s.discard(24)
s
{0.8, 'c', 'abcd', 12}
s.discard(12)
s
{0.8, 'c', 'abcd'}
s.discard('c')
s
{0.8, 'abcd'}
s.discard(0.8)
s
{'abcd'}
pop()
Traceback (most recent call last):
  File "<pyshell#194>", line 1, in <module>
    pop()
NameError: name 'pop' is not defined. Did you mean: 'pow'?
s.pop()
'abcd'
s.pop()
Traceback (most recent call last):
  File "<pyshell#196>", line 1, in <module>
    s.pop()
KeyError: 'pop from an empty set'
s.update(121)
Traceback (most recent call last):
  File "<pyshell#197>", line 1, in <module>
    s.update(121)
TypeError: 'int' object is not iterable
s.add(121)
>>> s
{121}
>>> s.update(34)
Traceback (most recent call last):
  File "<pyshell#200>", line 1, in <module>
    s.update(34)
TypeError: 'int' object is not iterable
>>> s.update('abcd')
>>> s
{'b', 'c', 'a', 'd', 121}
>>> s.pop()
'a'
>>> s.clear()
>>> s
set()
>>> a={2,5,7}
>>> b={12,24,48}
>>> a.union(b)
{48, 2, 5, 7, 24, 12}
>>> b.union(a)
{48, 2, 5, 7, 24, 12}
>>> a={12,24,48}
>>> b={12,3,4}
>>> a.union(b)
{48, 3, 4, 24, 12}
>>> b.union(a)
{48, 3, 4, 24, 12}
>>> a.intersection(b)
{12}
>>> a.difference(b)
{24, 48}
>>> b.diffrence(a)
Traceback (most recent call last):
  File "<pyshell#216>", line 1, in <module>
    b.diffrence(a)
AttributeError: 'set' object has no attribute 'diffrence'. Did you mean: 'difference'?
>>> b.difference(a)
{3, 4}
>>> max(a)
48
>>> min(b)
3
>>> sum(a)
84
>>> sum(b)
19
