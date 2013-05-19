# -*-coding:Utf-8 -*

class Pipe(object):
	"""Classe qui défini les propritétés et les connexions d'un tuyau.
	Attributs:
	- id
	- columnNbr : int
	- startingNode : Node
	- endingNode : Node
	- valveAtStart : bool
	- valveAtEnd : bool

	"""
	def __init__(self, inStartingNode, inEndingNode):
		super(Pipe, self).__init__()
		self.id = (inStartingNode.id, inEndingNode.id)
		self.startingNode = inStartingNode
		self.endingNode = inEndingNode
		self.startingNode.add_pipe(self)
		self.endingNode.add_pipe(self)
		self.valveAtStart = False
		self.valveAtEnd = False
		
	def __hash__(self):
		return hash(self.id)
	
	def __eq__(self, other):
		if type(other) == Pipe:
			return self.id == other.id
		elif type(other) == str:
			return str(self.id) == other
		return False
		
	def __ne__(self, other):
		if type(other) == Pipe:
			return self.id != other.id
		elif type(other) == str:
			return str(self.id) != other
		return True
	
	def __repr__(self):
		return (self.id[0]+"--"++self.id[1])
	
	def __str__(self):
		return (self.id[0]+"--"+self.id[1])

	def set_valve_at_start(self, inValve): #ajoute ou retire une valve au début de self
		self.valveAtStart = inValve
		
	def set_valve_node_side(self, node, inValve): #ajoute ou retire une valve au début de self
		if self.startingNode == node:
			self.valveAtStart = inValve
		elif self.endingNode == node:
			self.valveAtEnd = inValve
		
	def set_valve_at_end(self, inValve): #ajoute ou retire une valve à la fin de self
		self.valveAtEnd = inValve
		
	def get_valve_at_start(self):
		return self.valveAtStart
		
	def get_valve_at_end(self):
		return self.valveAtend
	
	def get_valve_at_both(self):
		return self.valveAtStart and self.valveAtEnd