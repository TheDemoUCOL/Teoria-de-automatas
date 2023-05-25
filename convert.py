import os
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def AFNDtoAFN (sigma, f, rules):
    clearConsole()
    autconvert = {'0':rules[0]}
    for x in autconvert['0']:
        for y in x:
            if y != 'NULL':
                if y not in autconvert.keys():
                    autconvert["".join(str(x))] = []
    it = True            
    while it:
        fill(autconvert, rules)
        it, autconvert=fill_keys(autconvert, rules)
    aux = []
    for i in autconvert.keys():
        for j in i:
            if j.isdigit():
                if j in f:
                    aux.append(i)
    f=aux   

    return sigma, f, autconvert

def fill_keys(autconvert, rules):
    aux={}
    
    for values in autconvert.values():
        for value in values:
            if value != 'NULL':
                if str(value) not in list(autconvert.keys()):
                    aux.update({str(value):[[],[]]})
    if aux == {}:
        it = False
    else:           #indica si se hizo o no iteración
        it = True
    
    autconvert.update(aux)
    return it, autconvert

def flatten_list(lst): #descomprime listas anidadas
    flattened_list = []
    for item in lst:
        if isinstance(item, list):  # Verifica si el elemento es una lista anidada
            flattened_list.extend(flatten_list(item))  # Llama recursivamente a la función para aplanar la lista anidada
        else:
            flattened_list.append(int(item))  # Convierte el valor a entero y lo agrega a la lista aplanada
    return list(set(flattened_list)) #elimina duplicados

def fill(autconvert, rules):
    for key in autconvert.keys():
        if key != '0':
            aux = [[],[]]
            for value in key:
                if value.isdigit():
                    for i in range(len(rules[int(value)])):
                        if rules[int(value)][i] != 'NULL':
                            aux[i].append(rules[int(value)][i])
                            
            for i in range(len(aux)):
                aux[i] = flatten_list(aux[i])                    
            autconvert[key] = aux
            #print(autconvert, "\n")
            #input()
    return autconvert


"""if __name__ == "__main__":
    sigma = []
    f = ['2', '4']
    rules = [[[0, 3], [0, 1]], ['NULL', '2'], ['2', '2'], ['4', 'NULL'], ['4', '4']]
    AFNDtoAFN(sigma, f, rules)"""