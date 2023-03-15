from scipy.optimize import linprog
import numpy

# Solicitar entrada de usuario para el problema de programación lineal
num_variables = int(input("Ingrese el número de variables: "))
num_restricciones = int(input("Ingrese el número de restricciones: "))

# Definir coeficientes de la función objetivo
objetivo = []
for i in range(num_variables):
    coeficiente = int(input(f"Ingrese el coeficiente para la variable x{i+1}: "))
    objetivo.append(coeficiente)

# Definir coeficientes de las restricciones
restricciones = []
for i in range(num_restricciones):
    restriccion = []
    for j in range(num_variables):
        coeficiente = int(input(f"Ingrese el coeficiente para la variable x{j+1} en la restricción {i+1}: "))
        restriccion.append(coeficiente)
    valor = int(input(f"Ingrese el valor de la restricción {i+1}: "))
    restriccion.append(valor)
    restricciones.append(restriccion)
    
    obj=numpy.array(objetivo)
    res=numpy.array(restricciones)

# Resolver el problema utilizando el método simplex
resultado = linprog(c=-1*obj, A_ub=res[:, :-1], b_ub=res[:, -1])

# Imprimir resultados
print(f"Valor óptimo: {-1 * resultado.fun}")
print("Solución óptima:")
for i in range(num_variables):
    print(f"x{i+1}: {resultado.x[i]}")