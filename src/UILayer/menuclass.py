from UILayer.outputclass import Output
from UILayer.inputclass import Input
from LogicLayer.logic_test import LogicLayerAPI

class MenuAPI:
    def __init__(self):
        self.inputclass = Input()
        self.outputclass = Output()
        self.logic = LogicLayerAPI()
    
    def mainMenu(self):
        print("Welcome to NaN Air!")
        mainMenu = """

    1. Register data
    2. Retrieve data
    3. Update data

    q - Quit program

    Choose 1-3: """
        userInput = input(mainMenu)
        if userInput == "1":
            self.registerMenu()
        elif userInput == "2":
            self.retrieveMenu() 
        elif userInput == "3":
            self.updateMenu() 
        elif userInput == "q":
            return
        


    """
    Register
    """

    def registerMenu(self):
        print("###\nREGISTER DATA\n###")
        registerMenu = input("""

    1. Voyage
    2. Assign crew to voyage.
    3. Assign airplane to voyage
    4. Crew member
    5. Destination.
    6. Airplane

    b - go back
    m - main menu

    Choose 1-6: """)
        userInput = input(registerMenu)
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

        print("###\nREGISTER DATA -> VOYAGE\n###")
        print("If any line is empty it will not get registered")
        voyageInfo = self.inputclass.getRegisterVoyageInput()

        return voyageInfo

    def registerCrewMember(self):
        print("###\nREGISTER DATA -> CREW\n###")

        crewMemberInfo = self.inputclass.getRegisterCrewMemberInput()

        return crewMemberInfo

    def registerDestination(self):
        print("""###\nREGISTER DATA -> DESTINATION\n###""")

        destinationInfo = self.inputclass.getRegisterDestinationInput()
        print("function not available")
        
        return destinationInfo
    

    """
    Retrieve
    """

    def retrieveMenu(self):
        print("###\nRETRIEVE DATA\n###")
        retrieveMenuList = """

    1. Crew
    2. Aircrafts
    3. Destinations
    4. Voyage

    b - go back

    Choose 1-5: """
        userInput = input(retrieveMenuList)
        if userInput == '1':
            self.retrieveCrewMenu()   #Retrieve Crew
        elif userInput == '2':
            pass                    #Retrieve Aircrafts
        elif userInput == '3':
            pass                    #Retrieve Destinations
        elif userInput == '4':
            self.retrieveVoyagesMenu()                  #Retrieve Voyages
        elif userInput == 'b':
            return
    
    def retrieveVoyagesMenu(self):
        print("###\nRETRIEVE DATA -> VOYAGE\n###")
        retrieveVoyagesMenu = """

        1. Next Day
        2. Next Week
        3. By Crew Member (SSN)

        b - go back

        Choose 1-3: """

        userInput = input(retrieveVoyagesMenu)
        if userInput == "1":
            self.outputclass.printVoyages()
        if userInput == "2":
            pass
        if userInput == "3":
            ssn = self.inputclass.getSSN()
            self.outputclass.printWorkSchedule(ssn)

    
    def retrieveCrewMenu(self):
        print("###\nRETRIEVE DATA -> CREW\n###")
        retrieveCrewMenu = """

    1. All Crew
    2. Available Crew
    3. Unavailable Crew
    4. Crew Member by SSN

    b - go back

    Choose 1-4: """

        userInput = input(retrieveCrewMenu)
        if userInput == "1":
            self.outputclass.printAllStaff()
        elif userInput == "2":
            date = self.inputclass.getDate()
            self.outputclass.printAvailableStaff(date)
        elif userInput == "3":
            date = self.inputclass.getDate()
            self.outputclass.printUnavailableStaff(date)
        elif userInput == "4":
            ssn = self.inputclass.getSSN()
            self.outputclass.printStaffMember(ssn)
        elif userInput == "b":
            return 0
    

    """
    Update
    """


    def updateMenu(self):
        print("###\nUPDATE DATA\n###")
        updateMenu = """

    1. Crew member info
    2. Destination info

    b - go back
    
    Choose 1-2: """
        userInput = input(updateMenu)
        if userInput == '1':
            self.updateCrewMenu()
        elif userInput == '2':
            self.updateDestinationMenu()
        elif userInput == 'b':
            return 0
    
    def updateCrewMenu(self):
        print("###\nUPDATE DATA -> CREW MEMBER INFO\n###")

        userInput = self.inputclass.getSSN()

        if userInput == 'b':
            return
        
        return userInput

    def updateCrewMenuSSN(self, ssn):
        print("###\nUPDATE DATA -> CREW MEMBER INFO -> {}\n###""".format(ssn))
        print("Leave blank if you do not want to update.")

        updatedInfo = self.inputclass.getUpdateStaffInput()

        return updatedInfo

    def updateDestination(self):
        pass






# class UserExperienceOutPutInputMeter:

#     def __init__(self):
#         stringToPrint = """

#     1. Register data
#     2. Retrieve data
#     3. Update data

#     q - Quit program

#     Choose 1-3:"""

#         userInput = input(stringToPrint)
#         if userInput == "1":
#             self.registerMenu() ## register
#         elif userInput == "2":
#             self.retreiveMenu() ## Retreive
#         elif userInput == "3":
#             self.updateMenu() ## Update

#         elif userInput == "q":
#             return

#     def registerMenu(self):
#         print("hello")
#         userInput = input("""
#     ###
#     REGISTER DATA
#     ###

#     1. Voyage
#     2. Assign crew to voyage.
#     3. Assign airplane to voyage
#     4. Crew member
#     5. Destination.
#     6. Airplane

#     b - go back
#     m - main menu

#     Choose 1-5:


#     """)
        
#         if userInput == "1":
#             self.registerVoyage()
#         elif userInput == '2':
#             self.registerCrewToVoyage()
#         elif userInput == '3':
#             self.registerAirplaneToVoyage()
#         elif userInput == '4':
#             self.registerCrew()
#         elif userInput == '5':
#             self.registerDestination()
#         elif userInput == '6':
#             self.registerAirplase()
#         elif userInput == "b":
#             return

#         def registerVoyage(self):

#             print("""###
#     REGISTER DATA -> VOYAGE
#     ###""")
#             print("if any line is empty it will not get registered")
#             destination = input('Destination: ')
#             departureFromIceland = input('Departure from Iceland: ')
#             departureFromDestination = input('Departure from destination: ')

#             print("function not implemented, returning")

#             return

#     def registerCrewMember(self):
#         print("""###
# REGISTER DATA -> CREW
# ###""")
#         ssn = input('Social security number: ')
#         name = input('Name: ')
#         phone = input('Phone number: ')
#         email = input('Email: ')
#         address = input('Residence: ')

#         print("function not available, returning")
#     def registerDestination(self):
#         print("""###
# REGISTER DATA -> DESTINATION
# ###""")
#         destination = input('Destination: ')
#         country     = input('Country: ')
#         airport     = input('Airport: ')
#         timeOfFlight = input('Time of flight: ')
#         DistanceFromIceland = input('Distance from Iceland: ')
#         contact = input('Contact: ')
#         contactsNumber = input('Contacts phonenumber: ')
#         emergencyNumber = input('Emergency number: ')
#         print("function not available")
#         return








#     def retreiveMenu(self):
#         userInput("""
#     ###
#     RETRIEVE DATA
#     ###

#     1. Crew
#     2. Airplanes
#     3. Destinations
#     4. Voyage

#     b - go back

#     Choose 1-5:""")

#         if userInput == "1":
#             pass
#         elif userInput == '2':
#             pass
#         elif userInput == '3':
#             pass
#         elif userInput == '4':
#             pass
#         elif userInput == 'b':
#             return



#     def updateMenu(self):
#         userInput = input("""

#     ###
#     UPDATE DATA
#     ###

#     1. Crew member info
#     2. Destination info

#     b - go back
#     """)

#         if userInput == '1':
#             self.updateCrewMenu()
#         elif userInput == '2':
#             self.updateDestinationMenu()
#         elif userInput == 'b':
#             return 0

#     def updateCrewMenu(self):
#         print("""
#     #
#     UPDATE DATA -> CREW MEMBER INFO
#     #""")

#         userInput = input('Enter members SSN, or b to return')


#         if userInput == 'b':
#             return
#         elif len(userInput) == 10:  ## it's ssn
#             self.updateCrewMenuSSN(userInput)
#         else:
#             print("not a real ssn")
#             return


#     def updateCrewMenuSSN(self, ssn):
#         print("""
# #
# UPDATE DATA -> CREW MEMBER INFO -> {}
# #""".format(ssn))

#         print("Leave it empty if you don't want to update")
#         updatedNumber = input("Phone number:")

#         updatedRedidence = input("Residence:")

#         updatedEmail = input("Email:")

#         print("function not available")
#         return

#         ## check if parameters are not "" and pass those into logic to be processed.
#     def updateDestinationMenu(self):
#         pass


