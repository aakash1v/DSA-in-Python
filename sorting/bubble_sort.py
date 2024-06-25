""" This is bubble sort algorithm"""

def bubble(l):
    n = len(l)

    for i in range(n-1):
        for j in range(n-i-1):
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]


#Driver code..

arr = [2,10,8,7]
print("array before sorting ",*arr)
bubble(arr)
print("array after sorting :",*arr)
