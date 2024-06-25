""" Program for insertion sort """

def insertion(l):
    n = len(l)
    for i in range(1,n):
        x = l[i]
        j = i-1

        while j>=0 and x<l[j]:
            l[j+1] = l[j]
            j = j-1
        l[j+1] = x #putting x at it's right position..

# Driver code
arr = [10, 2,3,5,20,7]
print("Array before insertion sort :",*arr)
insertion(arr)
print("Array after insertion sort :",*arr)
