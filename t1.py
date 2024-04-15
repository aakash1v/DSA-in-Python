'''Given a number n, find the sum of first natural numbers.
'''
def findSum(n):
    sum =0
    for i in range(1,n+1):
        sum +=i
    return sum


#Driver Code
n =5
print(findSum(n))