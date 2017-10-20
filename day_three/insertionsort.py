unsorted=[4,9,6,6,8,3,7,7,64,78,24]

for x in range(0,len(unsorted)):

	for y in range(x-1,-1,-1):

		if unsorted[x] > unsorted[y]:
			temp_item = unsorted.pop(x)
			unsorted.insert(y+1, temp_item)
			break
		elif y == 0 and unsorted[x] <= unsorted[y]:
			temp_item = unsorted.pop(x)
			unsorted.insert(0, temp_item)
			break

	print(unsorted)
	print("-------------------")