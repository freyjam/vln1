from tempfile import NamedTemporaryFile
import shutil
import csv


class WriteCSV:


    def addCrewCSV(self, instance):
        email = instance.email
        ssn = instance.ssn
        name = instance.name
        address = instance.address
        phone = instance.phone
        role = instance.role
        rank = instance.rank
        license = instance.license

        row = [ssn, name, role, rank, license, address, phone, email ]
        row = ",".join(row)
        row = "\n" + row

        with open('csv/Crew.csv','a') as file:
            file.write(row)

    def addVoyageToCSV(self, instance):
        row = [
            instance.destinationName,
            instance.destinationAirport,
            instance.departure,
            instance.arrivalAtDest,
            instance.departureFromDest,
            instance.arrival,
            instance.aircraft,
            instance.outboundFlightNumber,
            instance.inboundFlightNumber
        ]

        ''' TODO!
        captain = instance.captain
        copilot = instance.copilot
        scc = instance.scc
        fa1 = instance.fa1
        fa2 = instance.fa2
        '''

        row = ",".join(row)
        row = "\n" + row
        with open('csv/Voyage.csv','a') as file:
            file.write(row)

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
            
        row = [destination, country, airport, distanceFromIceland, contact, emergencyNumber ]
        row = ",".join(row)
        row = "\n" + row
        with open('csv/Destinations.csv','a') as file:
            file.write(row)

    def addCrewToCSV(self, instance):
        email = instance.email
        ssn = instance.ssn
        name = instance.name
        address = instance.address
        phone = instance.phone
        role = instance.role
        rank = instance.rank
        license = instance.address
        try:        
            row = [ssn, name, role, rank, license, address, phone, email ]
            row = ",".join(row)
            row = "\n" + row
            with open('csv/Crew.csv','a') as file:
                file.write(row)
            return "success"
        except Exception as e:
            return e
    
