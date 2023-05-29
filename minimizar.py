import os
import numpy as np
from tabulate import tabulate

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def mini(sigma, f, rules):
    aceptados = f #estados aceptados
    noAceptados = [x for x in rules.keys() if x not in aceptados] #estados no aceptados
    particiones = [aceptados, noAceptados] #particiones iniciales
    

    for partition in range(len(particiones)):
        aux = []
        #print("particion: ", particiones[partition])
        for value in range(len(particiones[partition])):
            #print("value: ", particiones[partition][value])
            for transition  in rules[particiones[partition][value]]:
                #print("transition: ", transition)
                if str(transition) not in particiones[partition]:
                    aux.append(particiones[partition][value])
        if aux != []:
            for i in aux:
                particiones[partition].remove(i)
                particiones.append(i)

    for i in particiones:
        if type(particiones[particiones.index(i)]) != list:
            aux = []
            for j in i:
                if j.isdigit():
                    aux.append(int(j))
                    
            particiones.append(aux)

    for i in particiones:
        if type(particiones[particiones.index(i)]) != list:
            particiones.remove(i)
    for i in particiones:
        if type(i) != list:
            particiones.remove(i)
                            
    grupos=[]
    
    for i in particiones:
        if type(i[0]) == int:
            j=str(i)
        else:
            j = i[0]
        grupos.append(j)
    
    
        
    gruposDic={}
    for i in grupos:
        gruposDic[i]=[]
    
    for i in grupos:
        for j in rules[i]:
            gruposDic[i].append(j)
            
    return gruposDic
    # for values in gruposDic.values():
    #     for item in values:
    #         for particion in particiones:
    #             if str(item) in particion:
    #                 print(values[values.index(item)])
                

def tablitas(rules, sigma):
    tabla=[]
    for key, value in rules.items():
        tabla.append([key, value[0], value[1]])
    return tabulate(tabla, headers=['Estado', '0', '1'], tablefmt='fancy_outline')
                
    
if __name__ == "__main__":
    sigma = ['0', '1']
    f = ['[0, 3, 4]', '[0, 2, 3]', '[0, 2, 3, 4]', '[0, 1, 2, 4]', '[0, 1, 4]', '[0, 1, 2]']
    rules = {'0': [[0, 3], [0, 1]], 
             '[0, 3]': [[0, 3, 4], [0, 1]], 
             '[0, 1]': [[0, 3], [0, 1, 2]], 
             '[0, 3, 4]': [[0, 3, 4], [0, 1, 4]], 
             '[0, 1, 2]': [[0, 2, 3], [0, 1, 2]], 
             '[0, 1, 4]': [[0, 3, 4], [0, 1, 2, 4]],
             '[0, 2, 3]': [[0, 2, 3, 4], [0, 1, 2]], 
             '[0, 1, 2, 4]': [[0, 2, 3, 4], [0, 1, 2, 4]], 
             '[0, 2, 3, 4]': [[0, 2, 3, 4], [0, 1, 2, 4]]}
    particiones = mini(sigma, f, rules)
    print(tablitas(particiones, sigma))