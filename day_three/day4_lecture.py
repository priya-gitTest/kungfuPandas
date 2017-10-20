
#Takes in a number and returns the square of that number
def square(number):
	squared=number*number
	return squared


number = float( input("Enter a number"))

print( square(number) )


class Car:
	name = str()
	model = ""
	category = ""
	color = ""
	year = int()
	milage = 0

	def __init__(self, make, model, category, color, year, milage):
		self.name = make
		self.model = model
		self.category = category
		self.color = color
		self.year = year
		self.milage = milage

	def setMake(self, new_make):
		self.name = new_make

	def getMake(self):
		return self.name

	def setMilage(self, new_milage):
		self.milage = new_milage

	def getMilage(self):
		return self.milage

	def addMilage(self, miles_total):
		self.milage = self.milage + miles_total



my_car = Car("Toyota","Carolla","4 Door Sedan","Red", 2010, 0)

car2 = Car("Honda","Cord","Sedan","Silver",2016,3000)

my_car.addMilage(1000)

my_car.setMake("Nissan")

print( my_car.getMake() )