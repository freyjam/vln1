from DataLayer.DataLayer import DataLayerAPI

from operator import attrgetter
import datetime
from datetime import datetime
from datetime import date
from datetime import timedelta


class LogicLayerAPI:
    def __init__(self):
        self.instance = DataLayerAPI() #ATH þarf að breyta nafni! Okkur datt ekkert betra í hug
        #Og ath hvort að þetta virki og sé eins og á að gera

    def getAllCrewList(self):
        allCrewList = self.instance.getAllCrewFromFile()
        return allCrewList

    def getAllDestinationsList(self):
        ''''''
        allDestinationsList = self.instance.getAllDestinationsFromFile()
        allDestinationsList.sort(key=attrgetter('destination'))
        return allDestinationsList

    def getAllVoyages(self):
        allVoyagesList = self.instance.getAllVoyageFromFile()
        return allVoyagesList

    def getListofAllVoyages(self):
        allVoyagesList = self.getAllVoyages()
        for voyage in allVoyagesList:
            voyage.status = self.getVoyageStatus(voyage)
            voyage.departure = self.changeFromIsoTimeFormat(voyage.departure)                       # Date and time will be on the right form for printing
            voyage.departureFromDest = self.changeFromIsoTimeFormat(voyage.departureFromDest)
            voyage.arrivalAtDest = self.changeFromIsoTimeFormat(voyage.arrivalAtDest)
            voyage.arrival = self.changeFromIsoTimeFormat(voyage.arrival)
        return allVoyagesList

    def getAllVoyagesByDate(self, date):
        voyagesThatDate = []
        for voyage in self.getAllVoyages():
            departureDate, departureTime = self.changeFromIsoTimeFormat(voyage.departure)
            if departureDate == date:
                voyages.append(voyage)
        return voyagesThatDate

    

    def getVoyageStatus(self, voyage):
        time = self.getCurrentDateAndTimeISO()
        if voyage.departure > time:
            return 'Not started'
        elif voyage.departure <= time <= voyage.arrivalAtDest:
            return 'En route to destination'
        elif voyage.arrivalAtDest <= time <= voyage.departureFromDest:
            return 'Landed at destination'
        elif voyage.departureFromDest <= time <= voyage.arrival:
            return 'En route to Reykjavík'
        else:
            return 'Landed in Reykjavík'

    def registerNewCrewMember(self, instanceOfCrew):
        if self.isSSNValid(instanceOfCrew.ssn):
            if self.isPhoneNumberValid(instanceOfCrew.phone):
                if self.isEmailValid(instanceOfCrew.email):
                    return self.instance.addCrewToCSV(instanceOfCrew)
                else:
                    return 'Email is not valid'
            else:
                return 'Phone number is not valid'
        else:
            return 'SSN not Valid'

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

    def getAllCrewWorking(self, date):
        crewWorking = []
        voyagesList = self.getAllVoyages()
        firstTime = self.changeInputedDateAndTimeToIso(date, '00:00')
        secTime = self.changeInputedDateAndTimeToIso(date, '23:59')
        for voyage in voyagesList:
            if firstTime <= voyage.departure <= secTime or firstTime <= voyage.arrival <= secTime:
                for member in self.sortAllCrewAlpha():
                    if member.ssn in voyage.crew:
                        crewWorking.append(member)
                        member.destination = voyage.destinationAirport
        return crewWorking

    def getAllCrewNotWorking(self, date):
        allCrewList = self.sortAllCrewAlpha()
        allCrewWorkingList = [obj.ssn for obj in self.getAllCrewWorking(date)]
        for member in allCrewList:
            nr1 = member.ssn
            if nr1 in allCrewWorkingList:
                allCrewList.remove(member)                            # Removes all working Crew members from list
        return allCrewList


    def getCrewMemberBySsn(self, inputedSSN):
        '''Takes in a SSN inputed by user and returns 
        the object of the crew member that has that ssn'''
        for obj in self.getAllCrewList():
            if obj.ssn == inputedSSN:
                return obj

    def changeInputedDateAndTimeToIso(self, date, time='00:00'):
        '''Takes in a date on the form dd/mm/yyyy and a time on 
        the form 16:06 and returns the datetime on isoformat'''
        day, month, year = date.split('/')
        hours, minutes = time.split(':')
        dateTimeIso = datetime(int(year), int(month), int(day), int(hours), int(minutes), 0).isoformat()
        return dateTimeIso

    def changeFromIsoTimeFormat(self, isotime):
        '''Takes in isoformat from file, and returns date and time on
        the form year, month, day, hour, minutes'''
        year, month, day = isotime[:4], isotime[5:7] ,isotime[8:10]
        hour, minutes = isotime[11:13], isotime[14:16] 
        return day + '/' + month + '/' + year, hour + ':' + minutes

    def getAllAircrafts(self):
        '''Returns list of all aircrafts'''
        allAircraftList = self.instance.getAllAircraftInfoFromFile()
        return allAircraftList

    def getCurrentDateAndTimeISO(self):
        '''Returns the current date and time on iso format'''
        hours, minutes = str(datetime.now().strftime('%H:%M')).split(':')
        year, month, day = str(date.today()).split('-')
        return datetime(int(year), int(month), int(day), int(hours), int(minutes), 0).isoformat()

    def listOfAllAircraftsWithState(self, date, time):
        '''Returns a list  of all aircrafts and adds their state and state info to the instance'''
        listOfAircrafts = self.getAllAircrafts()
        listOfVoyages = self.getAllVoyages()
        time = self.changeInputedDateAndTimeToIso(date, time)
        for aircraft in listOfAircrafts:
            for voyage in listOfVoyages:
                if aircraft.insignia == voyage.aircraft:
                    if voyage.departure <= time <= voyage.arrival:
                        aircraft.state = 'Unavailable'
                        aircraft.availableAt = self.changeFromIsoTimeFormat(voyage.arrival)
                        aircraft.destination = voyage.destinationAirport
                        if voyage.departure <= time <= voyage.arrivalAtDest:
                            aircraft.numberOfFlight = voyage.outboundFlightNumber
                        elif voyage.departureFromDest <= time <= voyage.arrival:
                            aircraft.numberOfFlight = voyage.inboundFlightNumber
        return listOfAircrafts

    def getWorkScheduleForCrewMember(self, ssn):
        startTime = self.getCurrentDateAndTimeISO()
        endTime = self.reverseIsoformat(startTime, 'days', 7)
        crewMembersVoyagesList = []
        crewMember = self.getCrewMemberBySsn(ssn)
        voyagesList = self.getAllVoyages()
        for voyage in voyagesList:
            if startTime <= voyage.departure <= endTime or startTime <= voyage.arrival <= endTime:
                if crewMember.ssn in voyage.crew:
                    crewMembersVoyagesList.append(voyage)
                    voyage.departure = self.changeFromIsoTimeFormat(voyage.departure)
                    voyage.arrival = self.changeFromIsoTimeFormat(voyage.arrival)
        return crewMember, crewMembersVoyagesList

    def addToIsoFormat(self, isotime, whatToChange, howMany): 
        dateTest = isotime[:4] + isotime[5:7] + isotime[8:10] + isotime[11:13] + isotime[14:16]
        if whatToChange == 'days':
            newTime = (datetime.strptime(str(dateTest),"%Y%m%d%H%M") + timedelta(days=howMany)).strftime("%Y%m%d%H%M")
        elif whatToChange =='hours':
            newTime = (datetime.strptime(str(dateTest),"%Y%m%d%H%M") + timedelta(minutes=howMany)).strftime("%Y%m%d%H%M")
        year, months, days, hours, minutes = newTime[:4], newTime[4:6], newTime[6:8], newTime[8:10], newTime[10:12]
        return datetime(int(year), int(months), int(days), int(hours), int(minutes)).isoformat()

    def getAllPilotsAfterLicenseOnAircraft(self, aircraftInsignia, rank):
        returnList = []
        for aircraft in self.getAllAircrafts():
            if aircraft.insignia == aircraftInsignia:
                aircraftTypeID = aircraft.typeID
        for pilot in self.sortAllPilotsAlpha():
            if pilot.rank == rank:
                if pilot.license == aircraftTypeID:
                    returnList.append(pilot)
        return returnList

    def getAllAvailebleCrewMembersForVoyage(self, voyage, rank):
        returnAvailableCrewList = []
        departureDate, departureTime = self.changeFromIsoTimeFormat(voyage.departure)
        arrivalDate, arrivalTime = self.changeFromIsoTimeFormat(voyage.arrival)
        if departureDate == arrivalDate:
            availableCrew = self.getAllCrewNotWorking(departureDate)
        else:
            availableCrewDepartureDate = {self.getAllCrewNotWorking(departureDate)}                 # If voyage ends after midnight a crew member that is unavailable the next day is not available
            availableCrewArrivalDate = {self.getAllCrewNotWorking(arrivalDate)}
            availableCrew = intersection(availableCrewDepartureDate, availableCrewArrivalDate)
        if rank == 'Captain' or rank == 'Copilot':                                                  # When finding pilot, license have to be checked
            for pilot in self.getAllPilotsAfterLicenseOnAircraft(voyage.aircraft, rank):
                if pilot.ssn in [member.ssn for member in availableCrew]:
                    returnAvailableCrewList.append(pilot)
        else:
            for member in availableCrew:
                if member.rank == rank:
                    returnAvailableCrewList.append(member)                  #OF STÓRT FALL????
        return returnAvailableCrewList






















    def getTimingsForVoyage(self, destination, departureDate, departureTime):
        if isTimeFormatValid(departureDate, departureTime):
            departureISO = self.changeInputedDateAndTimeToIso(departureDate, departureTime)
            if isAirportAvailable(departureTime):
                arrivalAtDestISO = self.addToIsoFormat(departure, 'hours', destination.distanceFromIceland)
                departureFromDestISO = self.addToIsoFormat(arrivalAtDest, 'hours', 1)
                arrivalISO = self.addToIsoFormat(departureFromDest, 'hours', destination.distanceFromIceland)
                if isAirportAvailable(arrival):
                    return departureISO, arrivalAtDestISO, departureFromDestISO, arrivalISO

    def getNextFlightNumbers(self, priorFlightNumberOut, priorFlightNumberIn):
        firstPartOut, secondPartOut = priorFlightNumberOut[:4], int(priorFlightNumberOut[4])
        newFlightNumberOut = firstPartOut + str(secondPartOut + 2)

        firstPartIn, secondPartIn = priorFlightNumberIn[:4], int(priorFlightNumberIn[4])
        newFlightNumberIn = firstPartIn + str(secondPartIn + 2)

        return newFlightNumberOut, newFlightNumberIn

    
    def getFlightNumbersForVoyage(destination, departureISO):
        departureDate, departureTime = self.changeFromIsoTimeFormat(departureISO)
        for voyage in self.getAllVoyagesByDate(departureDate):
            if voyage.destinationAirport == destination.airport:
                if departureISO < voyage.departure:
                    outboundFlightNumber = voyage.outboundFlightNumber
                    inboundFlightNumber = voyage.inboundFlightNumber
                    voyage.outboundFlightNumber, voyage.inboundFlightNumber = getNextFlightNumbers(voyage.outboundFlightNumber, voyage.inboundFlightNumber)
                    #Hér er kallað á fall sem update-ar voyage.csv og bætir þessum nýju flugnúmerum við







