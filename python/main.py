from graph import SimpleGraph
from bfs import search
import path

cidades=['Pouso Alegre', 'Santa Rita', 'Pocos de Caldas', 'Varginha', 'Belo Horizonte']

for cidade in cidades:
    print(cidade)

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
    
    SerachObject = search(example_graph)    
    came_from,path,solution = SerachObject.breadth_first_search2('Pouso Alegre','Belo Horizonte')
    print(came_from)
    if solution == True:
        print(path)
        
    print('Searching Itajuba starting from Belo Horizonte')
    came_from,path,solution = SerachObject.breadth_first_search2('Belo Horizonte','Itajuba')
    print(came_from)
    if solution == True:
        print(path)
    
        
    