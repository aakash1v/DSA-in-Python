def merge(arr,low,mid,high):
    left = arr[low:mid+1]
    right = arr[mid+1:high+1]

    i=j=0
    k=low
    while (i<len(left)and j<len(right)):
        if left[i] <right[j]:
            arr[k]=left[i]
            i+=1
            k+=1
        else:
            arr[k]=right[j]
            k+=1
            j+=1

    while (i<len(left)):
        arr[k]=left[i]
        k+=1
        i+=1
    
    while( j < len(right)):
        arr[k]=right[j]
        k+=1
        j+=1


def mergeSort(arr,l,r):
    if r>l:
        m = (l+r) //2
        mergeSort(arr,l,m)
        mergeSort(arr,m+1,r)
        merge(arr,l,m,r)

#Driver code
arr = [10, 5, 30, 15, 7]
print(*arr)
mergeSort(arr, 0, 4)
print(*arr)
