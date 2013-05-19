# -*-coding:Utf-8 -*

from hydraulic_network.globalnetwork import GlobalNetwork
from optimization import  *

import time

def evol_qual(num, best):
    f = open('/home/dollars/Desktop/gen_var-best.txt', 'a')
    f.write('{0} {1}\n'.format(num, best))
    f.close()


def avg_result():
    f = open('/home/dollars/Desktop/gen_var-avg_qual.txt', 'a')
    avgQual = GeneticAlgorithmVariation(pattern, [myNetwork.average_valves_per_segment, myNetwork.average_segment_size, myNetwork.standard_deviation_segment_size, myNetwork.nbr_valves, myNetwork.average_unintended_isolation])
    f.write('{0}\n'.format(avgQual.assess_fitness(avgQual.bestSolution)))
    f.close()

if __name__=="__main__":
    print("Collecting information.")
    myNetwork = GlobalNetwork("ferraraNetwork", "../input/ferraraNetwork.dot")
    pattern = [(0,1) for i in range(myNetwork.network.nbrPipes*2)]
    
    t0 = time.time()
    evolQual = GeneticAlgorithmVariation(pattern, [myNetwork.average_valves_per_segment, myNetwork.average_segment_size, myNetwork.standard_deviation_segment_size, myNetwork.nbr_valves, myNetwork.average_unintended_isolation], evol_qual)
    print(time.time()-t0)
    
    for i in range(50):
        avg_result()

        
        
    