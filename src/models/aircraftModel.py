class Aircraft:
	def __init__(self, insignia, typeID, capacity):
		self.insignia = insignia
		self.typeID = typeID
		self.capacity = capacity
		self.state = 'Available'
		self.availableAt = None
		self.numberOfFlight = None
		self.destination = None