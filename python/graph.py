'''
Created on Jun 15, 2016

@author: Edielson
'''

class SimpleGraph:
    
    def __init__(self):
        self.edges = {}
    
    def neighbors(self, index):
        return self.edges[index]