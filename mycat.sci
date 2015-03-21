function destMatrix = mycat(destMatrix,srcMatrix)
    [l,c,dim]=size(destMatrix);
    if((c~=0)&(l~=0))
        destMatrix(:,:,dim+1)=srcMatrix;
    else
        destMatrix(:,:,dim)=srcMatrix;
    end
endfunction
