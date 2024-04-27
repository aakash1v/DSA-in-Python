'''INsertion Sort..'''

def insertionSort(arr:int):
    for i in range(1,len(arr)):
        x=arr[i]
        j = i-1

        while(j >=0 and x<arr[j]):
            arr[j+1]= arr[j]
            j = j-1
        arr[j+1]=x
        # print(arr[j+1],arr[j],x)
        # print(arr)
    
#Driver code
arr = [10,5,40,60,10,30]
insertionSort(arr)
print(arr)

