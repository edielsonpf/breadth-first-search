'''
Created on Jun 15, 2016

@author: Edielson
'''
from queue import Queue
        
class search(object):
    '''
    classdocs
    '''

    def __init__(self, graph):
        '''
        Constructor
        '''
        self.g = graph
    
    def breadth_first_search(self,start,target):
        frontier = Queue()
        frontier.put(start)
        visited = {}
        visited[start] = True
        solution = False
        path=[start]=None
        
        while not frontier.empty():
            current = frontier.get()
            if current == target:
                solution = True
                path.append(current)
                break
            else:    
                path.append(current)
                print("Visiting %r" % current)
                for next_item in self.g.neighbors(current):
                    if next_item not in visited:
                        frontier.put(next_item)
                        visited[next_item] = True
        
        return solution,path
    
    def breadth_first_search2(self,start,target):
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