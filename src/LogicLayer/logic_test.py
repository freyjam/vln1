from DataLayer.classes import DataLayerAPI

from operator import attrgetter

class LogicLayerAPI:

    def getAllCrewList(self):
        allCrew = DataLayerAPI()
        allCrew.loadObjectFromClass()
        allCrewList = allCrew.retrieveCrew()
        return allCrewList

    def getAllDestinationsList(self):
        allDestinations = DataLayerAPI()
        allDestinationsList = allDestinations.getAllDestinationsFromFile()
        allDestinationsList.sort(key=attrgetter('destination'))
        return allDestinationsList

    def sortAllCrewAlpha(self):
        allCrewList = self.getAllCrewList()
        allCrewList.sort(key=attrgetter('name'))
        return allCrewList

    def sortAllPilotsAlpha(self):
        allPilotsList = []
        for obj in self.getAllCrewList():
            if obj.role == 'Pilot':
                allPilotsList.append(obj)
        allPilotsList.sort(key=attrgetter('name'))
        return allPilotsList

    def sortAllPilotsBylicense(self):
        allPilotsList = self.sortAllPilotsAlpha()
        allPilotsList.sort(key=attrgetter('license'))
        return allPilotsList
    
    def sortAllCabincrewAlpha(self):
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

    def getCrewMemberBySsn(self, ssn):
        for obj in self.getAllCrewList():
            if obj.ssn == ssn:
                return obj

