def binary(num,place=1,binary=0):
    while num!=0:
        ld=num%2
        binary=binary+ld*place
        num//=2
        place*=10
    return binary
num=8
print(binary(num))
        
