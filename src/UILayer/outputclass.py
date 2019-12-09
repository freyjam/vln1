from LogicLayer.logic_test import LogicLayerAPI

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
        ret_str = "####\nUnavailable Staff {}\n####".format(date)
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
        ret_str = "####\nAvailable Staff {}\n####".format(date)
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

            departureDate, DepartureTime = self.printer.changeFromIsoTimeFormat(voyage.departure)
            arrAtDestDate, arrAtDestTime = self.printer.changeFromIsoTimeFormat(voyage.arrivalAtDest)
            depFromDestDate, depFromDestTime = self.printer.changeFromIsoTimeFormat(voyage.departureFromDest)
            arrivalDate, arrivalTime = self.printer.changeFromIsoTimeFormat(voyage.arrival)

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
