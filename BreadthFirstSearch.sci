function BreadthFirstSearch()

    target=[1 2 3; 4 5 6; 7 8 0];
    
     // Cria um estado inicial aleatório (primeira solução)
    //newSolutions = [1 2 3; 4 5 0; 7 8 6];
    //newSolutions = [1 2 3; 4 0 5; 7 8 6];
    newSolutions = [1 0 3; 4 2 5; 7 8 6];
    //newSolutions = createInitialState();
    
    disp('Initial state');
    disp(newSolutions);
    disp('================================');
    // Inicializa um conjunto com todas as soluções
    allSolutions = [];
    
    solutionsToExpand = [];
    
    // Coloca essa solução no conjuto de soluções
    allSolutions = mycat(allSolutions, newSolutions);
    solutionFound=0;    
    // Enquanto existem soluções para serem exploradas...
    while (~isempty(newSolutions)&(solutionFound==0))
        [r,c,d] = size(newSolutions);
        for i=1:d
            if (validNode(target,newSolutions(:,:,i)) == 1)
                // Caso a solução seja encontrada, podemos parar o loop
                solutionFound=1;
                break;
            else
                //Cloca na lista de soluções para expandir
                solutionsToExpand = mycat(solutionsToExpand, newSolutions(:,:,i));
            end
        end
        if(solutionFound==0)
            // Expande as soluções
            [newSolutions, allSolutions] = expandSolution(solutionsToExpand, allSolutions);
            solutionsToExpand=[];
            disp('================================');
            disp('Expanding new solutions');
            disp(newSolutions);
        else
         // Imprime a melhor solução
            disp('Solution found');
            disp(newSolutions(:,:,i));
        end
        disp('Total of tested solutions');
        [r,c,d] = size(allSolutions);
        disp(d);
    end
endfunction
