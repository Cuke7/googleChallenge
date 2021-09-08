#! usr/bin/python
# -*- coding: utf-8 -*-
from mip import *

import problem as pb # file containing the data structures to store the data of the problem and a solution to a problem (class Data, BalanceTriple, Solution)

def solve(data: pb.Data, maxTime: int, verbose: bool) -> pb.Solution:
    #To fill

    # Our model
    model = Model(name = "Exemple", sense = mip.MINIMIZE, solver_name="CBC")

    # Variable to optimize Z(p,m), indicate if process p is on machine m
    z = [[model.add_var(name="z(" + str(p) + "," + str(m) + ")", var_type=BINARY) for m in range(data.nbMachines)] for p in range(data.nbProcess)]            


    # Usage per machine U(m,r) <= C(m,r)
    for m in range(data.nbMachines):
        for r in range(data.nbResources):
            model += (xsum(z[p][m] * data.processReq[p, r]  for p in range(data.nbProcess)) <=
                          data.hardResCapacities[m, r])

    # Y(s,p) shows the repartions of process p across services s
    Y = []
    for s in range(data.nbServices):
        Y.append([])
        for p in range(data.nbProcess):
            # Si le process p appartient au service s
            if(data.servicesProcess[p] == s):
                Y[s].append(1)
            else:
                Y[s].append(0)

    # For each machine and each service, we check if the process on the machine belong to different services
    for m in range(data.nbMachines):
        for s in range(data.nbServices):
            model += (xsum(Y[s][p] * z[p][m] for p in range(data.nbProcess)) <= 1)


    


    return pb.Solution(data.initialAssignment,0)