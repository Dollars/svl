from hydraulic_network import Network
from hydraulic_network import SegmentValveGraph
from math import sqrt

class GlobalNetwork(object):
    
    def __init__(self, inId, dotFilePath="none"):
        super(GlobalNetwork, self).__init__()
        
        self.network = Network(inId, dotFilePath)
        
        self.segNetwork = SegmentValveGraph(self.network)
        
    def average_segment_size(self, valvesCode = 0):
        self.update(valvesCode)
        total = self.network.nbrNodes + self.network.nbrPipes
        return float(total)/(self.segNetwork.segmentNbr)
    
    def standard_deviation_segment_size(self, valvesCode = 0):
        self.update(valvesCode)
        average = self.average_segment_size()
        stdDev = 0
        for seg in self.segNetwork.segmentMap.values():
            curSize = float(seg.nbrNodes) + float(seg.nbrPipes)
            stdDev += (curSize-average)*(curSize-average)
        stdDev = sqrt(stdDev/self.segNetwork.segmentNbr)
        return stdDev
    
    def nbr_valves(self, valvesCode = 0):
        self.update(valvesCode)
        return self.network.get_valve_count()
    
    def average_valves_per_segment(self, valvesCode = 0):   
        self.update(valvesCode)
        total = 0
        for seg in self.segNetwork.segmentMap.values():
            total += len(seg.connectedValves)
        total = float(total)/ self.segNetwork.segmentNbr
        return total
    
    def average_unintended_isolation(self, valvesCode = 0):
        self.update(valvesCode)
        total = 0
        nbrNodes = self.network.nbrNodes
        waterSourceNode = []
        waterSourceNode.append(0)
        
        adjacencyMatrix = [ [ 0 for i in range(nbrNodes) ] for j in range(nbrNodes) ]
        
        for i in range(nbrNodes):
            for j in range(nbrNodes):
                if self.network.nodeMap[i] in self.network.nodeMap[j].connected_nodes():
                    adjacencyMatrix[i][j] = 1
        
        for seg in self.segNetwork.segmentMap.values():
            adjMatWithSegDel = adjacencyMatrix[:][:]
            for key in seg.nodeMap.keys():
                for i in range(nbrNodes):
                    adjMatWithSegDel[key][i] = 0
                    adjMatWithSegDel[i][key] = 0
            seg.nodeMap
            suppliedNodes = []
            
            suppliedNbr = 1
            for node in waterSourceNode:
                suppliedNodes.append(node)
                for currNode in suppliedNodes:
                    for i in range(nbrNodes):
                        if (adjMatWithSegDel[currNode][i] == 1) and (i not in suppliedNodes):
                            suppliedNodes.append(i)
                            suppliedNbr += 1
            total += (nbrNodes - suppliedNbr)
            
        total = float(total)/self.segNetwork.segmentNbr
        return total

    def update(self, valvesCode):
        if type(valvesCode) == type([]):  
            self.network.set_valves(valvesCode)
            self.segNetwork = SegmentValveGraph(self.network)