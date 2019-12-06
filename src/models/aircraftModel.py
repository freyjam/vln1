class Aircraft:
	def __init__(self, insignia, typeID, capacity):
		self.insignia = insignia
		self.typeID = typeID
		self.capacity = capacity
		self.state = 'Available'
		self.availableAt = ''
		self.numberOfFlight = ''
		self.destination = ''