"""merge sort alogrithm """

def merge(arr,low,mid,high):

    left = arr[low:mid+1]
    right = arr[mid+1:high+1]

    i = 0
    j = 0

    k = low

    while i <len(left) and j <len(right):

        if left[i] <= right[j]:
            arr[k] = left[i]
            k = k+1
            i = i+1

        else:
            arr[k] = right[j]
            k = k+1
            j = j+1

    while i <len(left):
        arr[k] = left[i]
        k +=1
        i +=1

    while j <len(right):
        arr[k] = right[j]
        k +=1 
        j +=1
    
def mergesort(arr,l,r):
    if r>l:
        m = (l+r)//2

        mergesort(arr,l,m)
        mergesort(arr,m+1,r)
        merge(arr,l,m,r)


#Driver code
arr = [10,4,3,22,7,9]

print("Array before merge sort :",*arr)

mergesort(arr,0,5)
print("Array after merge sort :",*arr)
