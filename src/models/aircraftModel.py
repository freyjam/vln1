class Aircraft:
	def __init__(self, insignia, typeId, capacity):
		self.insignia = insignia
		self.typeId = typeId
		self.capacity = capacity
		self.state = 'Available'
		self.availableAt = None
		self.numberOfFlight = None
		self.destination = None