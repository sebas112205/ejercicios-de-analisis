def Trabajos(trabajos:list,trabajos_final:list=[]):
    
    while len(trabajos)>0:
        
        for i in range(len(trabajos)-1):
            if trabajos[i]["deadline"]>trabajos[i+1]["deadline"] :
                trabajos_final.append(trabajos[i]["profit"])
            suma=sum(trabajos_final)
                
        return trabajos_final,suma
trabajos = [
    {"id": "J1", "deadline": 2, "profit": 100},
    {"id": "J2", "deadline": 1, "profit": 19},
    {"id": "J3", "deadline": 2, "profit": 27},
    {"id": "J4", "deadline": 1, "profit": 25},
    {"id": "J5", "deadline": 2, "profit": 15},
]

print(Trabajos(trabajos))



