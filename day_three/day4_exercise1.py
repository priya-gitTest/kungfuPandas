class Bucket:
	name = str()
	max_volume = int()
	current_volume = int()

	def __init__(self, name, max_volume, current_volume):
		self.name = name
		self.max_volume = max_volume
		self.current_volume = current_volume

	def getName(self):
		return self.name

	def getMaxVolume(self):
		return self.max_volume

	def setMaxVolume(self, new_max):
		self.max_volume = new_max

	def getCurrentVolume(self):
		return self.current_volume

	def setCurrentVolume(self, new_current):
		self.current_volume = new_current

	def transferVolume(self, new_bucket):
		difference = self.max_volume - self.current_volume

		if new_bucket.getCurrentVolume() > 0 and new_bucket.getCurrentVolume() > difference:
			self.current_volume = self.current_volume + difference
			new_bucket.setCurrentVolume( new_bucket.getCurrentVolume() - difference )

		elif new_bucket.getCurrentVolume() > 0 and new_bucket.getCurrentVolume() <= difference:
			self.current_volume = self.current_volume + new_bucket.getCurrentVolume()
			new_bucket.setCurrentVolume(0)


bucket1 = Bucket("b1", 10, 5)
bucket2 = Bucket("b2", 475, 100)

print(bucket1.getCurrentVolume())

print(bucket2.getCurrentVolume())

bucket1.transferVolume(bucket2)

print("Transfering volumes")

print(bucket1.getCurrentVolume())

print(bucket2.getCurrentVolume())
