from LogicLayer.logic_test import LogicLayerAPI
 
class Input:
    def __init__(self):
        pass
 
    def getMenu(self):
        """Processes input for menu choice, i.e. 1,2,3, etc."""
        pass

    def getInfo(self):
        """Sends entered info to logic layer, i.e. ssn, name and other written information"""
        pass
 
#ATH! Ekki viss um að klasinn eigi að vera settur svona fram, þ.e. hvort hann hafi aðgang að öllu þessu eða hverju nákvæmlega hann tekur við af
#logic layer, tímabundin uppsetning.
 
class Output:
    def __init__(self):
        self.printer = LogicLayerAPI()
    
    def printMenu(self, menu):
        #Needs an iterable format of menu options.
        output = "What would you like to do?\n"
        i = 1                                       #Initialize number of options, first option is marked 1.
        for option in menu:
            output += "\n" + "{}. {}".format(i, option)
            i += 1
        output += "\n\nq - Quit Program"
        print(output)
   
    def printAllStaff(self):            #Gætum hugsanlega notað þetta sama fall í að prenta filteraðan staff lista.
        a = LogicLayerAPI()
        ret_str = "####\nAll Staff\n####"
        header = "\n\n{:<15} {:<15} {:<15} {:<15} {:<20} {:<13} {:<25} {:<15}".format("Name", "SSN", "Address", "Phone number", "E-mail address", "Role", "Rank", "License")   
        ret_str += header
        ret_str += "\n" + "-" * len(ret_str)            #Seperates header from data
        for member in a.sortAllCrewAlpha():             #Laga þegar við tengjum við LL
            ret_str += "\n{:<15} {:<15} {:<15} {:<15} {:<20} {:<13} {:<25} {:<15}".format\
                (member.name, member.ssn, member.address, member.phone, member.email, member.role, member.rank, member.license)
        print(ret_str)
   
    def printStaffMember(self):
        ret_str = "####\n{}\n####".format(staffMember.name)
        ret_str += "\n\nName: {}\nSocial Security Number: {}\nAddress: {}\nPhone Number: {}\nE-mail address: {}\nRole: {}\nRank: {}\nLicense: {}".format\
            (staffMember.name, staffMember.snn, staffMember.address, staffMember.phone, staffMember.email, staffMember.role, staffMember.rank, staffMember.license)
        print(ret_str)
    
    def printUnavailableStaff(self):
        #Birta fleiri/færri upplýsingar?
        ret_str = "####\nUnavailable Staff\n####"
        header = "\n\n{:<15} {:<15} {:<25} {:<15} {:<15}".format("Name", "SSN", "Rank", "Destination", "Becomes Available")   
        ret_str += header
        ret_str += "\n" + "-" * (len(ret_str) - 20)            #Seperates header from data
        for staff in unavailable_staff_list:
            ret_str += "\n{:<15} {:<15} {:<25} {:<15} {:<15}".format(staff.name, staff.ssn, staff.rank, staff.destination, staff.freedate)
        print(ret_str)
    
    def printAvailableStaff(self):
        #Birta fleiri upplýsingar? T.d. license
        ret_str = "####\nAvailable Staff\n####"
        header = "\n\n{:<15} {:<15} {:<25}".format("Name", "SSN", "Rank")
        ret_str += header + "\n" + "-" * (len(ret_str) - 20)
        for staff in available_staff_list:
            ret_str += "\n{:<15} {:<15} {:<25}".format(staff.name, staff.ssn, staff.rank)
        print(ret_str)

    def printDestinations(self):
        ret_str = "####\nDestinations:\n####"
        for destination in self.printer.getAllDestinationsList():
            ret_str += "\n{} ({}) - {}\n\tTravel Time: {} hours\n\tContact Name: {}\n\tEmergency Number: {}".format\
                (destination.destination, destination.airport, destination.country, destination.distanceFromIceland, destination.contact, destination.emergencyNumber)
        print(ret_str)
   
    def printAirplanes(self):
        #Needs an iterable format of all airplanes, attributes must be accessible.
        ret_str = "####\nAirplanes\n####"
        header = "\n\n{:<15}{:<15}{:<20}{:<15}".format("Name", "Model", "Manufacturer", "Capacity")
        ret_str += header
        ret_str += "\n" + "-" * (len(ret_str) - 20) #-20 to make the line align better with the header
        for airplane in airplaneList:               #Vantar fall frá logic layer
            ret_str += "\n{:<15}{:<15}{:<20}{:<10}".format(airplane.name, airplane.model, airplane.manufacturer, airplane.capacity)
        print(ret_str)
 
    def printWorkSchedule(self):
        #Needs both the desired staff member and their work schedule from LL
        ret_str = "####\nWork Schedule\n####\n"
        staff_info = "\n{:<15} {:<15} {:<15} {:<30}".format(staff.name, staff.ssn, staff.role, staff.rank)
        frame = "\n" + "=" * (len(staff_info) - 5)
        schedule = ""
        for entry in work_plan:
            schedule += "\n{:<15} {:<15} {:<11} {:<5}\n{:>43} {:>6}".format(entry.ddmmyy, entry.destination, "Departure: ", entry.departuretime, "Arrival: ", entry.arrivaltime)
        ret_str += frame + staff_info + frame + schedule
        print(ret_str)
       
    def printVoyage(self):
        #Needs an iterable format of voyages from LL
        #Skoða formattið á flight number þegar hægt er að prófa kóðan, gæti litið illa út :)
        ret_str = "####\nVoyages\n####"
        for voyage in voyages_list:     #Kallar í function frá LL, t.d. getAllVoyages                                       #Abbrevations
            voytitlestatus = "\n\n{} - {}\n   Status: {}".format(voyage.deplocation, voyage.destinationname, voyage.status) #dep = departure, arr = arrival
            outbound = "\n   Outbound: {} - {}\t{}".format("RVK", voyage.destairport, voyage.outflightnumber)                                           #dest = destination, out = outbound, in = inbound
            outbound_info = "\n\t{:<11} {:<6} {:<10}\n\t{:<11} {:<6} {:<10}".format("Departure: ", voyage.outdeptime, voyage.outdepdate, "Arrival: ", voyage.outarrtime, voyage.outarrdate)
            inbound = "\n   Inbound: {} - {}\t{}".format(voyage.destairport, "RVK", voyage.inflightnumber)
            inbound_info = "\n\t{:<11} {:<6} {:<10}\n\t{:<11} {:<6} {:<10}".format("Departure: ", voyage.indeptime, voyage.indepdate, "Arrival: ", voyage.inarrtime, voyage.inarrdate)
            crew = "\n   Crew: "
            for member in voyage_crew:  #For every member in the voyage's crew
                crew += "\n\t{}, {}".format(member.name, member.rank)
            ret_str += voytitlestatus + outbound + outbound_info + inbound + inbound_info + crew
        print(ret_str)