def reverse(num,length):
    if num==0:
        return 0
    return (num%10)*(10**length)+reverse(num//10,length-1)

num=101
print(reverse(num) if reverse(num,len(str(num))-1) == num)
