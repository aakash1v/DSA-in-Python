'''Function to print union of two sorted array...
'''
def Union(a,b,n,m) -> list:
    result = [0 for _ in range(m+n)]

    index,left,right = 0,0,0
    while left <n and right <m:
        if (a[left]<b[right]):
            if (index !=0 and a[left]==result[index-1]):
                left+=1
            else:
                result[index]=a[left]
                left +=1
                index +=1
        else:
            if (index!=0 and b[right]==result[index-1]):
                right +=1
            else:
                result[index]=b[right]
                right +=1
                index +=1
    #for left element of the list..
    while (left<n):
        if (left!=0 and a[left] ==result[index-1]):
            left +=1
        else:
            result[index] = a[left]
            index +=1
            left +=1

    while (right<m):
        if (right!=0 and b[right] ==result[index-1]):
            right +=1
        else:
            result[index] = b[right]
            index +=1
            right +=1
    
    return result[:index]
#Driver code
a= [1, 12, 14,14]
b = [2,3,4,5,100,101]
n = len(a)
m = len(b)
result = Union(a,b,n,m)
print(result)
