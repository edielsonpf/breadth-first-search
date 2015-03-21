function test = validNode(target, var)
    
    test=1;
    [row,col]=size(target);
    for i=1:row
        for j=1:col
            if(target(i,j)~= var(i,j))
               test=0; 
               break;
            end
        end
        if(test==0)
            break;
        end
    end
endfunction
