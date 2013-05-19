# -*-coding:Utf-8 -*

from hydraulic_network.globalnetwork import GlobalNetwork
from optimization import  *

import time

def print_in_file(num, qual):
	f = open('/home/dollars/Desktop/plouf.txt', 'a')
#	total = 0.00
#	for i in qual:
#		total += i
	f.write('{0} {1}\n'.format(num, qual))

if __name__=="__main__": #petit exemple
	print("Test de Network")
	
	myNetwork = GlobalNetwork("myNetwork", "../input/ferraraNetwork.dot")
	
	print(myNetwork.segNetwork.str_segments())
	
	pattern = [(0,1) for i in range(myNetwork.network.nbrPipes*2)]
	
	t0 = time.time()
	test = GeneticAlgorithm(pattern, [myNetwork.average_valves_per_segment, myNetwork.average_segment_size, myNetwork.standard_deviation_segment_size, myNetwork.nbr_valves, myNetwork.average_unintended_isolation], print_in_file)
	print(time.time()-t0)
	
	print(test.solution)
	myNetwork.update(test.solution)
	print(myNetwork.average_unintended_isolation())
	print(myNetwork.average_segment_size())
	print(myNetwork.standard_deviation_segment_size())
	print(myNetwork.average_valves_per_segment())
	print(myNetwork.nbr_valves())
	
	print(myNetwork.segNetwork.str_valves())
	print(myNetwork.segNetwork.str_segments())
	
	t0 = time.time()
	test = GeneticAlgorithmVariation(pattern, [myNetwork.average_valves_per_segment, myNetwork.average_segment_size, myNetwork.standard_deviation_segment_size, myNetwork.nbr_valves, myNetwork.average_unintended_isolation], print_in_file)
	print(time.time()-t0)
	
	print(test.solution)
	myNetwork.update(test.solution)
	print(myNetwork.average_unintended_isolation())
	print(myNetwork.average_segment_size())
	print(myNetwork.standard_deviation_segment_size())
	print(myNetwork.average_valves_per_segment())
	print(myNetwork.nbr_valves())

	print(myNetwork.segNetwork.str_valves())
	print(myNetwork.segNetwork.str_segments())

	t0 = time.time()
	test = SimulatedAnnealing(pattern, [myNetwork.average_valves_per_segment, myNetwork.average_segment_size, myNetwork.standard_deviation_segment_size, myNetwork.nbr_valves, myNetwork.average_unintended_isolation], print_in_file)
	print(time.time()-t0)
	
	print(test.solution)
	myNetwork.update(test.solution)
	print(myNetwork.average_unintended_isolation())
	print(myNetwork.average_segment_size())
	print(myNetwork.standard_deviation_segment_size())
	print(myNetwork.average_valves_per_segment())
	print(myNetwork.nbr_valves())

	print(myNetwork.segNetwork.str_valves())
	print(myNetwork.segNetwork.str_segments())