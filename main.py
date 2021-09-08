#! usr/bin/python
# -*- coding: utf-8 -*-
import mip

### Import of files needed for the project
import parser_project as parser  # file containing the function to parse the data files and create a Data object
import problem as pb # file containing the data structures to store the data of the problem and a solution to a problem (class Data, BalanceTriple, Solution)
import checker # file containing the functions to check if a given Solution object is feasible according to a Data object and if its cost is correclty computed
import solver


def mainFunction(instanceFilename: str, assignmentFilename: str, verbose: bool, maxTime: int):
    print("Received instance files ", instanceFilename, " and ", assignmentFilename)

    # reading the data
    data = parser.parseFiles(instanceFilename, assignmentFilename)

    if verbose:
        problem.printData(data)

    # solve the problem
    solution = solver.solve(data, maxTime, verbose)

    if verbose:  # print the solution
        print("Solution of cost ", solution.cost)
        for i in range(data.nbProcess):
            print(solution.assignment[i], end=" ")  # here the solution is written with our convention 1..n
        print()

    # test if the solution is feasible and compute its cost
    checker.check(data, solution, True)  # check if the solution is feasible


# enter your instance name here 
instanceFilename = "data/dataA/model_a1_1.txt"
assignmentFilename = "data/dataA/assignment_a1_1.txt"

# set to true if you want to print intermediate logs
verbose = False

# default time allowed
maxTime = 300 
        
# reads the data, calls the method solve you have implemented, retrieves the solution, and checks that the constraints are respected and the cost correctly computed
mainFunction(instanceFilename, assignmentFilename, verbose, maxTime)