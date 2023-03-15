# Escribir codigo en python que vacie el contenido
# de un archivo texto con un formato especifico, a 2 vectores
# y una matriz


# Definir funcion para cargar gramaticas
def cargar_gramaticas():
    
    archivo = open('gramaticas.txt','r')
    contenido = archivo.read()
    archivo.close()
    
    contenido = contenido.splitlines()
    no_terminales = []
    terminales = []
    producciones = []
    
    for linea in contenido:
        linea = linea.split()
        no_terminales.append(linea[0])
        terminales.append(linea[1])
        producciones.append(linea[2:])
    return no_terminales, terminales, producciones