# Importing NumPy Library
import numpy as np #Importamos libreria para usar vectores

def imprimirmatriz(matriz):
    nomren = len(matriz)
    for x in range (nomren):
        print(matriz[x])

inc = int(input("Introduce tu número de incógnitas: "))
matrix = np.zeros((inc,inc+1))
vectorsolucion = np.zeros(inc) #Hacemos un array con vector solución

for i in range(inc):
    for j in range(inc):
        float(input(f"Introduce el número de la celda [{i}][{j}]: ")) #Introducimos datos
#Desarrollo del método de eliminación por Gauss-Jordan
    for i in range(inc): #Desplazamos por renglones
        for j in range(inc): #Obtención del renglón pivote
            matrix[i][j] = (matrix[i][j]/matrix[i][i])
        for k in range(inc): #
            multiplo = (matrix[i+k][i]) #Obtención del múltiplo para eliminar las columnas
            for l in range(inc): 
                matrix[i+k][l] = (-1)*(multiplo)*(matrix[i][l])+(matrix[k+1][l])
print(matrix)
#matrix[k+1][j] = (matrix[i][j])*(matrix[k+1][j])*(-1)+

#Desarrollo (Aquí solo llegaremos a la solución final, no desplegaremos cada matriz u.u)

# np.zeros() nos permite hacer un arreglo definiendo sus renglones y columnas según un valor dado. 
# ubico un +1 ya que la matriz de gauss jordan siempre está aumentada, así que si nos dan 4 incógnitas por ejemplo, 
# tendrémos cuatro columnas de las variables y una de los términos independientes

# imprimirmatriz(matriz2)