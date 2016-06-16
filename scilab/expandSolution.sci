// Função que expande uma solução criando as soluções filhas possíveis
function [newSolutions, nodes] = expandSolution(solutions, nodes)
    
    // Inicializa o vetor com as soluções expandidas
    newSolutions = [];
    
    // Para cada solução...
    for i = 1 : size(solutions, 3)
        solution = solutions(:, :, i);
 
        // Encontra a posição do espaço vazio (valor 0)
        [row, col] = find(solution == 0);
        row = row(1);
        col = col(1);
 
        // Verifica quais soluções filhas devem ser criadas.
        // Se a linha é maior que 1 quer dizer que podemos deslocar o espaço
        // uma casa para cima
        if row > 1
            [nodes, newSolutions] = createSolution(solution, nodes, newSolutions, row - 1, col, row, col);
        end
 
        // Se a linha é menor que 3 quer dizer que podemos deslocar o espaço
        // uma casa para baixo
        if row < 3
            [nodes, newSolutions] = createSolution(solution, nodes, newSolutions, row + 1, col, row, col);
        end
 
        // Se a coluna é maior que 1 quer dizer que podemos deslocar o espaço
        // uma casa para esquerda
        if col > 1
            [nodes, newSolutions] = createSolution(solution, nodes, newSolutions, row, col - 1, row, col);
        end
 
        // Se a coluna é menor que 3 quer dizer que podemos deslocar o espaço
        // uma casa para direita
        if col < 3
            [nodes, newSolutions] = createSolution(solution, nodes, newSolutions, row, col + 1, row, col);
        end
     end
endfunction
