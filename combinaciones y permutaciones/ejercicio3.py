import string
def abecedarioynumeros(abecedario:list,numeros):
    guardados:list=[]
    resultado:list=[]
    n=len(abecedario)
    for i in range(len(abecedario)-1):
        ab1=abecedario[i]
        ab2=abecedario[i+1]
        guardados.append((ab1,ab2))
        suma_abecedario=ab1,ab2
        for j in range(len(numeros)-1):
            num1=numeros[j]
            num2=numeros[j+1]
            suma_numeros = num1,num2
            if (n > 0 and len(numeros) > 0):
                resultado.append((suma_abecedario,suma_numeros))
            if ((ab1,ab2) is guardados):
                abecedario.remove((ab1,ab2))
                return abecedario
    return resultado

abecedario = list(string.ascii_lowercase)
numeros=[0,1,2,3,4,5,6,7,8,9]
print(abecedarioynumeros(abecedario,numeros))
