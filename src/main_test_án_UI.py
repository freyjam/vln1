from LogicLayer.logic_test import LogicLayerAPI

a = LogicLayerAPI()

for x in a.getAllPilotsAfterLicenseOnAircraft('TF-EPG', 'Copilot'):
    print(x.name, x.ssn, x.role, x.rank)