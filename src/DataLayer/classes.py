#import csv
from models.crewModel import Crew
from models.destinationModel import Destination
from models.aircraftModel import Aircraft


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

	def registerDestination(self, destination, country, airport, distanceFromIceland, contact, emergencyNumber):
		node = destinationNode(destination, country, airport, distanceFromIceland, contact, emergencyNumber)
		self.destinations.append(node) 

		# create a instance of destination node 
		# and putting that node into the list.
	def registerCrewMember(self, ssn, name, role, rank, license, address, phonenumber, email):
		self.crew.createPilot(ssn, name, role, rank, license, address, phonenumber, email)
		# crew instance has a function that creates 
		# a crew node and puts it into a dictionary with
		# the ssn as a key.

		# iterate over all crew members and taking the flight attendants 
		# and putting them into a list and returning the list

	def openFileForReading(self, filename):
		try:
			file_stream = open(filename, 'r')
			return file_stream
		except FileNotFoundError:
			return None

	def getAllDestinationsFromFile(self):
		allDestinationsList = []
		lineCounter = 0
		for line in self.openFileForReading('csv/Destinations.csv'):
			if lineCounter == 0:
				lineCounter += 1
			else:
				destination, country, airport, distance, contact, emergencyNumber = line.strip().split(',')
				allDestinationsList.append(Destination(destination, country, airport, distance, contact, emergencyNumber))
		return allDestinationsList
	
	def getAllAircraftInfoFromFile(self):
		aircraftsList = []
		lineCounter = 0
		for line in self.openFileForReading('csv/Aircraft.csv'):
			if lineCounter == 0:
				lineCounter += 1
			else:
				insignia, typeId, capacity = line.stip().split(',')
				aircraftsList.append(Aircraft(insignia, typeId, capacity))
		return aircraftsList

	def getAllCrewFromFile(self):
		allCrewList = []
		lineCounter = 0
		for line in self.openFileForReading('csv/Crew.csv'):
			if lineCounter == 0:
				lineCounter += 1
			else:
				ssn, name, role, rank, license, address, phone, email = line.strip().split(',')
				allCrewList.append(Crew(ssn, name, role, rank, license, address, phone, email))
			return allCrewList

	
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
		        	self.crew.createPilot(row[0],row[1], row[2], row[3], row[4], row[5], row[6], row[7])


	    # taking data from csv file and inserting that data into the class 
	    # ...
	def saveLocalStuff(self):
		pass
		## stuff
		# todo..


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

	def createPilot(self, ssn, name, role, rank, license, address, phonenumber, email):
		node = Crew(ssn, name, role, rank, license, address, phonenumber, email)
		self.data[ssn] = node
		