# -*-coding:Utf-8 -*

from hydraulic_network.node import Node
from hydraulic_network.pipe import Pipe
from math import sqrt
from compiler.ast import Print
import copy
import pipes

class Network(object):
	"""Contient les information d'un réseau.
	Attributs:
	- nodes : liste de nodes
	- pipeMap : liste de pipeMap"""
	
	def __init__(self, inId, dotFilePath="none"): #construit le graphe a partir d'un fichier DOT
		super(Network, self).__init__()
		
		self.id=inId;
		
		self.nbrNodes = 0
		self.nbrPipes = 0
		
		self.nodeMap = dict()
		self.pipeMap = dict()

		if dotFilePath != "none":
			lecture = open(dotFilePath, "r")
			
			for i in lecture:
				lineNodes = i[:-2].split(" ")
				firstNode = Node(lineNodes.pop(0))
				if not self.is_in_nodes(firstNode):
					self.add_node(firstNode)
				else:
					firstNode = self.get_node_by_id(firstNode.id)
				
				for pipeInfo, nodeID in zip(lineNodes[0::2], lineNodes[1::2]):
					secondNode = Node(nodeID)
					if not self.is_in_nodes(secondNode):
						self.add_node(secondNode)
					else:
						secondNode = self.get_node_by_id(secondNode.id)
					currPipe = Pipe(firstNode, secondNode)
					if pipeInfo[0] == "|":
						currPipe.set_valve_node_side(firstNode, True)
					if pipeInfo[1] == "|" :
						currPipe.set_valve_node_side(secondNode, True)
					self.add_pipe(currPipe)
					firstNode = secondNode
			lecture.close
		
		self.networkMatrix = NetworkMatrix(self)
		self.valveLocationMatrix = ValveLocationMatrix(self)
		self.valveDeficiencyMatrix = ValveDeficiencyMatrix(self)
	
	def is_in_nodes(self, node):
		for currNode in self.nodeMap.values():
			if currNode == node:
				return True
		return False
				
	def get_node_by_id(self, inId):
		for currNode in self.nodeMap.values():
			if currNode.id == inId:
				return currNode
	
	def get_valve_count(self):
		valveCount = 0
		for valveIter in range(self.nbrPipes):
			if self.pipeMap[valveIter].valveAtStart:
				valveCount += 1
			if self.pipeMap[valveIter].valveAtEnd:
				valveCount += 1
		return valveCount
			
	def __str__(self):
		string = ""
		for node in self.nodeMap.values():
			for connectedNode in node.connected_nodes():
				string += (node.id + " -- "+ connectedNode.id)
		return string
	
	def str_elements(self):
		string = "Nodes: "
		for node in self.nodeMap.values():
			string += node.id+" "
		string += "\n"
		string += "Pipes: "
		for pipe in self.pipeMap.values():
			string += str(pipe)+" "
		string +="\n"
		return string
				
	def set_valves(self, valvesCode):
		"""Méthode permettant de positionner les valves selon un
			vecteur"""
		if len(valvesCode) != 2*self.nbrPipes:
			print("Erreur, longueur du code génétique invalide")
		else:
			for i in range(self.nbrPipes):
				if valvesCode[i*2] == 1:
					self.pipeMap[i].set_valve_at_start(True)
				elif valvesCode[i*2] == 0:
					self.pipeMap[i].set_valve_at_start(False)
				
				if valvesCode[i*2+1] == 1:
					self.pipeMap[i].set_valve_at_end(True)
				elif valvesCode[i*2+1] == 0:
					self.pipeMap[i].set_valve_at_end(False)
			self.update()
								
	def add_node(self, inNode, key = -1):
		if key > -1:
			self.nodeMap[key] = inNode
		else:
			self.nodeMap[self.nbrNodes] = inNode
		self.nbrNodes+=1
		
	def add_pipe(self, inPipe, key = -1):
		if key > -1:
			self.pipeMap[key] = inPipe
		else:
			self.pipeMap[self.nbrPipes] = inPipe
		self.nbrPipes+=1

	def __len__(self):
		return len(self.nbrPipes)
	
	def update(self):
		self.networkMatrix.update(self)
		self.valveLocationMatrix.update(self)
		self.valveDeficiencyMatrix.update(self)

		
class NetworkMatrix(object):
	
	def __init__(self, inNetwork): 
		super(NetworkMatrix, self).__init__()
		
		self.network = inNetwork
		self.rowNbr = inNetwork.nbrNodes
		self.columnNbr = inNetwork.nbrPipes
		self.matrix = [ [ 0 for i in range(self.columnNbr) ] for j in range(self.rowNbr) ]
		self.update(inNetwork)

	def __str__(self):
		string = ""
		string += str(len(self.network.pipeMap))+'\n'
		string += str(self.network.pipeMap.values())+'\n'
		for i,v in enumerate(self.matrix):
			string += self.network.nodeMap.values()[i].id + str(v) + "\n"
		return string
		
	def get_value(self, inRow, inColumn):
		return self.matrix[inRow][inColumn]
	
	def update(self, inNetwork):	
		for row in range(inNetwork.nbrNodes):
			currNode = inNetwork.nodeMap[row]
			for column in range(self.columnNbr):
				currPipe = inNetwork.pipeMap[column]
				if currPipe in currNode.connectedPipes:
					self.matrix[row][column] = 1
			
class ValveLocationMatrix(object):
	
	def __init__(self, inNetwork):
		super(ValveLocationMatrix, self).__init__()
		self.network = inNetwork
		self.rowNbr = inNetwork.nbrNodes
		self.columnNbr = inNetwork.nbrPipes
		self.matrix = [ [ 0 for i in range(self.columnNbr) ] for j in range(self.rowNbr) ]
		self.update(inNetwork)
					
	def __str__(self):
		string = ""
		for i in self.matrix:
			string = string + str(i) + "\n"
		return string
	
	def update(self, inNetwork):
		self.matrix = [ [ 0 for i in range(self.columnNbr) ] for j in range(self.rowNbr) ]
		for row in range(self.rowNbr):
			currNode = inNetwork.nodeMap[row]
			for column in range(self.columnNbr):
				currPipe = inNetwork.pipeMap[column]
				if (currPipe.startingNode == currNode and currPipe.valveAtStart) or (currPipe.endingNode == currNode and currPipe.valveAtEnd):
					self.matrix[row][column] = 1					
	
	def get_value(self, inRow, inColumn):
		return self.matrix[inRow][inColumn]
		
class ValveDeficiencyMatrix(object):
		
	def __init__(self, inNetwork):
		super(ValveDeficiencyMatrix, self).__init__()
		self.network = inNetwork
		self.rowNbr = inNetwork.nbrNodes
		self.columnNbr = inNetwork.nbrPipes
		self.matrix = [ [ 0 for i in range(self.columnNbr) ] for j in range(self.rowNbr) ]
		self.update(inNetwork)
		
	def __str__(self):
		string = ""
		for i in self.matrix:
			string = string + str(i) + "\n"
		return string
	
	def get_value(self, inRow, inColumn):
		return self.matrix[inRow][inColumn]
	
	def update(self, inNetwork):
		self.matrix = [ [ 0 for i in range(self.columnNbr) ] for j in range(self.rowNbr) ]
		for i in range(self.rowNbr):
			for j in range(self.columnNbr):
				self.matrix[i][j] = inNetwork.networkMatrix.get_value(i, j) - inNetwork.valveLocationMatrix.get_value(i, j)
