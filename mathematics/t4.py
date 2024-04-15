# Factorial of a Number

def factorial(n):
    if n==0:
        return 1
    return n* factorial(n-1)

def factorial(n):
    if (n<0 or n in [0,1]):
        return 1
    
    result=1
    while(n>0):
        result *=n
        n=n-1
    return result

#Driver code
num =5
print(factorial(num))