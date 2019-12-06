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


def mainMenu():
    stringToPrint = """

1. Register data
2. Retrieve data
3. Update data

q - Quit program

Choose 1-3:"""

    userInput = input(stringToPrint)
    if userInput == 1:
        registerMenu() ## register
    elif userInput == 2:
        retreiveMenu() ## Retreive
    elif userInput == 3:
        updateMenu() ## Update

    elif userInput == "q":
        return

def registerMenu():
    userInput = input("""
###
REGISTER DATA
###

1. Voyage
2. Crew member
3. Destination.
4. Assign crew to voyage.
5. Airplane

b - go back
m - main menu

Choose 1-5:


""")



def retreiveMenu():
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

    if userInput == 1:
        pass
    elif userInput == 2:
        pass
    elif userInput == 3:
        pass
    elif userInput == 4:
        pass
    elif userInput == 'b':
        return



def updateMenu():
    userInput = input("""

###
UPDATE DATA
###

1. Crew member info
2. Destination info

b - go back
""")

    if userInput == 1:
        updateCrewMenu()
    elif userInput == 2:
        updateDestinationMenu()
    elif userInput == 'b':
        return

def updateCrewMenu():
    userInput = input("""
#
UPDATE DATA -> CREW MEMBER INFO
#

Enter member's SSN:

b - go back""")

    if userInput == 'b':
        return
    else:  ## it's ssn
        updateCrewMenuSSN(userInput)

def updateCrewMenuSSN(ssn):
    print("""
    #
    UPDATE DATA -> CREW MEMBER INFO -> {}
    #""".format(ssn))

    print("Leave it empty if you don't want to update")
    updatedNumber = input("Phone number:")

    updatedRedidence = input("Residence:")

    updatedEmail = input("Email:")

def updateDestinationMenu():
    pass

mainMenu()