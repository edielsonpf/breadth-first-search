from SearchAlgorithms.bfs import breadth_first_search
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
        'Congonhal': ['Pouso Alegre'],
        'Belo Horizonte':['Varginha']
    }
    
    #Creating an problem object based on FindPath class
    Problema = FindPath(example_graph)
    
    #Creating an object for breadth first search algorithm for ``FindPath`` problem
    SerachObject = breadth_first_search(Problema)    
    
    
    #Finding solution
    print('Searching Belo Horizonte starting from Pouso Alegre...')
    start = 'Pouso Alegre'
    target = 'Belo Horizonte'
    came_from,path,solution = SerachObject.search(start,target)
    print('Done!\n')
    if solution == True:
        print('Path found!')
        string=(start)
        for city in path:
            if city != start:
                string=(string+'->'+city)
        print(string)
    else:
        print('Path not found!')        
        
    print('\nSearching Itajuba starting from Belo Horizonte...')
    start = 'Belo Horizonte'
    target = 'Itajuba'
    came_from,path,solution = SerachObject.search('Belo Horizonte','Itajuba')
    print('Done!\n')
    if solution == True:
        print('Path found!')
        string=(start)
        for city in path:
            if city != start:
                string=(string+'->'+city)
        print(string)
    else:
        print('Path not found!')   
    
        
    