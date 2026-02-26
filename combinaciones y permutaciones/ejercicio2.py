def permutaciones(array, r):
    resultado = []
    n = len(array)
    
    for i in range(n): # i será 0, 1, 2, 3
        pos1 = array[i]
        
        # CAMBIO AQUÍ: j ahora será 0, 1, 2, 3
        for j in range(n): 
            if i != j: # Evitamos usar la misma letra dos veces
                pos2 = array[j] # Ahora j es un entero, ¡ya no hay error!
                
                resultado.append((pos1, pos2))
    
    return resultado

array = ['a', 'b', 'c', 'd']
r = 2
print(permutaciones(array, r))