
def union(a,b):
    n = len(a)
    m = len(b)
    i =0 
    j=0

    while i< m and j<n:
        if i>0 and  a[i] == a[i-1]:
            i +=1
        if j>0 and b[j] == b[j-1]:
            j +=1
        if a[i] < b[j]:
            print(a[i],end=" ")
            i +=1
        elif a[i] > b[j]:
            print(b[j],end=" ")
            j +=1
        else:
            print(a[i],end=" ")
            i +=1
            j +=1

    while i<m :
        if i> 0 and a[i] == a[i-1]:
            i +=1
        print(a[i],end=" ")
        i +=1
    while j<n:
        if j>=0 and b[j] == b[j-1]:
            j +=1
        print(b[j],end=" ")
        j +=1
    print()


# Driver code
arr = [10,20,25,30,40]
arr2 = [10,15,40,60,80]

union(arr,arr2)
