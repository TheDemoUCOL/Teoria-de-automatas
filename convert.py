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

def fill(autconvert, rules):
    #print(rules)
    for keys in autconvert.keys():
            #print("key",keys)
            if keys != '0':
                aux = [[],[]]
                for y in keys:
                    if y.isdigit():
                        #print("y",y)                       #permite obtener los estados de las llaves desde 
                        #print("rules",rules[int(y)])
                        for z in rules[int(y)]:             #la tabla de transiciones
                            if z != 'NULL':
                                #print("z",z)
                                for w in z:
                                    aux[rules[int(y)].index(z)].append(w)
                                    #print("agregado",[rules[int(y)]])

                #print("aux",aux)
                for state in aux:
                    #print("state",state)
                    for state2 in state:
                        state[state.index(state2)] = int(state2) #convierte los elementos de las listas en enteros no repetidos
                    aux[aux.index(state)] = list(set(state))
                #print("aux",aux)
                autconvert[keys] = aux
                #print(set(aux1))
    return autconvert


if __name__ == "__main__":
    sigma = []
    f = ['2', '4']
    rules = [[[0, 3], [0, 1]], ['NULL', '2'], ['2', '2'], ['4', 'NULL'], ['4', '4']]
    print(AFNDtoAFN(sigma, f, rules))