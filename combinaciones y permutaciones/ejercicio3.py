import string
def abecedarioynumeros(abecedario:list,numeros):
    guardados=set()
    resultado:list=[]
    n=len(abecedario)
    for i in range(len(abecedario)-1):
        ab1=abecedario[i]
        ab2=abecedario[i+1]
        suma_abecedario=ab1,ab2
        for j in range(len(numeros)-1):
            num1=numeros[j]
            num2=numeros[j+1]
            suma_numeros = num1,num2
            if (n > 0 and len(numeros) > 0):
                resultado.append((suma_abecedario,suma_numeros))
    return resultado

# string.ascii_lowercase es "abcdefghijklmnopqrstuvwxyz"
# list() lo pica letra por letra
abecedario = list(string.ascii_lowercase)
numeros=[0,1,2,3,4,5,6,7,8,9]
print(abecedarioynumeros(abecedario,numeros))
# Resultado: ['a', 'b', 'c', 'd', 'e', ..., 'z']