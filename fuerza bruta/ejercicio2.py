def ejercicio2(array:list[int])->int:
    resultado1:list=[]
    resultado:int=0
    for i in range(len(array)-1):
        pos1=array[i]
        pos2=array[i+1]
        if (pos1>0 and pos2>0):
            suma=pos1+pos2
            resultado1.append(suma)
            for j in range(len(resultado1)-1):
                posj1=resultado1[j]
                posj2=resultado1[j+1]
                if posj1>posj2:
                    return posj1

#    return resultado
        

array=[1,2,-2,3,-4,10,5,-4,4,6]
print(ejercicio2(array))