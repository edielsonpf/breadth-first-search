function [nodes, newSolutions] = createSolution(solution, nodes, newSolutions, newRow, newCol, zeroRow, zeroCol)
    // Copia a solução
    new = solution;
    
    // Faz o deslocamento
    value = new(newRow, newCol);
    new(newRow, newCol) = new(zeroRow, zeroCol);
    new(zeroRow, zeroCol) = value;
 
    // Se a solução não existe ainda adiciona ela no vetor de nós e nas
    // novas soluções
    //if ~containsSolution(new, nodes)
    if (containsSolution(new, nodes)==0)
        //nodes = cat(3, nodes, new);
        nodes = mycat(nodes, new);
        //newSolutions = cat(3, newSolutions, new);
        newSolutions = mycat(newSolutions, new);
    end
endfunction
