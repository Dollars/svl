# -*-coding:Utf-8 -*

'''
Created on 13 déc. 2012

@author: jwillaim
'''

from hydraulic_network.networks import Network
from hydraulic_network.valve import Valve
import copy

class SegmentValveGraph(object):
	
	def __init__(self, inNetwork):
		super(SegmentValveGraph, self).__init__()
		
		self.segmentMap = dict()
		self.valveMap = dict()
		self.segmentNbr = 0
		self.valveNbr = 0
		
		self.nodes = copy.copy(inNetwork.nodeMap)
		self.pipes = copy.copy(inNetwork.pipeMap)
		
		self.nodesExplored = []
		self.pipesExplored = []

		self.defMatrix = inNetwork.valveDeficiencyMatrix
				
		for node in self.nodes.keys():
			if inNetwork.valveLocationMatrix.matrix[node] == inNetwork.networkMatrix.matrix[node]:
				newSegment = Segment("Seg "+ str(self.segmentNbr))
				newSegment.add_node(self.nodes[node], node)
				self.add_new_segment(newSegment)
				self.nodesExplored.append(node)

		for columnNbr in self.pipes.keys():
			pipesToAdd = []
			nodesToAdd = []
			if columnNbr not in self.pipesExplored:		   
				self.explore_pipe(columnNbr, pipesToAdd, nodesToAdd)
				newSegment = Segment("Seg "+ str(self.segmentNbr))
				for node in nodesToAdd:
					newSegment.add_node(self.nodes[node], node)
				for pipe in pipesToAdd:
					newSegment.add_pipe(self.pipes[pipe], pipe)
				self.add_new_segment(newSegment)

		for segment in self.segmentMap.values():
			valvesOfSegment = segment.names_of_valves()
			for name in valvesOfSegment:
				needNew = True
				for valve in self.valveMap.values():
					if name == valve.id:
						segment.add_valve(valve)
						valve.endingSegment = segment
						needNew = False
						
				if needNew:
					newValve = Valve(name, segment)
					self.add_new_valve(newValve)
					
		self.segValveMatrix = SegmentValveMatrix(self)
			
	def explore_pipe(self, pipe, inPipesToAdd, inNodesToAdd):
		if pipe not in self.pipesExplored:
			inPipesToAdd.append(pipe)
			self.pipesExplored.append(pipe)
			for row in range(len(self.defMatrix.matrix)):
				if self.defMatrix.get_value(row, pipe) == 1:
					self.explore_node(row, inPipesToAdd, inNodesToAdd)
		
	def explore_node(self, node, inPipesToAdd, inNodesToAdd):
		if node not in self.nodesExplored:
			inNodesToAdd.append(node)
			self.nodesExplored.append(node)
			for column in range(len(self.defMatrix.matrix[node])):
				if self.defMatrix.get_value(node, column) == 1:
					self.explore_pipe(column, inPipesToAdd, inNodesToAdd)
			
	def add_new_segment(self, inSegment):
		self.segmentMap[self.segmentNbr] = inSegment
		self.segmentNbr+=1

	def add_new_valve(self, inValve):
		self.valveMap[self.valveNbr] = inValve
		self.valveNbr+=1
		
	def str_segments(self):
		string = ""
		for seg in self.segmentMap.values():
			string += seg.id + ", "
			string += seg.str_elements()
			string += "\n"
		return string
			
	def str_valves(self):
		string = ""
		for valve in self.valveMap.values():
			string += str(valve) + "\n"
		return string
			
class Segment(Network):
	
	def __init__(self,inId, dotFilePath="none"):
		super(Segment, self).__init__(inId, dotFilePath="none")
		self.connectedValves = []
		
	def add_valve(self, inValve):
		self.connectedValves.append(inValve)
		
	def names_of_valves(self):
		valvesNames = []
		
		for pipe in self.pipeMap.values():
			if pipe.valveAtStart:
				name = str(pipe) + "-" + str(pipe.startingNode)
				if not name in valvesNames:
					valvesNames.append(name)
			if pipe.valveAtEnd:
				name = str(pipe) + "-"+ str(pipe.endingNode)
				if not name in valvesNames:
					valvesNames.append(name)
					
		for node in self.nodeMap.values():
			for pipe in node.connectedPipes:
				if pipe.valveAtStart and pipe.startingNode == node:
					name = str(pipe) + "-" + str(node)
					if not name in valvesNames:
						valvesNames.append(name)
				if pipe.valveAtEnd and pipe.endingNode == node:
					name = str(pipe) + "-"+ str(node)
					if not name in valvesNames:
						valvesNames.append(name)
		return valvesNames
		
class SegmentValveMatrix(object):
	
	def __init__(self, inSegmentValveGraph): 
		super(SegmentValveMatrix, self).__init__()
		
		self.rowNbr = inSegmentValveGraph.segmentNbr
		self.columnNbr = inSegmentValveGraph.valveNbr
		
		self.matrix = [ [ 0 for i in range(self.columnNbr) ] for j in range(self.rowNbr) ]
		
		for row in range(self.rowNbr):
			currSeg = inSegmentValveGraph.segmentMap[row]
			for column in range(self.columnNbr):
				currValve = inSegmentValveGraph.valveMap[column]
				if currValve in currSeg.connectedValves:
					self.matrix[row][column] = 1
	
	def __str__(self):
		string = ""
		for i in self.matrix:
			string = string + str(i) + "\n"
		return string
		
	def get_value(self, inRow, inColumn):
		return self.matrix[inRow][inColumn]
		