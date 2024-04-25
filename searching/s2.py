'''Index of first occurance and last occurance in a sorted array
'''
def findFirstAndLast(arr,x):

    first=-1
    last=-1
    for i in range(len(arr)):
        if arr[i]==x:
            if first ==-1:
                first = i
            last=i

    if first!=-1:
        print("First index is ",first," and \nlast Index is ",last)
        

#Driver code...
arr=[1,4,4,4,4,6,7,7,9,12,12,100]
print(arr)
x = int(input('Enter the value of x from the array'))
findFirstAndLast(arr,x)
