from LogicLayer.logic_test import LogicLayerAPI
 
class Menu:
    def __init__(self, menuid):
        self.menuid = menuid
 
    def getMenu(self, menuid):
        """Send message to logic layer to fetch the desired menu from the data layer"""
        #returns a menu, write code when connections between layers have been nailed down.
        pass
 
    def printMenu(self, menu):
        print(menu)
 
 
#ATH! Ekki viss um að klasinn eigi að vera settur svona fram, þ.e. hvort hann hafi aðgang að öllu þessu eða hverju nákvæmlega hann tekur við af
#logic layer, tímabundin uppsetning.
 
class PrintOverview:
    def __init__(self):
        self.printer = LogicLayerAPI()
   
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
   
    def printStaffMember(self, staffMember):
        ret_str = "####\n{}\n####".format(staffMember.name)
        ret_str += "\n\nName: {}\nSocial Security Number: {}\nAddress: {}\nPhone Number: {}\nE-mail address: {}\nRole: {}\nRank: {}\nLicense: {}".format\
            (staffMember.name, staffMember.snn, staffMember.address, staffMember.phone, staffMember.email, staffMember.role, staffMember.rank, staffMember.license)
        print(ret_str)
 
 
    def printDestinations(self):
        ret_str = "####\nDestinations:\n####"
        for destination in self.printer.getAllDestinationsList():
            ret_str += "\n{} ({}) - {}\n\tTravel Time: {} hours\n\tContact Name: {}\n\tEmergency Number: {}".format\
                (destination.destination, destination.airport, destination.country, destination.distanceFromIceland, destination.contact, destination.emergencyNumber)
        print(ret_str)
   
    def printAirplanes(self):
        ret_str = "####\nAirplanes\n####"
        header = "\n\n{:<15}{:<15}{:<20}{:<15}".format("Name", "Model", "Manufacturer", "Capacity")
        ret_str += header
        ret_str += "\n" + "-" * (len(ret_str) - 20) #-20 to make the line align better with the header
        for airplane in airplaneList:               #Vantar fall frá logic layer
            ret_str += "\n{:<15}{:<15}{:<20}{:<10}".format(airplane.name, airplane.model, airplane.manufacturer, airplane.capacity)
        print(ret_str)
 
    def printWorkSchedule(self):
        #Check how work hours are maintained in logic layer before writing this function
        pass
       
    def printVoyage(self):
        ret_str = "####\nVoyages\n####"
        for voyage in voyages_list:     #Kallar í function frá LL, t.d. getAllVoyages                                       #Abbrevations
            voytitlestatus = "\n\n{} - {}\n   Status: {}".format(voyage.deplocation, voyage.destinationname, voyage.status) #dep = departure, arr = arrival
            outbound = "\n   Outbound: {} - {}".format("RVK", voyage.destairport)                                           #dest = destination, out = outbound, in = inbound
            outbound_info = "\n\t{:<11} {:<6} {:<10}\n\t{:<11} {:<6} {:<10}".format("Departure: ", voyage.outdeptime, voyage.outdepdate, "Arrival: ", voyage.outarrtime, voyage.outarrdate)
            inbound = "\n   Inbound: {} - {}".format(voyage.destairport, "RVK")
            inbound_info = "\n\t{:<11} {:<6} {:<10}\n\t{:<11} {:<6} {:<10}".format("Departure: ", voyage.indeptime, voyage.indepdate, "Arrival: ", voyage.inarrtime, voyage.inarrdate)
            crew = "\n   Crew: "
            for member in voyage_crew:  #For every member in the voyage's crew
                crew += "\n\t{}, {}".format(member.name, member.rank)
            ret_str += voytitlestatus + outbound + outbound_info + inbound + inbound_info + crew
        print(ret_str)