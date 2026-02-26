def permutaciones1(array,inicio,fin):
    if inicio==fin:
        print(array)
    else:
        for i in range(inicio, fin):
            array[inicio],array[i]=array[i],array[inicio]
            permutaciones1(array,inicio + 1,fin)
            array[inicio],array[i]=array[i],array[inicio]
    pass
array=['A', 'B', 'C']
fin=len(array)
print(permutaciones1(array,0,fin))