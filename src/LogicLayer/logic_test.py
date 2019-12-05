from DataLayer.classes import DataLayerAPI

from operator import attrgetter
import datetime

class LogicLayerAPI:
    def __init__(self):
        self.instance = DataLayerAPI() #ATH þarf að breyta nafni! Okkur datt ekkert betra í hug
        #Og ath hvort að þetta virki og sé eins og á að gera

    def getAllCrewList(self):
        self.instance.loadObjectFromClass()
        allCrewList = allCrew.retrieveCrew()
        return allCrewList

    def getAllDestinationsList(self):
        ''''''
        allDestinationsList = self.instance.getAllDestinationsFromFile()
        allDestinationsList.sort(key=attrgetter('destination'))
        return allDestinationsList

    def sortAllCrewAlpha(self):
        '''Sorts list of all crew alphabetically'''
        allCrewList = self.getAllCrewList()
        allCrewList.sort(key=attrgetter('name'))
        return allCrewList

    def sortAllPilotsAlpha(self):
        '''Finds all pilots from a list of all crew 
        and returns a list of them sorted alphabetically'''
        allPilotsList = []
        for obj in self.getAllCrewList():
            if obj.role == 'Pilot':
                allPilotsList.append(obj)
        allPilotsList.sort(key=attrgetter('name'))
        return allPilotsList

    def sortAllPilotsBylicense(self):
        '''Returns a list of all piots sorted by license'''
        allPilotsList = self.sortAllPilotsAlpha()
        allPilotsList.sort(key=attrgetter('license'))
        return allPilotsList
    
    def sortAllCabincrewAlpha(self):
        '''Finds all Cabincrew from a list of all crew 
        and returns a list of them sorted alphabetically'''
        allCabincrewList = []
        for obj in self.getAllCrewList():
            if obj.role == 'Cabincrew':
                allCabincrewList.append(obj)
        allCabincrewList.sort(key=attrgetter('name'))
        return allCabincrewList
    
    def getAllCrewNotWorking(self, date):
        pass

    def getAllCrewWorking(self, date):
        pass

    def getCrewMemberBySsn(self, inputedSSN):
        '''Takes in a SSN inputed by user and returns 
        the object of the crew member that has that ssn'''
        for obj in self.getAllCrewList():
            if obj.ssn == inputedSSN:
                return obj

    def changeInputedDateAndTimeToIso(self, date, time):
        '''Takes in a date on the form dd/mm/yyyy and a time on 
        the form 16:06 and returns the datetime on isoformat'''
        day, month, year = date.split('/')
        hours, minutes = time.split(':')
        dateTimeIso = datetime.datetime(int(year), int(month), int(day), int(hours), int(minutes), 0).isoformat()
        return dateTimeIso
<<<<<<< HEAD
=======
    
    def changeIsoTimeFormat(self, isotime):
        year, month, day = isotime[:4], isotime[5:7] ,isotime[8:10]
        hour, minutes = isotime[11:13], isotime[14:18] 
        isoTimeChange = int(year), int(month), int(day), int(hour), int(minutes)
        return isoTimeChange
>>>>>>> f655e1587c43a9cb4d9e972b3dc634cb02ce301b
