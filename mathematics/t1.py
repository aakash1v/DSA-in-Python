'''Given a number n, find the sum of first natural numbers.
'''
def findSum(n):
    sum =0
    for i in range(1,n+1):
        sum +=i
    return sum

# efficient program to find sum 
def findSum(n):
    return n*(n+1)//2


#avoid overflow if the result is going to be
# within limits.
def findSum(n):
    if n%2==0:
        return n//2 * (n+1)
    else:
        return ((n+1)//2 )*n


#Driver Code
n =5
print(findSum(n))