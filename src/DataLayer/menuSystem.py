class node:
	def __init__(self, string = None, parent = None):
		self.string = string
		self.parent = parent # is None if node is root
		self.children = [] # list of nodes.
	def __str__(self):
		return str(self.string)

class Tree:
	def __init__(self):
		self.root = node()
		self.root.string = """

1. Register data
2. Retrieve data
3. Update data

q - Quit program
		"""
		self.current = self.root


	def insert(self, string):
		tempNode = node(string, self.current)

	def moveup(self):
		if self.current.parent:
			self.current = self.current.parent
	def movedown(self, index):
		if len(self.current.children) >= index:
			self.current = self.current.children[index]



## gotta hardcode the menu.
## but it's possible to change it pretty easily
