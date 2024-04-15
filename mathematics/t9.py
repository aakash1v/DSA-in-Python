# All Divisor of a number..
def printDivisor(n):
    i =1
    while (i<=n):
        if (n%i ==0):
            print(i)
        i+=1

# Efficient way..
def printDivisor(n):
    i =1
    while(i*i<n):
        if n%i==0:
            if n//i == i:
                print(i,end=' ')
            else:
                print(i,n//i,end=' ')
        
        i+=1


#Driver code
printDivisor(40)