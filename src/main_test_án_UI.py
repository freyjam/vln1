from LogicLayer.logic_test import LogicLayerAPI

a = LogicLayerAPI()

for x in a.getAllCrewWorking('21/12/2019'):
    print(x.name, x.ssn)

print('\n####### NOT WORKING #######\n')

for x in a.getAllCrewNotWorking('21/12/2019'):
    print(x.name, x.ssn)