from models.destinationModel import Destination
from models.crewModel import Crew
from models.voyageModel import Voyage

class Input:
    def __init__(self):
        pass

    def getUpdateStaffInput(self):
        newNumber = input("Enter Phone Number: ")
        newResidence = input("Enter Residence: ")
        newEmail = input("Enter Email Address: ")

        newInfoList = [newNumber, newResidence, newEmail]

        return newInfoList
    
    def getRegisterVoyageInput(self):
        return Voyage(
            input('Destination name: '),
            input('Destination Airport: '),
            input('Departure from Iceland: '),
            input('Arrival at destination: '),
            input('Departure from destination: '),
            input('Time of arrival: '),
            input('Aircraft: '),
            input('Outbound flightnumber: '),
            input('Inbound flightnumber: ')
        )
    
    def getRegisterCrewMemberInput(self):
        ssn = input('Social security number: ')
        name = input('Name: ')
        role = input('Role: ')
        rank = input('Rank: ')
        license = input('License: ')
        address = input('Residence: ')
        phone = input('Phone number: ')
        email = input('Email: ')

        return Crew(ssn, name, role, rank, license, address, phone, email)

    def getRegisterAircraftInput(self):
        name = input("Name: ")
        model = input("Model: ")
        manufacturer = input("Manufacturer: ")
        aircraftType = input("Type: ")
        capacity = input("Capacity: ")

        aircraftInfo = [name, model, manufacturer, aircraftType, capacity]

        return aircraftInfo
    
    def getRegisterDestinationInput(self):
        destination = input('Destination: ')
        country     = input('Country: ')
        airport     = input('Airport: ')
        travelTime = input('Travel Time: ')
        contact = input('Contact: ')
        emergencyNumber = input('Emergency number: ')

        return Destination(destination, country, airport, travelTime, contact, emergencyNumber)
    
    def getSSN(self):
        ssn = input("Enter SSN: ")

        return ssn

    def getDate(self):
        date = input("Enter date: ")

        return date
    
    def getTime(self):
        time = input("Enter date: ")
        
        return time

