function y = getValidPositions(row, col)
    y = [];
    
    //Se é possível mover para cima
    if row - 1 >= 1
        // Cria um estado válido
        y = cat(1, y, [row - 1 col]);
    end
    
    //Se é possível mover para baixo
    if row + 1 <= 3
        y = cat(1, y, [row + 1 col]);
    end
    
    //Se é possível mover para a esquerda
    if col - 1 >= 1
        y = cat(1, y, [row col - 1]);
    end
    
    //Se é possível mover para a direita
    if col + 1 <= 3
        y = cat(1, y, [row col + 1]);
    end
endfunction
