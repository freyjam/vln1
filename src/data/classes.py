class DataLayerAPI:
	def __init__(self):  ## probably going to have no parameters when created, but
						 ## when the 	
		self.crew = CrewClass()
		self.destinations = []

	# def registerDestination(self, destination, country, airport, distanceFromIceland, contact, contactNumber, emergencyNumber)
	# 	node = destinationNode(destination, country, airport, distanceFromIceland, contact, contactNumber, emergencyNumber)
	# 	self.destinations.append(node)

	def createUserPilot(self, name, ssn, address, phone , homephone , rank, role, license):
		self.crew.createPilot(name, ssn, address, phone, homephone, rank, role, license)

	def getAllDestinations(self):
		output = []
		for x in self.destinations:
			output.append(x.destination)
		return output

	def retrieveCrew(self):
		outputList = []
		for x, v in self.crew.data.items():
			outputList.append(v)
		return outputList



class Voyage: 
	def __init__(self):
		pass

class destinationNode:
	def __init__(self, destination, country, airport, distanceFromIceland, contact, contactNumber, emergencyNumber):
		self.destination = destination
		self.country  = country
		self.airport = airport
		self.distanceFromIceland = distanceFromIceland
		self.contact = contact
		self.contactNumber = contactNumber
		self.emergencyNumber = emergencyNumber


class Airplane:
	def __init__(self):
		pass


class CrewNode:
	def __init__(self, name, ssn, address, phone , homephone , role, rank, license ):
		self.name = name
		self.ssn = ssn
		self.address = address
		self.phone = phone
		self.homephone = homephone
		self.rank = rank
		self.role = role
		self.license = license


class CrewClass: ## store people in a hash map
	def __init__(self):
		self.data = {}

	def createPilot(self, name, ssn, address, phone, homephone, rank, role, license 
	 = None):
		node = CrewNode(name, ssn, address, phone, homephone, rank, role, license)
		self.data[ssn] = node
			
	def contains(self, name, ssn):
		out = False
		index = hash(name) % self.cap
		for x in self.buckets[index]:
			if x.ssn is ssn:
				out = True

		return out

	def function():
		pass
  