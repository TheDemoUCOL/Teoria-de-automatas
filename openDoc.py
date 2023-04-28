def determinista(rules):    #Convierte las gramaticas dobles en separadas
    deterministic=True
    for i in rules:
        for j in i:
            if j != 'NULL':
                j_str = str(j)
                dig=len(j_str)
                if dig > 1:
                    j_list=[int(d) for d in str(j)]
                    rules[rules.index(i)][rules[rules.index(i)].index(j)]=j_list
                    deterministic=False
    return deterministic

def create_array(n,m): #Crea un arreglo de n x m
    array1 = []
    for i in range(n):
        a = [0]*m
        array1.append(a)

    return array1


def open_gram(fileName):
    try:
        txt = open(fileName, 'r')
        N = txt.readline() #Recupera el conjunto de no terminales
        T = txt.readline() #Recupera el conjunto de terminales
        P = txt.readline() #Recupera el conjunto de producciones
        RdeP = txt.readline() #Recupera el numero de producciones
        vectorN = txt.readline() #Recupera el numero de renglones de la matriz
        vectorN = vectorN.split('{', 1)[1]
        vectorN = vectorN.split('}', 1)[0]
        vectorN = vectorN.split(',') #Separa los renglones
        vectorT = txt.readline()
        vectorT = vectorT.split('{', 1)[1]
        vectorT = vectorT.split('}', 1)[0]
        vectorT = vectorT.split(',') #Separa los elementos del vector
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
        return N, T, P, RdeP, vectorN, vectorT, MatrizP
    except FileNotFoundError:
        print("Archivo no encontrado")
        input("Presione enter para continuar...")
    return 0,0,0,0,0,0,0
    
    
def open_aut(name_file): #Funcion para abrir el archivo y extraer los datos mejorada respecto a la anterior
    ok=False
    isDeterministic = True
    
    try:
        open(name_file, "r")
        ok = True
    except FileNotFoundError:
        print("Archivo no encontrado")
        input("Presione enter para continuar...")
        
        
    if ok == True:
        print("Archivo cargado correctamente")
        with open(name_file, "r") as file_automata:
            cs = int(file_automata.readline()) 
            ce = int(file_automata.readline()) 
            rules = create_array(cs,ce)
            c, c_p1, c_p2 = 0, 0, 0
            automata = (linea for i, linea in enumerate(file_automata) if i>=0)

            for linea in automata:
                if len(linea)>1:
                    if c_p1 == 0:
                        if "Sig{" in linea: 
                            i1 = linea.index('{')
                            i2 = linea.index('}')
                            sig = linea[i1+1:i2].split(",")
                            c_p1 += 1

                    if c_p2 == 0:
                        if "F{" in linea:
                            i1 = linea.index('{')
                            i2 = linea.index('}')
                            f = linea[i1+1:i2].split(',')
                            c_p2 += 1

                    if '>' in linea: 
                        i1 = linea.index('>')
                        if ',' in linea:
                            i2 = linea.index(',')
                        elif '}' in linea:
                            i2 = linea.index('}')
                        rules[c] = linea[i1+1:i2].split('|')
                        c+=1

            i = 0
            while i < len(rules):
                j = 0
                while j < len(rules[i]):  
                    c_space = str(rules[i][j]).count(" ")
                    rules[i][j] = str(rules[i][j]).replace(" ","",c_space)
                    j += 1
                i += 1
                
            isDeterministic=determinista(rules)
                        
        try:
            return sig,f,rules,isDeterministic
        
        except UnboundLocalError:
            print("Archivo no valido, sintaxis inapropiada")
            input("Presione enter para continuar...")
            return 0,0,0,0
    
    else:
        return 0,0,0,0
    
    