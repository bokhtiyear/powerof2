def powerOfTwo(n):
    if(n == 0):
        return 0
    elif((n & (~(n - 1)))== n):
        return 1
    return 0
num = int(input("Enter a number"))
if(powerOfTwo(num)):
    print("This number is power of two")
    
    
else:
    print("The number is not power of two")    