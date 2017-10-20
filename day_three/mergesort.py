def mergeSort(unsorted):
	list_of_list = []

	for item in unsorted:
		list_of_list.append( [item] )

	while len(list_of_list) > 1:
		temp_list = []
		for x in range(0, len(list_of_list), 2):
			if x+1 >= len(list_of_list):
				temp_list.append(list_of_list[x])
			else:
				list1 = list_of_list[x]
				list2 = list_of_list[x+1]
				new_list = []

				while len(list1) > 0 or len(list2) > 0:
					if len(list1) == 0:
						new_list.append( list2.pop(0) )

					elif len(list2) == 0:
						new_list.append( list1.pop(0) )

					else:
						if list1[0] < list2[0]:
							new_list.append( list1.pop(0) )
						else:
							new_list.append( list2.pop(0) )

				temp_list.append(new_list)
		list_of_list = temp_list

	return list_of_list

unsorted=[4,9,6,6,8,3,7,7,64,78,24]
print(mergeSort(unsorted))