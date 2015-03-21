//Verifica se a solução a existe no espaço de soluções analisadas
function y = containsSolution(solution, nodes)
 
    //Inicialmente considera-se que a solução ainda não foi anaisada
    //y = false;
    y = 0;
    //length = size(nodes);
    Length = size(nodes);
    
    //Verifica no vetor de soluções se já existe uma solução igual
    //if numel(length) == 3
    if length(Length) == 3
        //for i = 1 : length(3)
        for i = 1 : Length(3)
            if nodes(:,:,i) == solution
                //y = true;
                y = 1;
                break;
            end
        end
    end
endfunction
