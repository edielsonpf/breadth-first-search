'''
Created on Jun 15, 2016

@author: Edielson
'''
from queue import Queue
        
class breadth_first_search(object):
    '''
    classdocs
    '''

    def __init__(self, graph):
        '''
        Constructor
        '''
        self.g = graph
    
    def search(self,start,target):
        frontier = Queue()
        frontier.put(start)
        path = []
        come_from={}
        come_from[start]=None
        solution = False
        
        while not frontier.empty():
            current = frontier.get()
            path.append(current)
            
            if current == target:
                solution = True
                break
            
            print("Visiting %r" % current)
            for next_item in self.g.neighbors(current):
                if next_item not in come_from:
                    frontier.put(next_item)
                    come_from[next_item] = current
                    
        return come_from,path,solution        