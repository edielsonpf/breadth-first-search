'''
Created on Jun 15, 2016

@author: Edielson
'''
from queue import Queue
        
class breadth_first_search(object):
    '''
    This class implements the breadth first search algorithm
    '''

    def __init__(self, problem):
        '''
        Constructor
        Any object instance must receive an ``problem`` parameter that is responsible
        for controlling the problem evaluation and next possible solutions. This parameter
        have two required functions:
            
            ExpandSolution(current): function that returns all possible solutions from 
            ``current`` state
            TestObjective(current,target): function that evaluates if ``current`` state
            corresponds to the ``target`` state 
         
        '''
        self.problem = problem
        
    def search(self,start,target):
        #start a empty queue
        frontier = Queue()
        #insert ``start`` state in the queue
        frontier.put(start)
        
        #initialize control variables
        path = []
        come_from={}
        come_from[start]=None
        solution = False
        
        #repeat while there are not visited candidate solutions
        while not frontier.empty():
            #take the first candidate solution
            current = frontier.get()
            #add to the visited states
            path.append(current)
            
            #evaluate is this is the objective
            if self.problem.ObjectiveTest(current,target) == True:
                #if true, finish serach
                solution = True
                break
            
            #else
            print("Visiting %r" % current)
            #expand new candidate solutions from current 
            new_solutions = self.problem.ExpandSolution(current)
            #run over all expanded solutions 
            for next_item in new_solutions:
                #check if each expanded solution was already visited
                if next_item not in come_from:
                    #if not, add to the queue for evaluation
                    frontier.put(next_item)
                    come_from[next_item] = current
                    
        return come_from,path,solution            