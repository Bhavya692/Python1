def Reverse(num,length):
    if num==0:
        return 0
    return (num%10)*(10**length)+Reverse(num//10,length-1)
num=543
print(Reverse(num,(len(str(num))-1)))
