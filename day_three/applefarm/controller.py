from model import Model
from view import View

my_model = Model()

my_view = View()

def showsEmployees():
	output = my_model.selectAllEmployees()
	my_view.showData(output, ["ID","Name","Hours","$/hour"])
	return True

def showsTrees():
	output = my_model.selectAllTrees()
	my_view.showData(output, ["ID","Ripe Apples","Rotten Apples","Price per Apple","Type of Apple"])
	return True

def hireEmployee():
	employee_name = my_view.takeInput("What is the new employee's name? ")

	running_pay = True
	while running_pay == True:
		pay_per_hour = my_view.takeInput("How much will they be paid per hour? ")
		try:
			pay_per_hour = float(pay_per_hour)
			running_pay = False
		except ValueError:
			my_view.printOut("Invalid entry, try again")

	my_model.insertEmployee( [employee_name, 0, pay_per_hour] )

	return True

def fireEmployee():
	running_id = True
	all_employees = my_model.selectAllEmployees()
	all_employees_id = []
	for item in all_employees:
		all_employees_id.append( item[0] )

	while running_id == True:
		employee_id = my_view.takeInput("What employee id do you want to fire? ")
		try:
			employee_id = int(employee_id)
			if employee_id in all_employees_id:
				running_id = False
			else:
				my_view.printOut("Error that Id is not in the system")
		except ValueError:
			my_view.printOut("Invalid Entry, try again")

	# print(employee_id)
	# print(type(employee_id))

	my_model.deleteEmployee(employee_id)


	return True

def buyTree():
	type_of_apple = my_view.takeInput("What type of apple tree do you want? ")
	
	running_apple = True
	while running_apple == True:
		price_per_apple = my_view.takeInput("How much are these apples worth? ")
		try:
			price_per_apple = float(price_per_apple)
			running_apple = False
		except ValueError:
			my_view.printOut("Invalid entry, try again.")


	running_trees = True
	while running_trees == True:
		number_of_trees = my_view.takeInput("How many of these trees do you want? ")
		try:
			number_of_trees = int(number_of_trees)
			running_trees = False
		except ValueError:
			my_view.printOut("Invalid entry, try again.")

	for x in range(number_of_trees):
		my_model.insertTree( [ 0, 0, price_per_apple, type_of_apple ] )
	return True

def harvestTree():
	running_id = True

	all_trees = my_model.selectAllTrees()
	all_trees_id = []
	for item in all_trees:
		all_trees_id.append( item[0] )

	while running_id == True:
		tree_id = my_view.takeInput("Enter tree Id to Harvest: ")
		try:
			tree_id = int(tree_id)
			if tree_id in all_trees_id:
				running_id = False
			else:
				my_view.printOut("ID not found try again")
		except ValueError:
			my_view.printOut("Invalid entry, try again.")

	single_tree = my_model.selectOneTree(tree_id)

	updated_tree = [ 0, 0, single_tree[3], single_tree[4], tree_id ]

	my_model.updateTree(updated_tree)

	my_view.printOut("Harvested: "+str(single_tree[1])+"\nTotal Value: "+ str(single_tree[1]*single_tree[3]) )

	return True

def growTree():
	return True

def exit():
	return False

# my_model.createTables()

# my_model.insertEmployee( ["Cletus", 40, 15.00] )

# output = my_model.selectAllEmployees()

# my_view.printOut(output)

# output = my_view.takeInput("How many Trees? ")

# my_view.printOut(output)

running = True

while running == True:
	my_view.showMenu( ["Show Employees", "Hire Employee", "Fire Employee", "Show Trees", "Buy Tree", "Harvest Tree", "Grow Tree", "Exit"] )
	user_input = my_view.takeInput("Choose a menu item: ")

	potenial_inputs = ["1","2","3","4","5","6","7","8"]

	if user_input in potenial_inputs:
		
		function_dictionary = { "1":showsEmployees,"2":hireEmployee,"3":fireEmployee,"4":showsTrees,"5":buyTree,"6":harvestTree,"7":growTree,"8":exit }
		
		running = function_dictionary[user_input]()


	else:
		my_view.printOut("\nInvalid entry. Try again. \n")




my_model.closeConnection()

