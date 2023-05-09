import comprobarcadena as ca
import openDoc as od
import os
import convert

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')



def auth(sigma, f, rules, isDeterministic):
    print(f"\nSigma -> {sigma}")
    print(f"Estados Finales -> {f}")
    print(f"Reglas -> {rules}")
    print("\n-- Elija, por favor --")
    print("1- Elegir otro automata")
    print("2- Comprobar cadena")
    if isDeterministic == False:
        print("3- Convertir a deterministico")
        print("4- Salir")
    else:
        print("3- Salir")
    op = int(input("\nIngrese su selección: "))
    if op == 1:
        name_file = input("Ingresa el nombre del otro automata: ")
        clearConsole()
        sig,f,rules,isDeterministic = od.open_aut(name_file)
        
    elif op == 2:
        str_evaluate = input("Ingrese la cadena a evaluar: ")
        ca.evaluate_string(str_evaluate,sigma,f,rules)
        clearConsole()
        main()
    elif op == 3:
        if isDeterministic == False:
            sigma, f, rules = convert.AFNDtoAFN(sigma, f, rules)
            clearConsole()
            auth(sigma, f, rules, isDeterministic=True)
        else:
            return 1
            
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
    op =int(input("\nIngrese su selección: "))
    if(op==1):
        name_file=input("Ingrese el nombre de la gramática: ")
        N, T, P, RdeP, vectorN, vectorT, MatrizP= od.open_gram(name_file)
    elif(op==2):
        cadena=ca.generarCadenas(vectorN, MatrizP)
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
                sigma, f, rules, isDeterministic = od.open_aut(name_file)
                if sigma == 0:
                    aut_loaded = False
                    clearConsole()
                else:
                    aut_loaded = True
                    
            elif op == 2:
                name_file=input("Ingrese el nombre de la gramática")
                N, T, P, RdeP, vectorN, vectorT, MatrizP=od.open_gram(name_file)
                if N == 0:
                    aut_loaded = False
                    clearConsole()
                    
                else:
                    aut_loaded = True

            elif op == 3:
                c = 1
                break
        
        elif aut_loaded == True:
            if op==1:#type: ignore
                c=auth(sigma, f, rules, isDeterministic) #type: ignore

            elif op==2:#type: ignore
                c=gram(N, T, P, RdeP, vectorN, vectorT, MatrizP) #type: ignore
                
if __name__ == "__main__":
    main()