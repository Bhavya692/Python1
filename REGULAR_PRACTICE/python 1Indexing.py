Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s='python developer'
len(s)
16
s
'python developer'
len(s)
16
s[0]
'p'
s[6] = '@'
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    s[6] = '@'
TypeError: 'str' object does not support item assignment
s='abcd'
s[3][1]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    s[3][1]
IndexError: string index out of range
s[1][3]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    s[1][3]
IndexError: string index out of range
s[2][0]
'c'
s[6][0]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    s[6][0]
IndexError: string index out of range
s='python developer'
len(s)
16
s('p')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    s('p')
TypeError: 'str' object is not callable
s['p']
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    s['p']
TypeError: string indices must be integers, not 'str'
s[12]
'o'
s[14][14]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    s[14][14]
IndexError: string index out of range
s[14][1]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    s[14][1]
IndexError: string index out of range
s[1][14]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    s[1][14]
IndexError: string index out of range
s[14][0]
'e'
s[14][2]
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    s[14][2]
IndexError: string index out of range
s[16][0]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    s[16][0]
IndexError: string index out of range
s[15][0]
'r'
L=[24,3+9j,'abcd',[1,2,3],(12,24,48),True]
len(L)
6
L[0][5]
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    L[0][5]
TypeError: 'int' object is not subscriptable
L[2][3]
'd'
l[3][3]
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    l[3][3]
NameError: name 'l' is not defined. Did you mean: 'L'?
L[3][3]
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    L[3][3]
IndexError: list index out of range
L[3][2]
3
L[4][2]
48
L[4][2] = 3
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    L[4][2] = 3
TypeError: 'tuple' object does not support item assignment
L[4][2] = 's'
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    L[4][2] = 's'
TypeError: 'tuple' object does not support item assignment
L[3][2] = 'e'
L
[24, (3+9j), 'abcd', [1, 2, 'e'], (12, 24, 48), True]
L[3][2] = 3+99j
L
[24, (3+9j), 'abcd', [1, 2, (3+99j)], (12, 24, 48), True]
L[3][2] = True
L
[24, (3+9j), 'abcd', [1, 2, True], (12, 24, 48), True]
L[2][1] = 'c'
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    L[2][1] = 'c'
TypeError: 'str' object does not support item assignment
L[5][0] = 24
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    L[5][0] = 24
TypeError: 'bool' object does not support item assignment
L[5][0] = False
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    L[5][0] = False
TypeError: 'bool' object does not support item assignment
t=(244,(1,2,'c'),[12,24,46],3+9j,False,'abcd')
t[2][3]
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    t[2][3]
IndexError: list index out of range
t[2][0]
12
t[3][2]
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    t[3][2]
TypeError: 'complex' object is not subscriptable
t[4][1]
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    t[4][1]
TypeError: 'bool' object is not subscriptable
t[0][0]
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    t[0][0]
TypeError: 'int' object is not subscriptable
len(t)
6
t[5][1]
'b'
t=(0.5,0.5+4j,12,True,'abcd',[12,24,45],(1,1,'a'),{'a':20,'b':40},{12,'abc',(23,34,56)})
len(t)
9
t[8][0]
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    t[8][0]
TypeError: 'set' object is not subscriptable
t[7][0]
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    t[7][0]
KeyError: 0
t[7]['a']
20
t[7]['a'] = 'c'
t
(0.5, (0.5+4j), 12, True, 'abcd', [12, 24, 45], (1, 1, 'a'), {'a': 'c', 'b': 40}, {'abc', 12, (23, 34, 56)})
t[7]['a'] = ['a']
t
(0.5, (0.5+4j), 12, True, 'abcd', [12, 24, 45], (1, 1, 'a'), {'a': ['a'], 'b': 40}, {'abc', 12, (23, 34, 56)})
t[7]['a'] = 'a'
t
(0.5, (0.5+4j), 12, True, 'abcd', [12, 24, 45], (1, 1, 'a'), {'a': 'a', 'b': 40}, {'abc', 12, (23, 34, 56)})
t[7]['a'] = 5+9j
t
(0.5, (0.5+4j), 12, True, 'abcd', [12, 24, 45], (1, 1, 'a'), {'a': (5+9j), 'b': 40}, {'abc', 12, (23, 34, 56)})
t[7]['a'] = {'a':20,'b':40}
t
(0.5, (0.5+4j), 12, True, 'abcd', [12, 24, 45], (1, 1, 'a'), {'a': {'a': 20, 'b': 40}, 'b': 40}, {'abc', 12, (23, 34, 56)})
t[7]['a']['b'] = {'a':20,'b':40}
t
(0.5, (0.5+4j), 12, True, 'abcd', [12, 24, 45], (1, 1, 'a'), {'a': {'a': 20, 'b': {'a': 20, 'b': 40}}, 'b': 40}, {'abc', 12, (23, 34, 56)})
set()
set()
s={'abcdef',(a,b,c),[12,'a',3+77j],{'a':14,'b':23}}
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    s={'abcdef',(a,b,c),[12,'a',3+77j],{'a':14,'b':23}}
NameError: name 'a' is not defined
s={'abcdef',(a,b,c),[12,'a',3+77j],{'a':14,'b':23}}
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    s={'abcdef',(a,b,c),[12,'a',3+77j],{'a':14,'b':23}}
NameError: name 'a' is not defined
s={'abcdef',(a,b,c),[12,23,3+77j],{'a':14,'b':23}}
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    s={'abcdef',(a,b,c),[12,23,3+77j],{'a':14,'b':23}}
NameError: name 'a' is not defined
s={'abc',4+33j,(a1,b4),[22,33,44]}
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    s={'abc',4+33j,(a1,b4),[22,33,44]}
NameError: name 'a1' is not defined
s={'abc',4+33j,[22,33,44]}
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    s={'abc',4+33j,[22,33,44]}
TypeError: unhashable type: 'list'
s={'abc',4+33j}
\
s
{'abc', (4+33j)}
s={{'a':24,'b':44},'def',{24,99,88}}
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    s={{'a':24,'b':44},'def',{24,99,88}}
TypeError: unhashable type: 'dict'
s={'def',{24,99,88}}
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    s={'def',{24,99,88}}
TypeError: unhashable type: 'set'
s={'def',24,88+9j,0.8,True}
s
{0.8, True, (88+9j), 'def', 24}
d={'s':44+9j,'racd':ajjj}
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    d={'s':44+9j,'racd':ajjj}
NameError: name 'ajjj' is not defined
d={'s':44+9j,3:ajjj}
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    d={'s':44+9j,3:ajjj}
NameError: name 'ajjj' is not defined
d={'s':44+9j,[23,56,99]:(12,'a',24)}
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    d={'s':44+9j,[23,56,99]:(12,'a',24)}
TypeError: unhashable type: 'list'
d={'s':44+9j,(12,'a',24):[23,56,99]}
d
{'s': (44+9j), (12, 'a', 24): [23, 56, 99]}
d[0][1]
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    d[0][1]
KeyError: 0
d[0]['s']
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    d[0]['s']
KeyError: 0
d['s']
(44+9j)
d[(12,'a',24)]
[23, 56, 99]
d[(12,'a',24)] = 45
d
{'s': (44+9j), (12, 'a', 24): 45}
d[(12,'a',24)] = (12,'a',24)
dd
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    dd
NameError: name 'dd' is not defined. Did you mean: 'd'?
d
{'s': (44+9j), (12, 'a', 24): (12, 'a', 24)}
d[(12,'a',24)] = {'b':67,'b':98}
d
{'s': (44+9j), (12, 'a', 24): {'b': 98}}
d(12,'a',24) = [78,99,00]
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?
d[(12,'a',24)] = [78,99,00]
d
{'s': (44+9j), (12, 'a', 24): [78, 99, 0]}
d[(12,'a',24)] = (48,99,77)
d
{'s': (44+9j), (12, 'a', 24): (48, 99, 77)}
len(d)
2
d[0][1]
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    d[0][1]
KeyError: 0
d[1][(12,'a',24)]
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    d[1][(12,'a',24)]
KeyError: 1
d[(12,'a',24)][1]
99
d[(12,'a',24)][4]
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    d[(12,'a',24)][4]
IndexError: tuple index out of range
d[(12,'a',24)][0]
48
d[(12,'a',24)][2]
77
d['s'][0]
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    d['s'][0]
TypeError: 'complex' object is not subscriptable
d['s']
(44+9j)
d.real('s')
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    d.real('s')
AttributeError: 'dict' object has no attribute 'real'
s.real
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    s.real
AttributeError: 'set' object has no attribute 'real'
d.real
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    d.real
AttributeError: 'dict' object has no attribute 'real'
d['s']
(44+9j)
s='i am python developer'
len(s)
21
s[0]
'i'
D={0:['RCB','PBS',{5:['CSK','MI']},'DC','LSG',{1:('GT','RR'}]}
   
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
D={0:['RCB','PBS',{5:['CSK','MI']},'DC','LSG',{1:('GT','RR']}
      
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
D={0:['RCB','PBS',{5:['CSK','MI']},'DC','LSG',{1:('GT','RR'}]}
   
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
D={0:['RCB','PBS',{5:['CSK','MI']},'DC','LSG',{1:('GT','RR')}]}
   
D
   
{0: ['RCB', 'PBS', {5: ['CSK', 'MI']}, 'DC', 'LSG', {1: ('GT', 'RR')}]}
len(D)
   
1
D[0]
   
['RCB', 'PBS', {5: ['CSK', 'MI']}, 'DC', 'LSG', {1: ('GT', 'RR')}]
D[0][0]
   
'RCB'
D[0][0][0]
   
'R'
D[0][0][1]
   
'C'
D[0][0][2]
   
'B'
D[0][0][3]
   
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    D[0][0][3]
IndexError: string index out of range
D[0][1]
   
'PBS'
D[0][1][0]
   
'P'
D[0][1][1]
   
'B'
D[0][1][2]
   
'S'
D[0][2]
   
{5: ['CSK', 'MI']}
D[0][2][5]
   
['CSK', 'MI']
D[0][2][5][0]
   
'CSK'
D[0][2][5][0][0]
   
'C'
D[0][2][5][0][1]
   
'S'
D[0][2][5][0][1\2]
   
SyntaxError: unexpected character after line continuation character
D[0][2][5][0][2]
   
'K'
D[0][2][5][1]
   
'MI'
D[0][2][5][1][0]
   
'M'
D[0][2][5][1][1]
   
'I'
D[0][3]
   
'DC'
D[0][3][0]
   
'D'
D[0][3][1]
   
'C'

D[0][4]
   
'LSG'
D[0][4][0]
   
'L'
D[0][4][1]
   
'S'
D[0][4][2]
   
'G'
D[0][5]
   
{1: ('GT', 'RR')}
D[0][5][1]
   
('GT', 'RR')
D[0][5][1][0]
   
'GT'
D[0][5][1][1]
   
'RR'
D[0][5][1][0][0]
   
'G'
D[0][5][1][0][1]
   
'T'
D[0][5][1][1][0]
   
'R'
D[0][5][1][1][1]
   
'R'
D[0][6]
   
Traceback (most recent call last):
  File "<pyshell#164>", line 1, in <module>
    D[0][6]
IndexError: list index out of range
D[-1]
   
Traceback (most recent call last):
  File "<pyshell#165>", line 1, in <module>
    D[-1]
KeyError: -1
D[-1][1]
   
Traceback (most recent call last):
  File "<pyshell#166>", line 1, in <module>
    D[-1][1]
KeyError: -1
d[-1][1][-1]
   
Traceback (most recent call last):
  File "<pyshell#167>", line 1, in <module>
    d[-1][1][-1]
KeyError: -1
D[0][-1]
   
{1: ('GT', 'RR')}
D[0][-1][1]
   
('GT', 'RR')
D[0][-1][1][-1]
   
'RR'
D[0][-1][1][-2]
   
'GT'
D[0][-1][1][-2][-3]
   
Traceback (most recent call last):
  File "<pyshell#172>", line 1, in <module>
    D[0][-1][1][-2][-3]
IndexError: string index out of range
D[0][-1][1][-2][-2]
   
'G'
D[0][-1][1][-2][-1]
   
'T'
D[0][-1][1][-1][-2]
   
'R'
D[0][-1][1][-1][-1]
   
'R'
D[0][-2]
   
'LSG'
D[0][-2][-3]
   
'L'
D[0][-2][-2]
   
'S'
D[0][-2][-1]
   
'G'
D[0][-3]
   
'DC'
D[0][-3][-3]
   
Traceback (most recent call last):
  File "<pyshell#182>", line 1, in <module>
    D[0][-3][-3]
IndexError: string index out of range
D[0][-3][-2]
   
'D'
D[0][-3][-1]
   
'C'
D[0][-4]
   
{5: ['CSK', 'MI']}
D[0][-4][5]
   
['CSK', 'MI']
D[0][-4][5][-2]
   
'CSK'
D[0][-4][5][-2][-3]
   
'C'
D[0][-4][5][-2][-2]
   
'S'
>>> D[0][-4][5][-2][-1]
...    
'K'
>>> D[0][-4][5][-1]
...    
'MI'
>>> D[0][-4][5][-1][-2]
...    
'M'
>>> D[0][-4][5][-1][-1]
...    
'I'
>>> D[0][-5]
...    
'PBS'
>>> D[0][-5][-3]
...    
'P'
>>> D[0][-5][-2]
...    
'B'
>>> D[0][-5][-1]
...    
'S'
>>> D[0][-6]
...    
'RCB'
>>> D[0][-6][-3]
...    
'R'
>>> D[0][-6][-2]
...    
'C'
>>> D[0][-6][-1]
...    
'B'
>>> D[0][-1]
...    
{1: ('GT', 'RR')}
>>> D[0][-6]
...    
'RCB'
>>> D[0][1]
...    
'PBS'
