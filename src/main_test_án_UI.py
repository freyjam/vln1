from LogicLayer.logic_test import LogicLayerAPI

a = LogicLayerAPI()

for x in a.listOfAllAircraftsWithState():
    print(x.state, x.availableAt, x.destination, x.numberOfFlight)