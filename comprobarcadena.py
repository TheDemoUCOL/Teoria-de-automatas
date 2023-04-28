import numpy as np
import os
import random
from openDoc import open_aut, open_gram
from main import *

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def determinista(rules):
    for i in rules:
        for j in i:
            if j != 'NULL':
                j_str = str(j)
                dig=len(j_str)
                if dig > 1:
                    j_list=[int(d) for d in str(j)]
                    rules[rules.index(i)][rules[rules.index(i)].index(j)]=j_list
                    return False

def generarCadenas(vectorN, MatrizP):
    # Genera un numero aleatorio para el renglon
    rRandom = random.randint(0, len(MatrizP[0])-1)
    # Genera un numero aleatorio para el vector
    cadena=MatrizP[0][rRandom]
    ok=evaluar(cadena, vectorN)
    while ok == False:
        cadena=reemplazo(cadena, MatrizP, vectorN)
        ok=evaluar(cadena, vectorN)
    return cadena
    
def evaluar(cadena, vectorN):
    ok=0
    for i in range(0, len(cadena)):
        if cadena[i] in vectorN:
            ok=ok+1
    if ok == 0:
        return True
    else:
        return False
        
    
def reemplazo(cadena, MatrizP, vectorN):
    for i in range(len(cadena)):
        if cadena[i] in vectorN:
            for j in range(len(vectorN)):
                if cadena[i] == vectorN[j]:
                    ind=vectorN.index(cadena[i])
                    rRandom = random.randint(0, len(MatrizP[ind])-1)
                    cadena=cadena.replace(cadena[i], MatrizP[ind][rRandom])
    cadena = cadena.replace(' ', '')
    return cadena

def evaluate_string(str_evaluate,sigma,f,rules):
    str_valid = True
    list_pos_car, list_states1,list_states2,list_states = [], [], [], ["0"]

    for i in str_evaluate:
        if i in sigma:
            x = 0
            if 0 == len(list_states): 
                print("\nResultados -> ['NULL']")
                print("\nCadena no valida")
                input("Presione enter para continuar...")
                str_valid = False
                break
            else:
                while x < len(list_states): 
                    list_pos_car.append(sigma.index(i))
                    list_states1.append(rules[int(list_states[x])][list_pos_car[0]])

                    if list_states1[x] != "NULL": 
                        var_str = list_states1[x]

                        c = 0
                        while c < len(var_str):
                            list_states2.append(var_str[c])
                            c += 1
                    x += 1

                list_pos_car.clear()
                list_states1.clear()
                list_states.clear()

                c = 0
                while c < len(list_states2):
                    list_states.append(list_states2[c])
                    c += 1
                list_states = list(np.sort(list(set(list_states))))
                list_states2.clear()

        else:
            print(f"\nCadena no valida, el caracter '{i}' no pertenece a Sigma {sigma}") 
            str_valid = False
            input("Presione enter para continuar...")
            break
        
    if str_valid == True:
        if 0 == len(list_states):
            print(f"\nResultados -> ['NULL']")
            print("\nCadena no valida")
            input("Presione enter para continuar...")
        else: 
            print(f"\nResultados -> {list_states}")

            c = 0
            while c < len(list_states): 
                if list_states[c] in f:
                    print("\nCadena valida")
                    input("Presione enter para continuar...")
                    break  

                if c+1 == len(list_states): 
                    print("\nCadena no valida")
                    input("Presione enter para continuar...")
                    break

                c += 1
                
