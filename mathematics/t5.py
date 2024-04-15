# Trailing Zeros in Factorial

def findTrailingZeros(n):
    count =0
    i=5
    while(n/i >= 1):
        count += int(n/i)
        i *=5

    return count

#driver code
print(findTrailingZeros(5))


