from LogicLayer.logic_test import LogicLayerAPI

a = LogicLayerAPI()

for x in a.getAllVoyage():
    print(x.destinationAirport, x.departure, x.arrivalAtDest)