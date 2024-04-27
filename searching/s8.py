def selectionsort(arr):
    n= len(arr)
    for i in range(n-1):
        min_ind=i
        for j in range(i+1,n):
            # print(arr[j],arr[min_ind],arr[j]<arr[min_ind] )
            if arr[j]<arr[min_ind]:
                min_ind = j
        arr[i],arr[min_ind]= arr[min_ind],arr[i]
        # print('--------',arr)


#Driver code
arr = [64,25,12,22,11]
selectionsort(arr)
print('Sorted array (selection sort)',arr)
