import sys
sys.path.append('../data')
import classes

crew = classes.DataLayerAPI()

crew.createUserPilot("bla", "1233", "blalba5", "ergfg", 'lksjfdgn', "kashdf", 'ljkkj', 'khbsfgj')

a = crew.retrieveCrew()

print(a[0].ssn)

