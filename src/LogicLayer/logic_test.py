from DataLayer.classes import DataLayerAPI

from operator import attrgetter
import datetime
from datetime import datetime
from datetime import date


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

    def getAllVoyages(self):
        allVoyagesList = self.instance.getAllVoyageFromFile()
        return allVoyagesList

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

    def changeFromIsoTimeFormat(self, isotime):
        '''Takes in isoformat from file, and returns date and time on
        the form year, month, day, hour, minutes'''
        year, month, day = isotime[:4], isotime[5:7] ,isotime[8:10]
        hour, minutes = isotime[11:13], isotime[14:16] 
#        isoTimeChange = int(year), int(month), int(day), int(hour), int(minutes)
        return day + '/' + month + '/' + year, hour + ':' + minutes

    def getAllAircrafts(self):
        allAircraftList = self.instance.getAllAircraftInfoFromFile()
        return allAircraftList

    def getCurrentDateAndTimeISO(self):
        hours, minutes = str(datetime.now().strftime('%H:%M')).split(':')
        year, month, day = str(date.today()).split('-')
        return datetime(int(year), int(month), int(day), int(hours), int(minutes), 0).isoformat()

    def listOfAllAircraftsWithState(self):
        listOfAircrafts = self.getAllAircrafts()
        listOfVoyages = self.getAllVoyages()
        currentDatetime = self.getCurrentDateAndTimeISO()
        for aircraft in listOfAircrafts:
            for voyage in listOfVoyages:
                if aircraft.insignia == voyage.aircraft:
                    if voyage.departure <= currentDatetime <= voyage.arrival:
                        aircraft.state = 'Buzy'
                        aircraft.availableAt = self.changeFromIsoTimeFormat(voyage.arrival)
                        aircraft.destination = voyage.destinationAirport
                        if voyage.departure <= currentDatetime <= voyage.arrivalAtDest:
                            aircraft.numberOfFlight = voyage.outboundFlightNumber
                        elif voyage.departureFromDest <= currentDatetime <= voyage.arrival:
                            aircraft.numberOfFlight = voyage.inboundFlightNumber
        return listOfAircrafts