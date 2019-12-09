
from models.crewModel import Crew
from models.destinationModel import Destination
from models.aircraftModel import Aircraft
from models.voyageModel import Voyage


class DataLayerAPI:

    def openFileForReading(self, filename):
        try:
            fileStream = open(filename, 'r')
            return fileStream
        except FileNotFoundError:
            return None

    def getAllDestinationsFromFile(self):
        '''Reads all info about destinations from file and returns a list of destination instances'''
        allDestinationsList = []
        lineCounter = 0
        destFileStream = self.openFileForReading('csv/Destinations.csv')
        if destFileStream:
            for line in destFileStream:
                if lineCounter == 0:
                    lineCounter += 1
                else:
                    destination, country, airport, distance, contact, emergencyNumber = line.strip().split(',')
                    allDestinationsList.append(Destination(destination, country, airport, distance, contact, emergencyNumber))
            return allDestinationsList
    
    def getAllAircraftInfoFromFile(self):
        '''Reads all info about aircrafts from file and returns a list of Aircraft instances'''
        aircraftsList = []
        lineCounter = 0
        aircraftFileStream = self.openFileForReading('csv/Aircraft.csv')
        if aircraftFileStream:
            for line in aircraftFileStream:
                if lineCounter == 0:
                    lineCounter += 1
                else:
                    insignia, typeId, capacity = line.strip().split(',')
                    aircraftsList.append(Aircraft(insignia, typeId, capacity))
            return aircraftsList

    def getAllCrewFromFile(self):
        '''Reads all info about crew from file and returns a list of crew instances'''
        allCrewList = []
        lineCounter = 0
        CrewFileStream = self.openFileForReading('csv/Crew.csv')
        if CrewFileStream:
            for line in CrewFileStream:
                if lineCounter == 0:                                    # So that instance will not be made out of header line
                    lineCounter += 1
                else:
                    ssn, name, role, rank, license, address, phone, email = line.strip().split(',')
                    allCrewList.append(Crew(ssn, name, role, rank, license, address, phone, email))
            return allCrewList
        
    def getAllVoyageFromFile(self):
        allVoyagesList = []
        lineCounter = 0
        VoyageFileStream = self.openFileForReading('csv/Voyage.csv')
        if VoyageFileStream:
            for line in VoyageFileStream:
                if lineCounter == 0:
                    lineCounter +=1
                else:
                    voyageFileList = line.strip().split(',')
                    allVoyagesList.append(Voyage(voyageFileList[0], voyageFileList[1], voyageFileList[2], voyageFileList[3], voyageFileList[4], voyageFileList[5], voyageFileList[6], voyageFileList[7], voyageFileList[8], voyageFileList[9:]))
            return allVoyagesList


<<<<<<< HEAD

=======
    def addVoyageToCSV(self, instance):
        destination = instance.destination
        name = instance.name
        destinationAirport = instance.destinationAirport
        departure = instance.departure
        arrivalAtAirport = instance.arrivalAtAirport
        deportureFromAirport = instance.deportureFromAirport
        arrival = instance.arrival
        aircraft = instance.aircraft
        outboundFlightNumber = instance.outboundFlightNumber
        captain = instance.captain
        copilot = instance.copilot
        scc = instance.scc
        fa1 = instance.fa1
        fa2 = instance.fa2

        try:
            row = [destination, name,destinationAirport,departure,arrivalAtDestination,departureFromDestination,arrival,aircraft,outboundFlightNumber,inboundFlightNumber,captain,copilot,scc,fa1,fa2 ] 
            row = ",".join(row)
            row = "\n" + row
            with open('csv/Voyage.csv','a') as file:
                file.write(row)

        except Exception as e:
            return e

    def addAircraftsToCSV(self, instance):
        planeInsignia = instance.planeInsignia
        planeTypeId   = instance.planeTypeId
        capacity      = instance.capacity


<<<<<<< HEAD
        row = [planeInsignia, planeTypeId, capacity] 
        row = ",".join(row)
        row = "\n" + row
        with open('csv/Aircraft.csv','a') as file:
            file.write(row)
>>>>>>> 8e6150241c0f25edd2063091c601e72801601754
=======
        try:
            row = [planeInsignia, planeTypeId, capacity] 
            row = ",".join(row)
            row = "\n" + row
            with open('csv/Aircraft.csv','a') as file:
                file.write(row)
        except Exception as e:
            return e

>>>>>>> 1d1d8051ab813d1dde20128279097a3ab9a0f9e5
    def addDestinationToCSV(self, instance):
        destination         = instance.destination
        country             = instance.country
        airport             = instance.airport
        distanceFromIceland = instance.distanceFromIceland
        contact             = instance.contact
        emergencyNumber     = instance.emergencyNumber
       
        try:
            
            row = [destination, country, airport, distanceFromIceland, contact, emergencyNumber ] 
            row = ",".join(row)
            row = "\n" + row
            with open('csv/Destination.csv','a') as file:
                file.write(row)
        except Exception as e:
            return e    

    
    def addCrewToCSV(self, instance):
        email = instance.email
        ssn = instance.ssn
        name = instance.name
        address = instance.address
        phone = instance.phonenumber
        role = instance.role
        rank = instance.rank
        license = instance.address
        try:        
            row = [ssn, name, role, rank, license, address, phonenumber, email ] 
            row = ",".join(row)
            row = "\n" + row
            with open('csv/Crew.csv','a') as file:
                file.write(row)
            return "success"
        except Exception as e:
            return e
    
