from LogicLayer.logic_test import LogicLayerAPI

a = LogicLayerAPI()

<<<<<<< HEAD
for x in a.getAllCrewWorking('21/12/2019'):
    print(x.name, x.ssn)

print('\n####### NOT WORKING #######\n')

for x in a.getAllCrewNotWorking('21/12/2019'):
    print(x.name, x.ssn)
=======
print('##### WORKING ######')

for x in a.getAllCrewWorking('21/12/2019'):
    print(x.name, x.ssn, x.destination)

print('###### NOT WORKING ######')

for x in a.getAllCrewNotWorking('21/12/2019'):
     print(x.name, x.ssn)
for x in a.getAllPilotsAfterLicenseOnAircraft('TF-EPG', 'Copilot'):
    print(x.name, x.ssn, x.role, x.rank)
>>>>>>> c8e58cf02c07bbe7952daca492de3c826d8b77f9
