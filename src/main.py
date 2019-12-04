from LogicLayer.logic_test import LogicLayerAPI


a = LogicLayerAPI()

for x in a.getAllCrewList():
    print(x.name)

for x in a.getAllDestinationsList():
    print(x.destination)