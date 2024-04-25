'''count onces in arr which is sorted in non- increasing order
'''

def countOnes(arr,low,high):
    if high >=low:
        mid = low + (high-low)//2
    
    if ((mid == high or arr[mid+1]==0) and arr[mid]==1):
        return mid +1
    if arr[mid]==1:
        return countOnes(arr,(mid+1),high)
    return countOnes(arr,low,mid-1)

#Driver code
arr=[1,1,1,1,1,0,0,0,0]
print('Count of onces in given array is',countOnes(arr,0,len(arr)-1) )

'''count onces in arr which is sorted order '''
def countOnces(arr,n):
    low=0
    high =n-1
    while(low<=high):
        mid =(low+high)//2

        if((mid==n-1 or arr[mid+1]==0) and arr[mid]==1):
            return mid+1
        

