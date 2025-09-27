def Even(num):
    if num%2==0:
        return 1
print(list(filter(Even,range(1,100))))
