
def merge(a,b):
    m = len(a)
    n = len(b)
    res = []

    i =0
    j = 0
    while i<m and j<n:
        if a[i] < b[j]:
            res.append(a[i])
            i = i+1
        else:
            res.append(b[j])
            j = j+1
    while i<m:
        res.append(a[i])
        i +=1

    while j <n:
        res.append(b[j])
        j +=1

    return res

# Driver code
list1 = [2,5,7,9]
list2 = [3,6,8,11]

sorted_list = merge(list1,list2)
print('New sorted list is ',*sorted_list)
