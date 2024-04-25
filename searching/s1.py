def bSearch(l,x):
    low=0
    high=len(l)-1
    while low <=high:
        mid = (low+high)//2
        if l[mid]==x:
            return mid
        elif l[mid]<x:
            low = mid+1
        else:
            high = mid-1
    return -1

def bSearch(arr,l,r,x):

    if l >r:
        return -1
    
    mid=(l+r)//2

    if arr[mid] ==x:
        return mid
    elif arr[mid] >x:
        r=mid-1
        bSearch(arr,l,r,x)
    else:
        l=mid+1
        bSearch(arr,l,r,x)
    return -1

#Drivers code..
arr=[1,23,11,100,3,201,0]
ar= sorted(arr)
x =111
print(bSearch(arr,0,len(arr)-1,x))


    
