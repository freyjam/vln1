from UILayer.menuclass import Menu

class Input:
    def __init__(self):
        self.writer = Menu()

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
        ssn = input("Enter SSN: )

        return ssn


