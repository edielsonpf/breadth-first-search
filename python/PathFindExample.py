from SearchAlgorithms.breadth_first_search import breadth_first_search
from graph import SimpleGraph

class FindPath(object): 
    '''
    classdocs
    '''

    def __init__(self, graph):
        '''
        Constructor
        '''
        self.problem = graph
        
    def ObjectiveTest(self,current,target): 
        """Return ``True`` if ``current`` state corresponds to the ``target`` state 
        """ 
        solution = False 
        if current == target:
            solution = True
        return  solution
 
    def ExpandSolution(self,current): 
        """Returns all possible states from ``current`` 
        """ 
        return  self.problem.neighbors(current)
    
    def EqualityTest(self,state_a,state_b): 
        """Returns all possible states from ``current`` 
        """ 
        return  (state_a==state_b)


if __name__ == '__main__':
    
    #Creating a simple graph object
    example_graph = SimpleGraph()
    
    #Adding possible edges for this graph
    example_graph.edges = {
        'Pouso Alegre': ['Santa Rita','Varginha','Congonhal','Cachoeira de Minas'],
        'Santa Rita': ['Pouso Alegre', 'Itajuba', 'Cachoeira de Minas'],
        'Itajuba': ['Santa Rita'],
        'Varginha': ['Belo Horizonte', 'Pouso Alegre'],
        'Cachoeira de Minas': ['Santa Rita','Pouso Alegre'],
        'Congonhal': ['Pouso Alegre', 'Ouro Fino'],
        'Belo Horizonte':['Varginha'],
        'Ouro Fino': ['Congonhal']
    }
    
    #Creating an problem object based on FindPath class
    Problema = FindPath(example_graph)
    
    #Creating an object for breadth first search algorithm for ``FindPath`` problem
    SearchObj = breadth_first_search(Problema)    
    
    
    start = 'Pouso Alegre'
    target = 'Belo Horizonte'
    print('\nSearching %s starting from %s...'%(start,target))
    solution,path = SearchObj.search(start,target)
    print('Done!\n')
    if solution:
        print('Path found!')
        string=(start)
        for city in path:
            if city != start:
                string=(string+' -> '+city)
        print(string)
    else:
        print('Path not found!')        
        
    start = 'Belo Horizonte'
    target = 'Itajuba'
    print('\nSearching %s starting from %s...'%(start,target))
    solution,path = SearchObj.search('Belo Horizonte','Itajuba')
    print('Done!\n')
    print('Done!\n')
    if solution:
        print('Path found!')
        string=(start)
        for city in path:
            if city != start:
                string=(string+' -> '+city)
        print(string)
    else:
        print('Path not found!')  
    
        
    start = 'Ouro Fino'
    target = 'Campinas'
    print('\nSearching %s starting from %s...'%(start,target))
    solution,path = SearchObj.search(start,target)
    print('Done!\n')
    if solution:
        print('Path found!')
        string=(start)
        for city in path:
            if city != start:
                string=(string+' -> '+city)
        print(string)
    else:
        print('Path not found!') 
    