from LogicLayer.logic_test import LogicLayerAPI

a = LogicLayerAPI()

#for x in a.listOfAllAircraftsWithState():
#    print(x.state, x.availableAt, x.destination, x.numberOfFlight)

print('Working')

for x in a.getAllCrewWorking('21/12/2019'):
    print(x.name, x.ssn, x.destination)

print('Not working')

for x in a.getAllCrewNotWorking('21/12/2019'):
    print(x.name, x.ssn, x.destination)

print('Schedule for 1900769521')

crewMember, voyages = a.getWorkScheduleForCrewMember('1900769521', '19/12/2019', '24/12/2019')
print('Name: {} SSN: {}'.format(crewMember.name, crewMember.ssn))
for x in voyages:
    print('Destination: {} Departure: {}  Arrival: {}'.format(x.destinationAirport, a.changeFromIsoTimeFormat(x.departure), a.changeFromIsoTimeFormat(x.arrival)))