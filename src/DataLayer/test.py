import classes
import csv

Datalayerapi = classes.DataLayerAPI()

with open('Crew.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
        	Datalayerapi.createUserPilot(row[1],row[0], None, None, None, row[2], row[3], row[4] )



out = Datalayerapi.retrieveCrew()
for x in out:
	print(x.name, x.ssn)

# print(Datalayerapi.getSpecificEmployee('3009907461').name)