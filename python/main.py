from SearchAlgorithms.bfs import breadth_first_search
from graph import SimpleGraph


if __name__ == '__main__':
    
    example_graph = SimpleGraph()
    example_graph.edges = {
        'Pouso Alegre': ['Santa Rita','Varginha','Congonhal','Cachoeira de Minas'],
        'Santa Rita': ['Pouso Alegre', 'Itajuba', 'Cachoeira de Minas'],
        'Itajuba': ['Santa Rita'],
        'Varginha': ['Belo Horizonte', 'Pouso Alegre'],
        'Cachoeira de Minas': ['Santa Rita','Pouso Alegre'],
        'Congonhal': ['Pouso Alegre'],
        'Belo Horizonte':['Varginha']
    }
    
    SerachObject = breadth_first_search(example_graph)    
    came_from,path,solution = SerachObject.search('Pouso Alegre','Belo Horizonte')
    print(came_from)
    if solution == True:
        print(path)
        
    print('Searching Itajuba starting from Belo Horizonte')
    came_from,path,solution = SerachObject.search('Belo Horizonte','Itajuba')
    print(came_from)
    if solution == True:
        print(path)
    
        
    