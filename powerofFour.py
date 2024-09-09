def powerofFour(n):
    if n<= 0:
        return False
    if (n & (n -1 )) != 0:
        return False
    count = 0
    
    while(n>1):
        n>>=1
        count +=1
    return count % 2 == 0        
       
        
num = int(input("Enter a number"))
if(powerofFour(num)):
    print("This number is power of four")
    
    
else:
    print("The number is not power of four")                   