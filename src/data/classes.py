class aeroport:
	def __init__(self):  ## probably going to have no parameters when created, but
	 				     ## when the 
		pass




class Airplane:
	def __init__(self):
		pass


class pilotNode:
	def __init__(self):
		pass

class flightAttendantNode:
	def __init__(self):
		pass


class peeps: ## store people in a hash map
	def __init__(self):
		self.buckets = [ [16] ]

	def insertpilot(self, name, ssn, address, phone, homephone):
		node = pilotNode(name, ssn, address, phone, homephone)
		index = hash(name)

