#import logic_layer
 
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
    def __init__(self, staff, airplane, destination, voyage, workPlan):
        self.staff = staff
        self.airplane = airplane
        self.destination = destination
        self.voyage = voyage
        self.workPlan = workPlan
   
    def printAllStaff(self):            #Gætum hugsanlega notað þetta sama fall í að prenta filteraðan staff lista.
        ret_str = "####\nAll Staff\n####"
        #Bæta við status ? Eða bara hafa hann þegar leitað er eftir status? (gæti verið hentugt að sjá beint í yfirliti hver er laus og hver ekki)
        header = "\n\n{:<15} {:<15} {:<15} {:<15} {:<20} {:<13} {:<25} {:<15}".format("Name", "SSN", "Address", "Phone number", "E-mail address", "Role", "Rank", "License")   
        ret_str += header
        ret_str += "\n" + "-" * len(ret_str)            #Seperates header from data
        for member in staffList:                        #Laga þegar við tengjum við LL
            ret_str += "\n{:<15} {:<15} {:<15} {:<15} {:<20} {:<13} {:<25} {:<15}".format\
                (member.name, member.ssn, member.address, member.phone, member.email, member.role, member.rank, member.air_license)
        print(ret_str)
   
    def printStaffMember(self, staffMember):
        ret_str = "####\n{}\n####".format(staffMember.name)
        ret_str += "\n\nName: {}\nSocial Security Number: {}\nAddress: {}\nPhone Number: {}\nE-mail address: {}\nRole: {}\nRank: {}\nLicense: {}".format\
            (staffMember.name, staffMember.snn, staffMember.address, staffMember.phone, staffMember.email, staffMember.role, staffMember.rank, staffMember.license)
        print(ret_str)
 
 
    def printDestinations(self):
        ret_str = "####\nDestinations:\n####"
        for destination in destinationList:         #Laga þegar við tengjum við LL.
            ret_str += "\n{} ({}) - {}\n\tTravel Time: {} hours\n\tDistance from Iceland: {} km\n\tContact Name: {}\n\tEmergency Number: {}".format\
                (destination.destination, destination.airport, destination.country, destination.time, destination.distance, destination.contactName, destination.emergencyNumber)
        print(ret_str)
   
    def printAirplanes(self):
        ret_str = "####\nAirplanes\n####"
        header = "\n\n{:<15}{:<15}{:<20}{:<15}".format("Name", "Model", "Manufacturer", "Capacity")
        ret_str += header
        ret_str += "\n" + "-" * (len(ret_str) - 20) #-20 to make the line align better with the header
        for airplane in airplaneList:               #Laga þegar við tengjum við LL
            ret_str += "\n{:<15}{:<15}{:<20}{:<10}".format(airplane.name, airplane.model, airplane.manufacturer, airplane.capacity)
        print(ret_str)
 
    def printWorkSchedule(self):
        #Check how work hours are maintained in logic layer before writing this function
        pass
       
    def printVoyage(self):
        #Verkefni morgundagsins :)
        pass