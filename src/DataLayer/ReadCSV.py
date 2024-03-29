class ReadCSV:
    def openFileForReading(self, filename):
        try:
            fileStream = open(filename, 'r')
            return fileStream
        except FileNotFoundError:
            return None

    def getAllDestinationsFromFile(self):
            '''Reads all info about destinations from file and returns a list of destination instances'''
            allDestinationsList = []
            lineCounter = 0
            destFileStream = self.openFileForReading('csv/Destinations.csv')
            if destFileStream:
                for line in destFileStream:
                    if lineCounter == 0:
                        lineCounter += 1
                    else:
                        destination, country, airport, distance, contact, emergencyNumber = line.strip().split(',')
                        allDestinationsList.append(Destination(destination, country, airport, distance, contact, emergencyNumber))
                return allDestinationsList
    
    def getAllAircraftInfoFromFile(self):
        '''Reads all info about aircrafts from file and returns a list of Aircraft instances'''
        aircraftsList = []
        lineCounter = 0
        aircraftFileStream = self.openFileForReading('csv/Aircraft.csv')
        if aircraftFileStream:
            for line in aircraftFileStream:
                if lineCounter == 0:
                    lineCounter += 1
                else:
                    insignia, typeId, capacity = line.strip().split(',')
                    aircraftsList.append(Aircraft(insignia, typeId, capacity))
            return aircraftsList

    def getAllCrewFromFile(self):
        '''Reads all info about crew from file and returns a list of crew instances'''
        allCrewList = []
        lineCounter = 0
        CrewFileStream = self.openFileForReading('csv/Crew.csv')
        if CrewFileStream:
            for line in CrewFileStream:
                if lineCounter == 0:                                    # So that instance will not be made out of header line
                    lineCounter += 1
                else:
                    ssn, name, role, rank, license, address, phone, email = line.strip().split(',')
                    allCrewList.append(Crew(ssn, name, role, rank, license, address, phone, email))
            return allCrewList
        
    def getAllVoyageFromFile(self):
        allVoyagesList = []
        lineCounter = 0
        VoyageFileStream = self.openFileForReading('csv/Voyage.csv')
        if VoyageFileStream:
            for line in VoyageFileStream:
                if lineCounter == 0:
                    lineCounter +=1
                else:
                    voyageFileList = line.strip().split(',')
                    allVoyagesList.append(Voyage(voyageFileList[0], voyageFileList[1], voyageFileList[2], voyageFileList[3], voyageFileList[4], voyageFileList[5], voyageFileList[6], voyageFileList[7], voyageFileList[8], voyageFileList[9:]))
            return allVoyagesList

