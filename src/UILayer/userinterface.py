from LogicLayer.logic_test import LogicLayerAPI

#ATH! Ekki viss um að klasinn eigi að vera settur svona fram, þ.e. hvort hann hafi aðgang að öllu þessu eða hverju nákvæmlega hann tekur við af
#logic layer, tímabundin uppsetning.
 
class Output:
    def __init__(self):
        self.printer = LogicLayerAPI()
   
    def printAllStaff(self):            #Gætum hugsanlega notað þetta sama fall í að prenta filteraðan staff lista.
        a = LogicLayerAPI()
        ret_str = "####\nAll Staff\n####"
        header = "\n\n{:<20} {:<15} {:<15} {:<15} {:<20} {:<13} {:<25} {:<15}".format("Name", "SSN", "Address", "Phone number", "E-mail address", "Role", "Rank", "License")   
        ret_str += header
        ret_str += "\n" + "-" * len(ret_str)            #Seperates header from data
        for member in a.sortAllCrewAlpha():             #Laga þegar við tengjum við LL
            ret_str += "\n{:<20} {:<15} {:<15} {:<15} {:<20} {:<13} {:<25} {:<15}".format\
                (member.name, member.ssn, member.address, member.phone, member.email, member.role, member.rank, member.license)
        print(ret_str)
   
    def printStaffMember(self, ssn):
        staffMember = self.printer.getCrewMemberBySsn(ssn)
        ret_str = "####\n{}\n####".format(staffMember.name)
        ret_str += "\n\nName: {}\nSocial Security Number: {}\nAddress: {}\nPhone Number: {}\nE-mail address: {}\nRole: {}\nRank: {}\nLicense: {}".format\
            (staffMember.name, staffMember.snn, staffMember.address, staffMember.phone, staffMember.email, staffMember.role, staffMember.rank, staffMember.license)
        print(ret_str)
    
    def printUnavailableStaff(self, date):
        #Birta fleiri/færri upplýsingar?
        ret_str = "####\nUnavailable Staff\n####"
        header = "\n\n{:<20} {:<15} {:<25} {:<15}".format("Name", "SSN", "Rank", "Destination")   #"Becomes Available" # {:<15}
        ret_str += header
        ret_str += "\n" + "-" * (len(ret_str) - 20)            #Seperates header from data
        for staff in self.printer.getAllCrewWorking(date):
            ret_str += "\n{:<20} {:<15} {:<25} {:<15}".format(staff.name, staff.ssn, staff.rank, staff.destination) #Ath staff.freedate # {:<15}
        print(ret_str)
    
    def printAvailableStaff(self, date):
        #Birta fleiri upplýsingar? T.d. license
        ret_str = "####\nAvailable Staff\n####"
        header = "\n\n{:<20} {:<15} {:<25}".format("Name", "SSN", "Rank")
        ret_str += header + "\n" + "-" * (len(ret_str) - 20)
        for staff in self.printer.getAllCrewNotWorking(date):
            ret_str += "\n{:<20} {:<15} {:<25}".format(staff.name, staff.ssn, staff.rank)
        print(ret_str)

    def printDestinations(self):
        ret_str = "####\nDestinations:\n####"
        for destination in self.printer.getAllDestinationsList():
            ret_str += "\n{} ({}) - {}\n\tTravel Time: {} hours\n\tContact Name: {}\n\tEmergency Number: {}".format\
                (destination.destination, destination.airport, destination.country, destination.distanceFromIceland, destination.contact, destination.emergencyNumber)
        print(ret_str)
   
    def printAirplanes(self):
        ret_str = "####\nAirplanes\n####"
        header = "\n\n{:<15}{:<15}{:<15}".format("Insignia", "Type", "Capacity")
        ret_str += header
        ret_str += "\n" + "-" * (len(ret_str) - 20) #-20 to make the line align better with the header
        for airplane in airplaneList:               #Vantar fall frá logic layer
            ret_str += "\n{:<15}{:<15}{:<10}".format(airplane.insignia, airplane.typeid, airplane.capacity)
        print(ret_str)
 
    def printWorkSchedule(self, ssn, date1, date2):
        #Gets a tuple consisting of an instance of a staff member and their designated voyages
        ret_str = "####\nWork Schedule\n####\n"
        schedule = ""
        work_plan_tuple = self.printer.getWorkScheduleForCrewMember(ssn, date1, date2)
        staff = work_plan_tuple[0]
        staff_info = "\n{:<20} {:<15} {:<15} {:<30}".format(staff.name, staff.ssn, staff.role, staff.rank)
        frame = "\n" + "=" * (len(staff_info) - 5)
        plan = work_plan_tuple[1]
        for entry in plan:
            date, departureTime = self.printer.changeFromIsoTimeFormat(entry.departure)             #Ath nota fall frekar í LL
            datee, arrivalTime = self.printer.changeFromIsoTimeFormat(entry.arrival)
            schedule += "\n{:<15} {:<15} {:<11} {:<5}\n{:>43} {:>5}".format(date, entry.destinationAirport, "Departure: ", departureTime, "Arrival: ", arrivalTime)
        ret_str += frame + staff_info + frame + schedule
        print(ret_str)
       
    def printVoyage(self):
        #Needs an iterable format of voyages from LL
        #Skoða formattið á flight number þegar hægt er að prófa kóðan, gæti litið illa út :)
        ret_str = "####\nVoyages\n####"
        for voyage in self.printer.getAllVoyages():     #Kallar í function frá LL, t.d. getAllVoyages                                       #Abbrevations
            voytitlestatus = "\n\n{} - {}\n   Status: {}".format('Reykjavík', voyage.destinationName, 'Landed') #dep = departure, arr = arrival
            outbound = "\n   Outbound: {} - {}\t{}".format("RVK", voyage.destinationAirport, voyage.outboundFlightNumber)                                           #dest = destination, out = outbound, in = inbound
            departureDate, DepartureTime = self.printer.changeFromIsoTimeFormat(voyage.departure)
            arrAtDestDate, arrAtDestTime = self.printer.changeFromIsoTimeFormat(voyage.arrivalAtDest)
            depFromDestDate, depFromDestTime = self.printer.changeFromIsoTimeFormat(voyage.departureFromDest)
            arrivalDate, arrivalTime = self.printer.changeFromIsoTimeFormat(voyage.arrival)
            outbound_info = "\n\t{:<11} {:<6} {:<10}\n\t{:<11} {:<6} {:<10}".format("Departure: ", DepartureTime, departureDate, "Arrival: ", arrAtDestTime, arrAtDestDate)
            inbound = "\n   Inbound: {} - {}\t{}".format(voyage.destinationAirport, "RVK", voyage.inboundFlightNumber)
            inbound_info = "\n\t{:<11} {:<6} {:<10}\n\t{:<11} {:<6} {:<10}".format("Departure: ", depFromDestTime, depFromDestDate, "Arrival: ", arrivalTime, arrivalDate)
            crew = "\n   Crew: "
            for ssn in voyage.crew:  #For every member in the voyage's crew
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
            return

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
