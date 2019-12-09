from tempfile import NamedTemporaryFile
import shutil
import csv


class WriteCSV:



    def updateCrewCSV(self, listOfInstances):
        # create temporary file
        tempfile = NamedTemporaryFile(mode='w', delete=False)
        for instance in listOfInstances:
            
            email = instance.email
            ssn = instance.ssn
            name = instance.name
            address = instance.address
            phone = instance.phonenumber
            role = instance.role
            rank = instance.rank
            license = instance.address
          
            row = [ssn, name, role, rank, license, address, phonenumber, email ] 
            row = ",".join(row)
            row = "\n" + row
            with tempfile as file:
                file.write(row)

        shutil.copy(tempfile, 'csv/Crew.csv')

    


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


        row = [planeInsignia, planeTypeId, capacity] 
        row = ",".join(row)
        row = "\n" + row
        with open('csv/Aircraft.csv','a') as file:
            file.write(row)

        try:
            row = [planeInsignia, planeTypeId, capacity] 
            row = ",".join(row)
            row = "\n" + row
            with open('csv/Aircraft.csv','a') as file:
                file.write(row)
        except Exception as e:
            return e

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
    
