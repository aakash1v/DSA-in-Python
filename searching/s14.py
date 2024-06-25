'''Function to print intersection of two sorted array...
'''
def Intersection(a,b,n,m) -> list:
    result = [0 for _ in range(m+n)]

    index,left,right = 0,0,0
    while left <n and right <m:
        
        if a[left]<b[right]:
            left +=1
        
        elif a[left]>b[right]:
            right +=1

        else:
            if index ==0 or  result[index] != result[index-1]:
                result[index]=a[left]
                index +=1
                left +=1
                right +=1
            else:
                left +=1
                right +=1



    
    return result[:index]
#Driver code
a= [3,6,9,12]
b = [2,4    ,6,8,10,12]
n = len(a)
m = len(b)
result = Intersection(a,b,n,m)
print(result)