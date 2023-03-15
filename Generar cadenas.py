import random
import os

def generarCadenas(RenglonesP, MatrizP):
    # Genera un numero aleatorio para el renglon
    rRandom = random.randint(0, len(MatrizP[0])-1)
    # Genera un numero aleatorio para el vector
    cadena=MatrizP[0][rRandom]
    ok=evaluar(cadena)
    while ok == False:
        cadena=reemplazo(cadena, MatrizP, RenglonesP)
        ok=evaluar(cadena)
    return cadena
    
def evaluar(cadena):
    ok=0
    for i in range(0, len(cadena)):
        if cadena[i] in RenglonesP:
            ok=ok+1
    if ok == 0:
        return True
    else:
        return False
        
    
def reemplazo(cadena, MatrizP, RenglonesP):
    for i in range(len(cadena)):
        if cadena[i] in RenglonesP:
            for j in range(len(RenglonesP)):
                if cadena[i] == RenglonesP[j]:
                    ind=RenglonesP.index(cadena[i])
                    rRandom = random.randint(0, len(MatrizP[ind])-1)
                    cadena=cadena.replace(cadena[i], MatrizP[ind][rRandom])
    cadena = cadena.replace(' ', '')
    return cadena
    
    
def recuperarDatos(fileName):
    txt = open(fileName, 'r')
    N = txt.readline() #Recupera el conjunto de no terminales
    T = txt.readline() #Recupera el conjunto de terminales
    P = txt.readline() #Recupera el conjunto de producciones
    RenglonesP = txt.readline() #Recupera el numero de renglones de la matriz
    RenglonesP = RenglonesP.split('{', 1)[1]
    RenglonesP = RenglonesP.split('}', 1)[0]
    RenglonesP = RenglonesP.split(',') #Separa los renglones
    VectorP = txt.readline()
    VectorP = VectorP.split('{', 1)[1]
    VectorP = VectorP.split('}', 1)[0]
    VectorP = VectorP.split(',') #Separa los elementos del vector
    Matriz = txt.readlines()
    MatrizClear=[] #Matriz auxiliar para limpiar los datos
    MatrizP = [] #Matriz de producciones
    for i in range(len(Matriz)):
        if i == len(Matriz)-1:
            Matriz[i]=Matriz[i].split('}', 1)[0]
        if i == 0:
            Matriz[i] = Matriz[i].split('{', 1)[1]
        if Matriz[i] == '\n':                           #Elimina los saltos de linea y todo el cochinero
            Matriz[i].replace('\n', '')
        Matriz[i] = Matriz[i].split('>', 1)
        if(len(Matriz[i])==2):
            MatrizClear.append(Matriz[i][1])
    for i in range(len(MatrizClear)):
        MatrizClear[i] = MatrizClear[i].split(',')[0]
        MatrizP.append(MatrizClear[i].split('|'))
    
    print(MatrizP)
    txt.close()
    return N, T, P, RenglonesP, VectorP, MatrizP
    


if __name__ == '__main__':
    RenglonesP = None
    while True:
        print("Generador de cadenas")
        print("Que desea hacer?")
        print("1. Abrir un archivo nuevo")
        print("2. Generar una cadena")
        print("3. Salir")
        ans=input()
        if ans == '1':
            fileName = input("Ingrese el nombre del archivo: ")
            try:
                txt = open(fileName, 'r')
                txt.close()
                ok=True
            except FileNotFoundError:
                print("Archivo no encontrado, asegúrese de que el archivo se encuentre en la misma carpeta que el programa")
                input("Presione enter para continuar")
                ok=False
            if ok == True:
                N, T, P, RenglonesP, VectorP, MatrizP = recuperarDatos(fileName)
                print("Archivo abierto correctamente")
                input("Presione enter para continuar")
        
        if ans == '2':
            if RenglonesP == None:
                print("No se ha abierto ningun archivo")
                input("Presione enter para continuar")
            else:
                print("Cadena generada:")
                print(generarCadenas(RenglonesP, MatrizP))
                input("Presione enter para continuar")

        if ans == '3':  
            exit()
        if ans != '1' and ans != '2' and ans != '3':
            print("Opcion no valida")
            input("Presione enter para continuar")
        os.system("clear")