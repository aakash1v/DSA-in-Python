'first occurance of n'
def firstIndex(arr,x,low,high):
    if low>high:
        return -1
    
    mid = low + (high-low)//2

    if arr[mid]==x:
        if mid==0 or arr[mid]!=arr[mid-1]:
            return mid
        else:
            return firstIndex(arr,x,low,mid-1)
    
    elif arr[mid] >x:
        return firstIndex(arr,x,low,mid-1)
    
    else:
        return firstIndex(arr,x,mid+1,high)
    

'last occurance of n'
def lastIndex(arr,x,low,high):
    if low>high:
        return -1
    
    mid = low + (high-low)//2

    if arr[mid]==x:
        if arr[mid]!=arr[mid+1] or mid ==len(arr)-1:
            return mid
        else:
            return lastIndex(arr,x,mid+1,high)
    
    elif arr[mid] >x:
        return lastIndex(arr,x,low,mid-1)
    
    else:
        return lastIndex(arr,x,mid+1,high)
    
def CountOccurance(arr,x):
    n= len(arr)-1
    return lastIndex(arr,x,0,n) -  firstIndex(arr,x,0,n) +1
#driver code..
arr=[1,4,4,4,4,6,7,7,9,12,12,100]

x = 4
# result = lastIndex(arr,x,0,len(arr)-1)
result = CountOccurance(arr,x)
print(result)

    
