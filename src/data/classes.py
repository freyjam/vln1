import csv


class DataLayerAPI:
	def __init__(self):  ## probably going to have no parameters when created, but
						 ## when the 	
		self.crew = CrewClass()
		self.destinations = []
		self.airplanes = []

	def registerPlane(self, name, model, manufacturer, type, capacity, planeInsignia, planeTypeId):
		node = Airplane(name, model, manufacturer, type, capacity, planeInsignia, planeTypeId)
		self.airplanes.append(node)
	def registerDestination(self, destination, country, airport, distanceFromIceland, contact, contactNumber, emergencyNumber):
		node = destinationNode(destination, country, airport, distanceFromIceland, contact, contactNumber, emergencyNumber)
		self.destinations.append(node)

	def createUserPilot(self, name, ssn, address, phone, homephone, rank, role, license):
		self.crew.createPilot(name, ssn, address, phone, homephone, rank, role, license)

	def getAllDestinations(self):
		output = []
		for x in self.destinations:
			output.append(x.destination)
		return output

	def getAllPilots(self):
		output = []
		for x, v in self.crew.data.items():
			if v.role is "Pilot":
				output.append(v)
		return output
	def getAllFlightAttendants(self):
		output = []
		for x, v in self.crew.data.items():
			if v.role is "Cabincrew":
				output.append(v)
		return output
	def getSpecificEmployee(self, ssn):
		return self.crew.data[ssn]

	def changeEmployeeDetail(self, ssn, address = None, phone = None, homephone = None):
		if address is not None:
			 self.crew.data[ssn].address = address
		if phone is not None:
			self.crew.data[snn].phone = phone
		if homephone is not None:
			self.crew.data[snn].homephone = homephone
	def retrieveCrew(self):
		outputList = []
		for x, v in self.crew.data.items():
			outputList.append(v)
		return outputList

	def loadObjectFromClass(self):
		with open('csv/Crew.csv') as csv_file:
		    csv_reader = csv.reader(csv_file, delimiter=',')
		    line_count = 0
		    for row in csv_reader:
		        if line_count == 0:
		            line_count += 1
		        else:
		        	self.createUserPilot(row[1],row[0], None, None, None, row[2], row[3], row[4] )



	def saveLocalStuff(self):
		pass
		## stuff

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
	def __init__(self, name, model, manufacturer, type, capacity, planeInsignia, planeTypeId):
		self.name = name
		self.model = model
		self.manufacturer = manufacturer
		self.type = type
		self.capacity = capacity
		self.planeInsignia = planeInsignia
		self.planeTypeId = planeTypeId



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
			
	

	