# All Prime Factors..
import math

def primeFactor(n):
    while n%2 ==0:
        print(2)
        n = n/2

    for i in range(3,int(math.sqrt(n)+1),2):
        while n%i==0 :
            print(i)
            n = n/i

    if n>2:
        print(n)


# Driver code 
primeFactor(22)