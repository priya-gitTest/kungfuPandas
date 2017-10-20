
class View:

	def __init__(self):
		self

	def printOut(self, output):
		print(output)

	def takeInput(self, output):
		user_input = input(output)
		return user_input

	#Menu items will be a list of strings to be output in menu format
	def showMenu(self, menu_items):
		counter = 1
		for item in menu_items:
			print( str(counter)+". "+item )
			counter = counter + 1

	#Takes in a list of Tuples (Data) and a list of Strings(Key)
	def showData(self, data, key):
		key_string = ""
		for item in key:
			key_string = key_string + item + "  |  "
		key_string = key_string[0:-4]
		print(key_string)
		
		for row in data:
			data_string = ""
			for item in row:
				data_string = data_string + str(item) + "  |  "
			data_string = data_string[0:-4]
			print(data_string)
