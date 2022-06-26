#Lo hice yo jotos, claudio : P
def imprimirmatriz(matriz):
    nomren = len(matriz)
    for x in range (nomren):
        print(matriz[x])
#Multiplicacion de matrices
#Regla principal: El numero de columnas de la matriz izquierda debe ser igual al de filas de la matriz derecha y viceversa.
A = []
B = []
C = []
filasA = int(input("Numero de filas de la matriz A: "))
colA = int(input("Numero de columnas de la matriz A: "))
for i in range(filasA):
    lista = []
    for j in range(colA):
        valor = float(input(f"introduce datos dentro de la celda [{i+1}][{j+1}]: "))
        lista.append(valor)
    A.append(lista)
filasB = int(input("Numero de filas de la matriz B: "))
colB = int(input("Numero de columnas de la matriz B: "))
for i in range(filasB):
    lista = []
    for j in range(colB):
        valor = float(input(f"introduce datos dentro de la celda [{i+1}][{j+1}]: "))
        lista.append(valor)
    B.append(lista)
if (colA == filasB):
    for i in range(filasA): #Numero de arreglos o filas de la nueva matriz
        arreglo = []
        for j in range(colB): #Numero de columnas de la nueva matriz
            sum = 0
            for k in range(filasB): 
                sum = sum + (A[i][k])*(B[k][j])
            arreglo.append(sum)
        C.append(arreglo)
    imprimirmatriz(C)