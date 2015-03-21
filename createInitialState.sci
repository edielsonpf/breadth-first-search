// Função que cria um estado inicial aleatório do quebra cabeça de 8 peças
//Autor: edielson@inatel.br
function y = createInitialState()
 
    SHUFFLE = 40;
    //SHUFFLE = 1;
 
    //Cria um quebra cabeça com o estado objetivo (resolvido)
    y = [0 1 2;
         3 4 5;
         6 7 8];
    
    //Embaralha as peças um número de vezes definido
    for i = 1 : SHUFFLE
        
        //Pega a posição do espaço em branco
        [row, col] = find(y == 0);
        row = row(1);
        col = col(1);
        
        //Pega as posições possíveis de deslocamento
        positions = getValidPositions(row, col);
        
        //Calcula uma posição válida aleatória para fazer a troca
        maximo = size(positions, 1);
        //pos = randi(maximo, 1); MATLAB
        pos = grand(1, 1, "uin", 1, maximo);
        pos = positions(pos, :);
        
        // ...e troca os valores de lugar
        value = y(pos(2), pos(1));
        y(pos(2), pos(1)) = y(row, col);
        y(row, col) = value;
    end
endfunction
