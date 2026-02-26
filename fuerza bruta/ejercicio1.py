def suma(array:int,x)->int:  
    resultado:list=[]
    #n=len(array)
    for i in range(len(array)-1):
        for j in array:
            pos1=array[i]
            pos2=array[i+1]
            pos3=array[j-1]
            
            suma=pos1+pos2+pos3
            if (suma==x):
                resultado.append((pos1,pos2,pos3))
                return resultado


array=[1,2,3,4,5,6,7,8,9]
x=25
print(suma(array,x))