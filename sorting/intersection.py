
def intersection(a,b):
    m = len(a)
    n = len(b)

    for i in range(m):
        if i>0 and a[i] == a[i-1]:
            continue

        for j in range(n):
            if a[i] == b[j]:
                print(a[i],end=" ")
                break
    print()


def intersection(a,b):
    m = len(a)
    n = len(b)
    i =0
    j =0

    while i < m and j < n:
        if i > 0 and a[i] ==a[i-1]:
            i +=1
        if j > 0 and b[j] == b[j-1]:
            j +=1
        if a[i] < b[j]:
            i +=1
        elif a[i] > b[j]:
            j +=1
        else:
            print(a[i])
            i +=1
            j+=1

#Driver code
a = [10,10,15,20,30]
b = [10,30]
intersection(a,b)
