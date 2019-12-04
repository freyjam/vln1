class Voyage: 
	def __init__(self, destination, departureFromIceland, departureFromDestination):
		self.airplane = ""
		self.destination = destination
		self.departureFromIceland = departureFromIceland
		self.departureFromDestination = departureFromDestination
        

		## todo
        ## ENDURSKOÐA ÞENNAN KLASA VARÐANDI WIREFRAMES ÞAR SEM FLUGVÉL ER T.D. VALIN
        # STARFSFÓLK ER VALIÐ, FLUGNÚMER REIKNAST ÚT SKJÁLFKRAFA OG ÞARF AÐ VERA HÆGT AÐ BREYTA
        # EF ÖÐRU FLUGI ER BÆTT VIÐ Á UNDAN Á SAMA DEGI
        # KANNSKI ÞARF EKKI AÐ HAFA MODELKLASA FYRIR HVERJA FLUGFERÐ SKOÐA ÞETTA BETUR