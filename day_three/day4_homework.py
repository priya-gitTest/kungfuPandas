import math

class SpaceShip:
	speed = int()
	distance_to_target = int()

	def __init__(self, speed, distance):
		self.speed = speed
		self.distance_to_target = distance

	def __init__(self,distance):
		self.distance_to_target = distance

	def setSpeed(self, new_speed):
		self.speed = new_speed

	def getSpeed(self):
		return self.speed

	def setDistance(self, new_distance):
		self.distance_to_target = new_distance

	def getDistance(self):
		return self.distance_to_target

	def moveBySpeed(self):
		self.distance_to_target = self.distance_to_target - self.speed

	def remainingTime(self):
		time = self.distance_to_target / self.speed
		return math.ceil(time)

	def autopilot(self):
		count = 0
		while self.distance_to_target > 0:
			self.moveBySpeed()
			count = count + 1
		return count

s1 = SpaceShip(300, 10000)
print(s1.autopilot())
s1.getSpeed()