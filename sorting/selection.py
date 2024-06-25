""" This is the program for selection sort"""

def selection(l):
    n = len(l)
    for i in range(n-1):
        min = i
        for j in range(i+1,n):
            if l[min] > l[j]:
                min = j
        l[min],l[i]  = l[i],l[min]

#Driver code
arr = [3,11,5,7]
print("Arr before selection sort :",*arr)
selection(arr)
print("Arr after selection sort :",*arr)
