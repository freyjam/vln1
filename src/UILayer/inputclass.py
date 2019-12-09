
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
        destination = input("Destination: ")
        departureFromIceland = input("Departure from Iceland: ")
        departureFromDestination = input("Departure from Destination: ")

        voyageInfoList = [destination, departureFromIceland, departureFromDestination]

        return voyageInfoList
    
    def getRegisterCrewMemberInput(self):
        ssn = input('Social security number: ')
        name = input('Name: ')
        phone = input('Phone number: ')
        email = input('Email: ')
        address = input('Residence: ')

        crewMemberInfo = [ssn, name, phone, email, address]

        return crewMemberInfo
    
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

        destinationInfo = [destination, country, airport, travelTime, contact, emergencyNumber]

        return destinationInfo
    
    def getSSN(self):
        ssn = input("Enter SSN: ")

        return ssn

    def getDate(self):
        date = input("Enter date: ")

        return date
    
    def getTime(self):
        time = input("Enter date: ")
        
        return time

