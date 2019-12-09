from LogicLayer.logic_test import LogicLayerAPI
import models.aircraftModel
import models.crewModel
import models.destinationModel
import models.voyageModel
class Output:
    def __init__(self):
        self.printer = LogicLayerAPI()
    
    # def printMenu(self, menuString): #Sleppa??? klasauppsetning
    #     print(menuString)

    def printAllStaff(self):            #Gætum hugsanlega notað þetta sama fall í að prenta filteraðan staff lista.
        ret_str = "####\nAll Staff\n####"
        header = "\n\n{:<20} {:<15} {:<15} {:<15} {:<20} {:<13} {:<20} {:<15}".format("Name", "SSN", "Address", "Phone number", "E-mail address", "Role", "Rank", "License")   
        separator = "\n" + "-" * len(header)            #Seperates header from data
        
        staff_info = ""
        for member in self.printer.sortAllCrewAlpha():             
            staff_info += "\n{:<20} {:<15} {:<15} {:<15} {:<20} {:<13} {:<20} {:<15}".format\
                (member.name, member.ssn, member.address, member.phone, member.email, member.role, member.rank, member.license)
        
        ret_str += header + separator + staff_info
        print(ret_str)
   
    def printStaffMember(self, ssn):
        staffMember = self.printer.getCrewMemberBySsn(ssn)
        ret_str = "####\n{}\n####".format(staffMember.name)
        ret_str += "\n\nName: {}\nSocial Security Number: {}\nAddress: {}\nPhone Number: {}\nE-mail address: {}\nRole: {}\nRank: {}\nLicense: {}".format\
            (staffMember.name, staffMember.ssn, staffMember.address, staffMember.phone, staffMember.email, staffMember.role, staffMember.rank, staffMember.license)
        
        print(ret_str)
    
    def printUnavailableStaff(self, date):
        ret_str = "####\nUnavailable Staff\n####"
        header = "\n\n{:<20} {:<15} {:<20} {:<15}".format("Name", "SSN", "Rank", "Destination")   #"Becomes Available" # {:<15}
        separator = "\n" + "-" * len(header)            #Seperates header from data
        
        staff_info = ""
        if len(self.printer.getAllCrewWorking(date)) == 0:
            staff_info = "No unavailable staff members."
        else:
            for staff in self.printer.getAllCrewWorking(date):
                staff_info += "\n{:<20} {:<15} {:<20} {:<15}".format(staff.name, staff.ssn, staff.rank, staff.destination) #Ath staff.freedate # {:<15}
        
        ret_str += header + separator + staff_info
        print(ret_str)
    
    def printAvailableStaff(self, date):
        ret_str = "####\nAvailable Staff\n####"
        header = "\n\n{:<20} {:<15} {:<20}".format("Name", "SSN", "Rank")
        separator = "\n" + "-" * len(header)
        
        staff_info = ""
        if len(self.printer.getAllCrewNotWorking(date)) == 0:
            staff_info = "No available staff."
        else:
            for staff in self.printer.getAllCrewNotWorking(date):
                staff_info += "\n{:<20} {:<15} {:<20}".format(staff.name, staff.ssn, staff.rank)
        
        ret_str += header + separator + staff_info 
        print(ret_str)

    def printDestinations(self):
        ret_str = "####\nDestinations:\n####"

        for destination in self.printer.getAllDestinationsList():
            ret_str += "\n{} ({}) - {}\n\tTravel Time: {} hours\n\tContact Name: {}\n\tEmergency Number: {}".format\
                (destination.destination, destination.airport, destination.country, destination.distanceFromIceland, destination.contact, destination.emergencyNumber)
        
        print(ret_str)
   
    def printAirplanes(self):
        ret_str = "####\nAirplanes\n####"
        header = "\n\n{:<10}{:<15}{:<10}{:<15}{:<15}{:<15}{:<20}".format("Insignia", "Type", "Capacity", "Status", "Destination", "Flight Number", "Becomes Available")
        ret_str += header
        ret_str += "\n" + "-" * len(header)

        for airplane in self.printer.listOfAllAircraftsWithState("21/12/2019", "12:00"):    #ATH! Tekur við date and time frá user (input fall), setti bara inn fyrir testing purposes :)
            availableDate = airplane.availableAt[0]                                         #AvailableAt returns a tuple, containing a date and time
            availableTime = airplane.availableAt[1]
            ret_str += "\n{:<10}{:<15}{:<10}{:<15}{:<15}{:<15}{}{:>12}".format(airplane.insignia, airplane.typeID, airplane.capacity, airplane.state, airplane.destination, airplane.numberOfFlight, availableTime, availableDate)
        
        print(ret_str)
 
    def printWorkSchedule(self, ssn):
        #Gets a tuple consisting of an instance of a staff member and their designated voyages
        ret_str = "####\nWork Schedule\n####\n"
        work_plan_tuple = self.printer.getWorkScheduleForCrewMember(ssn, date1, date2)
        staff = work_plan_tuple[0]
        staff_info = "\n{:<20} {:<15} {:<15} {:<20}".format(staff.name, staff.ssn, staff.role, staff.rank)
        frame = "\n" + "=" * len(staff_info)

        schedule = ""
        plan = work_plan_tuple[1]
        if len(plan) == 0:
            schedule = "\nNo voyages for the upcoming week."
        for entry in plan:
            date, departureTime = self.printer.changeFromIsoTimeFormat(entry.departure)             #Ath nota fall frekar í LL
            datee, arrivalTime = self.printer.changeFromIsoTimeFormat(entry.arrival)
            schedule += "\n{:<15} {:<15} {:<11} {:<5}\n{:>43} {:>5}".format(date, entry.destinationAirport, "Departure: ", departureTime, "Arrival: ", arrivalTime)

        ret_str += frame + staff_info + frame + schedule
        print(ret_str)
       
    def printVoyages(self):
        #Needs an iterable format of voyages from LL
        ret_str = "####\nVoyages\n####"
        for voyage in self.printer.getAllVoyages():                                           
            voytitlestatus = "\n\n{} - {}\n   Status: {}".format('Reykjavík', voyage.destinationName, voyage.status)
            outbound = "\n   Outbound: {} - {}\t  Flight {}".format("RVK", voyage.destinationAirport, voyage.outboundFlightNumber)  

            departureDate, DepartureTime = voyage.departure
            arrAtDestDate, arrAtDestTime = voyage.arrivalAtDest
            depFromDestDate, depFromDestTime = voyage.departureFromDest
            arrivalDate, arrivalTime = voyage.arrival

            outbound_info = "\n\t{:<11} {:<6} {:<10}\n\t{:<11} {:<6} {:<10}".format("Departure: ", DepartureTime, departureDate, "Arrival: ", arrAtDestTime, arrAtDestDate)
            inbound = "\n   Inbound: {} - {}\t  Flight {}".format(voyage.destinationAirport, "RVK", voyage.inboundFlightNumber)
            inbound_info = "\n\t{:<11} {:<6} {:<10}\n\t{:<11} {:<6} {:<10}".format("Departure: ", depFromDestTime, depFromDestDate, "Arrival: ", arrivalTime, arrivalDate)
            
            crew = "\n   Crew: "
            if len(voyage.crew) < 3:
                crew+= "\nVOYAGE NOT SUFFICIENTLY STAFFED!"
            for ssn in voyage.crew: 
                member = self.printer.getCrewMemberBySsn(ssn)        
                crew += "\n\t{}, {}".format(member.name, member.rank)
            ret_str += voytitlestatus + outbound + outbound_info + inbound + inbound_info + crew
        
        print(ret_str)




class UserExperienceOutPutInputMeter:

    def __init__(self):
        stringToPrint = """

    1. Register data
    2. Retrieve data
    3. Update data

    q - Quit program

    Choose 1-3:"""

        userInput = input(stringToPrint)
        if userInput == "1":
            self.registerMenu() ## register
        elif userInput == "2":
            self.retreiveMenu() ## Retreive
        elif userInput == "3":
            self.updateMenu() ## Update

        elif userInput == "q":
            return

    def registerMenu(self):
        print("hello")
        userInput = input("""
    ###
    REGISTER DATA
    ###

    1. Voyage
    2. Assign crew to voyage.
    3. Assign airplane to voyage
    4. Crew member
    5. Destination.
    6. Airplane

    b - go back
    m - main menu

    Choose 1-5:


    """)
        
        if userInput == "1":
            self.registerVoyage()
        elif userInput == '2':
            self.registerCrewToVoyage()
        elif userInput == '3':
            self.registerAirplaneToVoyage()
        elif userInput == '4':
            self.registerCrew()
        elif userInput == '5':
            self.registerDestination()
        elif userInput == '6':
            self.registerAirplase()
        elif userInput == "b":
            pass
    def registerVoyage(self):

        print("""###
REGISTER DATA -> VOYAGE
###""")
        print("if any line is empty it will not get registered")
        destination = input('Destination: ')
        departureFromIceland = input('Departure from Iceland: ')
        departureFromDestination = input('Departure from destination: ')

        print("function not implemented, returning")

        return

    def registerCrewMember(self):
        print("""###
REGISTER DATA -> CREW
###""")
        ssn = input('Social security number: ')
        name = input('Name: ')
        phone = input('Phone number: ')
        email = input('Email: ')
        address = input('Residence: ')

        print("function not available, returning")
    def registerDestination(self):
        print("""###
REGISTER DATA -> DESTINATION
###""")
        destination = input('Destination: ')
        country     = input('Country: ')
        airport     = input('Airport: ')
        timeOfFlight = input('Time of flight: ')
        DistanceFromIceland = input('Distance from Iceland: ')
        contact = input('Contact: ')
        contactsNumber = input('Contacts phonenumber: ')
        emergencyNumber = input('Emergency number: ')
        print("function not available")
        return








    def retreiveMenu(self):
        userInput("""
    ###
    RETRIEVE DATA
    ###

    1. Crew
    2. Airplanes
    3. Destinations
    4. Voyage

    b - go back

    Choose 1-5:""")

        if userInput == "1":
            pass
        elif userInput == '2':
            pass
        elif userInput == '3':
            pass
        elif userInput == '4':
            pass
        elif userInput == 'b':
            return



    def updateMenu(self):
        userInput = input("""

    ###
    UPDATE DATA
    ###

    1. Crew member info
    2. Destination info

    b - go back
    """)

        if userInput == '1':
            self.updateCrewMenu()
        elif userInput == '2':
            self.updateDestinationMenu()
        elif userInput == 'b':
            return 0

    def updateCrewMenu(self):
        print("""
    #
    UPDATE DATA -> CREW MEMBER INFO
    #""")

        userInput = input('Enter members SSN, or b to return')


        if userInput == 'b':
            return
        elif len(userInput) == 10:  ## it's ssn
            self.updateCrewMenuSSN(userInput)
        else:
            print("not a real ssn")
            return


    def updateCrewMenuSSN(self, ssn):
        print("""
#
UPDATE DATA -> CREW MEMBER INFO -> {}
#""".format(ssn))

        print("Leave it empty if you don't want to update")
        updatedNumber = input("Phone number:")

        updatedRedidence = input("Residence:")

        updatedEmail = input("Email:")

        print("function not available")
        return

        ## check if parameters are not "" and pass those into logic to be processed.
    def updateDestinationMenu(self):
        pass