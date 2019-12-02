class aeroport:
	def __init__(self):  ## probably going to have no parameters when created, but
	 				     ## when the 
		pass




class Airplane:
	def __init__(self):
		pass


class Crew:
	def __init__(self, name, ssn, address, phone, homephone):
		self.name = name
		self.ssn = ssn
		self.address = address
		self.phone = phone
		self.homephone = homephone


class pilotNode(Crew):
	def __init__(self, name , ssn , address , phone , homephone, rank = None, privileges = None ):
		super().__init__(name , ssn , address , phone , homephone)
		self.rank = rank
		self.privileges = privileges

	def __str__(self):
		return str(self.ssn)

class flightAttendantNode(Crew):
	def __init__(self, name, ssn, address, phone, homephone, isboss, rank):
		super().__init__(name, ssn, address, phone, homephone)
		self.isboss = isboss
		self.rank = rank


class peeps: ## store people in a hash map
	def __init__(self):
		self.cap = 16
		self.buckets = [ [] ] * self.cap

	def insertpilot(self, name, ssn, address, phone, homephone):
		node = pilotNode(name, ssn, address, phone, homephone)
		index = hash(name) % self.cap
		if node in self.bucket[index]:
			pass
			# update
		else:
			self.bucket[index].append(node)

	def contains(self, name, ssn):
		out = False
		index = hash(name) % self.cap
		for x in self.buckets[index]:
			if x.ssn is ssn:
				out = True

		return out



