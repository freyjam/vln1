from LogicLayer.logic_test import LogicLayerAPI

a = LogicLayerAPI()

#for x in a.listOfAllAircraftsWithState():
#    print(x.state, x.availableAt, x.destination, x.numberOfFlight)

for x in a.getAllCrewWorking('21/12/2019'):
    print(x.name, x.destination)
