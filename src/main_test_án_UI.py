from LogicLayer.logic_test import LogicLayerAPI

a = LogicLayerAPI()

<<<<<<< HEAD
print('##### WORKING ######')

for x in a.getAllCrewWorking('21/12/2019'):
    print(x.name, x.ssn, x.destination)

print('###### NOT WORKING ######')

for x in a.getAllCrewNotWorking('21/12/2019'):
     print(x.name, x.ssn)
=======
for x in a.getAllPilotsAfterLicenseOnAircraft('TF-EPG', 'Copilot'):
    print(x.name, x.ssn, x.role, x.rank)
>>>>>>> 8e6150241c0f25edd2063091c601e72801601754
