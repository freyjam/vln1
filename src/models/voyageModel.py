class Voyage: 
	def __init__(self, destinationName, destinationAirport, departure, arrivalAtDest, departureFromDest, arrival, aircraft, outboundFlightNumber, inboundFlightNumber, crewList=None):
		self.destinationName = destinationName
		self.destinationAirport = destinationAirport
		self.departure = departure
		self.arrivalAtDest = arrivalAtDest
		self.departureFromDest = departureFromDest
		self.arrival = arrival
		self.aircraft = aircraft
		self.outboundFlightNumber = outboundFlightNumber
		self.inboundFlightNumber = inboundFlightNumber
		self.crew = crewList
		self.status = None
        
