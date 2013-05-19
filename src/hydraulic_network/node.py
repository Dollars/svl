# -*-coding:Utf-8 -*

from hydraulic_network.pipe import Pipe

class Node(object):
	"""Classe qui contient les informations sur un noeud
	Attributs:
	- id 
	- rowNbr : int
	- connectedPipes : liste de Pipe"""
	
	def __init__(self, inId):
		super(Node, self).__init__()
		self.id = inId
		self.connectedPipes = []
		
	def __hash__(self):
		return hash(self.id)
	
	def __eq__(self, other):
		return self.id == other
	
	def __repr__(self):
		return self.id
	
	def __str__(self):
		return self.id

	def add_pipe(self, inPipe): #connecte un tuyau à self
		self.connectedPipes.append(inPipe)
		
	def nbr_near_valves(self): #renvoie le nombre de valves proche du noeud
		toReturn=0
		for pipe in self.connectedPipes:
			if (self==pipe.startingNode and pipe.valveAtStart) or (self==pipe.endingNode and pipe.valveAtEnd):
				toReturn += 1
		return toReturn
		
	def set_valve_at_pipe(self, inPipe, inValve): #place ou retire une valve sur le tuyau inPipe près de self
		if (inPipe in self.connectedPipes):
			if inPipe.startingNode == self:
				inPipe.set_valve_at_start(inValve)
			else:
				inPipe.set_valve_at_end(inValve)
				
	def connected_nodes(self):
		connectedNodes = []
		for pipe in self.connectedPipes:
			if pipe.startingNode == self:
				connectedNodes.append(pipe.endingNode)
			else:
				connectedNodes.append(pipe.startingNode)
		return connectedNodes