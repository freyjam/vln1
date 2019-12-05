import csv
from modelClasses.airplaneClass import airplaneClass


class DataLayerAPI:
	def __init__(self):  ## probably going to have no parameters when created, but
						 ## when the 	
		self.crew = CrewClass() ## create instance of class that maintains people
		self.destinations = [] # list of nodes of destinations
		self.airplanes = [] # list of nodes of airplanes
		self.voyages = Voyage()
	def registerPlane(self, name, model, manufacturer, type, capacity, planeInsignia, planeTypeId):
		node = Airplane(name, model, manufacturer, type, capacity, planeInsignia, planeTypeId)
		self.airplanes.append(node) ## creating a airplane node and insert that node into list
	def registerDestination(self, destination, country, airport, distanceFromIceland, contact, contactNumber, emergencyNumber):
		node = destinationNode(destination, country, airport, distanceFromIceland, contact, contactNumber, emergencyNumber)
		self.destinations.append(node)

		# create a instance of destination node 
		# and putting that node into the list.
	def registerCrewMember(self, name, ssn, address, phone, homephone, rank, role, license):
		self.crew.createPilot(name, ssn, address, phone, homephone, rank, role, license)
		# crew instance has a function that creates 
		# a crew node and puts it into a dictionary with
		# the ssn as a key.

		# iterate over all crew members and taking the flight attendants 
		# and putting them into a list and returning the list

	
	def changeCrewMemberDetail(self, ssn, address = None, phone = None, homephone = None):
		if address is not None:
			 self.crew.data[ssn].address = address
		if phone is not None:
			self.crew.data[snn].phone = phone
		if homephone is not None:
			self.crew.data[snn].homephone = homephone

		# change crew member details 
	def retrieveCrew(self):
		outputList = []
		for x, v in self.crew.data.items():
			outputList.append(v)
		return outputList
		# return every member of crew

	def loadObjectFromClass(self):
		with open('csv/Crew.csv') as csv_file:
		    csv_reader = csv.reader(csv_file, delimiter=',')
		    line_count = 0
		    for row in csv_reader:
		        if line_count == 0:
		            line_count += 1
		        else:
		        	self.createUserPilot(row[1],row[0], None, None, None, row[2], row[3], row[4] )


	    # taking data from csv file and inserting that data into the class 
	    # ...
	def saveLocalStuff(self):
		pass
		## stuff
		# todo..

class VoyageNode: 
	def __init__(self, destination, departureFromIceland, departureFromDestination):
		self.airplane = ""
		self.destination = destination
		self.departureFromIceland = departureFromIceland
		self.departureFromDestination = departureFromDestination

		## todo


class Voyage:
	def __init__(self):
		self.voyages = []

	def registerVoyage(self, airplane, destination, departureFromIceland, departureFromDestination):
		node = VoyageNode(destination, departureFromIceland, departureFromDestination)
		self.voyages.append(node)

	def registerCrewToVoyage(self, staff):
		pass

	def registerAirplaneToVoyage(self, airplane):
		pass



class CrewClass: ## store people in a hash map
	def __init__(self):
		self.data = {}

	def createPilot(self, name, ssn, address, phone, homephone, rank, role, license 
	 = None, email = None):
		node = CrewNode(name, ssn, address, phone, homephone, rank, role, license, email)
		self.data[ssn] = node
			
