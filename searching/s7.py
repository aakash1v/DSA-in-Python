# Bubble sort 
def bubble(arr:list,n:int) ->list:
    for i in range(n-1):
        change = False
        for j in range(n-1-i):
            print(arr[j],arr[j+1],arr[j]>arr[j+1])
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                change = True
        print(arr)
        if change ==False:
            break
    return arr

#Driver code
arr=[20,30,10,100,0,-2]
n = 6
print(arr)
bubble(arr,n)
print('The sorted array is -- ',arr)
