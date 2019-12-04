import DataLayer.classes

import csv

from operator import attrgetter

class LogicLayerAPI:

    def getAllCrewList(self):
        allCrew = classes.DataLayerAPI()
        allCrew.loadObjectFromClass()
        allCrewList = allCrew.retrieveCrew()
        return allCrewList

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

    def getCrewMemberBySsn(self, Ssn):
        allCrewList = self.getAllCrewList()
        specialCrewMember = ""
        for obj in self.getAllCrewList():
            if obj == Ssn:
                specialCrewMember = obj



