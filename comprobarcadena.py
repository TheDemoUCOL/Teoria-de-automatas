import numpy as np
import os
import random
from openDoc import open_aut, open_gram

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

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
                
def auth(sigma, f, rules):
    print(f"\nSigma -> {sigma}")
    print(f"Estados Finales -> {f}")
    print(f"Reglas -> {rules}")
    print("\n-- Elija, por favor --")
    print("1- Elegir otro automata")
    print("2- Comprobar cadena")
    print("4- Salir")
    op = int(input("\nIngrese su selección: "))
    if op == 1:
        name_file = input("Ingresa el nombre del otro automata: ")
        clearConsole()
        sigma, f, rules = open_aut(name_file)
        
    elif op == 2:
        str_evaluate = input("Ingrese la cadena a evaluar: ")
        evaluate_string(str_evaluate,sigma,f,rules)
        clearConsole()
        main()
    elif op == 3:
        return 1
    
def gram(N, T, P, RdeP, vectorN, vectorT, MatrizP):
    print(f"""\nN -> {N}
    T -> {T}
    P -> {P}
    RdeP -> {RdeP}
    vectorN -> {vectorN}
    vectorT -> {vectorT}
    MatrizP -> {MatrizP}
    \n-- Elija, por favor --"
    1- Elegir otra gramática"
    2- Generar cadena"
    3- Salir""")
    op = int(input("\nIngrese su selección: "))
    if(op==1):
        name_file=input("Ingrese el nombre de la gramática: ")
        N, T, P, RdeP, vectorN, vectorT, MatrizP=open_gram(name_file)
    elif(op==2):
        cadena=generarCadenas(vectorN, MatrizP)
        clearConsole()
        print(f"Cadena generada: {cadena}")
        input("Presione enter para continuar...")
        clearConsole()
        main()
    elif(op==3):
        return 1
    

def main():
    
    aut_loaded = False

    c = 0
    N=0
    while c == 0:
        if aut_loaded == False:
            print("\n-- Carga de archivos --")
            print("1- Cargar automata")
            print("2- Cargar gramática")
            print("3- Salir")

            op=0
            try:
                op = int(input("\nIngrese su elección: "))
            except ValueError:
                print("Ingrese un numero valido")
                op = 0
                input("Presione enter para continuar...")
                clearConsole()
                
            if op == 1:
                name_file = input("Ingresa el nombre del automata: ")
                clearConsole()
                sigma, f, rules = open_aut(name_file)
                if sigma == 0:
                    aut_loaded = False
                    clearConsole()
                else:
                    aut_loaded = True
                    
            elif op == 2:
                name_file=input("Ingrese el nombre de la gramática")
                N, T, P, RdeP, vectorN, vectorT, MatrizP=open_gram(name_file)
                if N == 0:
                    aut_loaded = False
                    clearConsole()
                else:
                    aut_loaded = True

            elif op == 3:
                c = 1
                break
        
        elif aut_loaded == True:
            if op==1:
                c=auth(sigma, f, rules)

            elif op==2:
                c=gram(N, T, P, RdeP, vectorN, vectorT, MatrizP)
         
if __name__ == "__main__":
    main()