#Algoritmo principal de solución de sistemas de ecuaciones lineales por Gauss-Jordan por eliminación
def imprimirmatriz(matriz):
    nomren = len(matriz)
    for x in range (nomren):
        print(matriz[x])
vecsolu = [] #Vector solucion
A = [[1,2,3,4,5],
     [5,6,7,8,9],
     [9,10,11,12,13],
     [13,14,15,16,17]]
col = len(A[0])
fil = len(A)
for i in range(fil):
    vectemp = [] #vector temporal para checar procesos dentro del codigo
    pivote = A[i][i]
    for j in range(col):
        try:
            A[i][j] = A[i][j]/pivote #Dividimos renglon pivote entre su pivote
        except ZeroDivisionError:
            A[i][j] = 0
    print("VECTOR TEMPORAL")
    imprimirmatriz(A)
    for l in range(fil):
        if (l != i):
            multiplo = A[l][i]
            print(multiplo)
            for k in range(col):
                A[l][k] = A[l][k]+(A[i][k]*multiplo)*(-1)
    print("MATRIZ ACTUAL")
    imprimirmatriz(A)
    print("*****************")