def countFreq(arr,n):
	
	mp = {}

	for i in range(n):
		if arr[i] not in mp:
			mp[arr[i]] = 0
		mp [arr[i]] +=1

	
	for i in range(n):
		if (mp[arr[i]]  !=-1):
			print(arr[i],mp[arr[i]])
		mp[arr[i]]  = -1
	
#Driver code

arr = [10,20,20,10,10,20,5,20]
n = len(arr)
countFreq(arr,n)
