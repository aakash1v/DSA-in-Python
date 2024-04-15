'''Given an integral number N. The task is to find the count of digits present in this number.
'''
import math

def countDigits(N):
    if N==0:
        return 0
    
    digit =0
    while(N>0):
        N=N//10
        digit +=1
    return digit

def countDigits(N):
    if N==0:
        return 0
    
    return math.floor(math.log10(N)+1) 

#Driver code
print(countDigits(1024))