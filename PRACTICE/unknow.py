
def Sample(val):
    print(val)
num=10
Sample(num)

def Sample(val):
    print(val)
Sample(50)

def Sample(val):
    print(val)
Sample(50)

def Sample(num):
    print(num)
num=10
Sample(num)
print('                        ')

def Sample(num):
    print(num)

num=10
Sample(num)
print('                         ')
    
def Sample(num):
    print(num)
    num=num+5
    print(num)
num=10
Sample(num)
print(num)

print('                    ')

def Sample(num):
    print(f'Local value={num}')
    num=num+5
    print(f'Local value={num}')
num=10
Sample(num)
print(f'Global value={num}')
