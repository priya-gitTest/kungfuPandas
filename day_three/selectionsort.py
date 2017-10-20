unsorted=[4,9,6,6,8,3,7,7,64,78,24]
sorted_list = []


while len(unsorted) > 0:
	lowest = min(unsorted)
	sorted_list.append(lowest)
	unsorted.remove(lowest)

	# lowest_value = unsorted[0]
	# lowest_index = 0
	# for i in range(0, len(unsorted) ):
	# 	if lowest_value > unsorted[i]:
	# 		lowest_value = unsorted[i]
	# 		lowest_index = i

	# sorted_list.append( unsorted.pop(lowest_index) )

	print(unsorted)
	print(sorted_list)
	print("----------------------")