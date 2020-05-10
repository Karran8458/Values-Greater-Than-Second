def values_greater_than_second(arr):
	arr2 = [ ]
	if len(arr) < 3:
		return false
	for x in range(0,len(arr),1):
		if arr[x] > arr[1]:
		arr2.append(arr[x])
	print(len(arr2))
	return arr2
