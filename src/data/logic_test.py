import classes

import csv

from operator import attrgetter

all_crew = classes.DataLayerAPI()

all_crew.loadObjectFromClass()

all_crew.sort(key=attrgetter('name'))

print(all_crew)










