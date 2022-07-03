#Inversa de una matriz
from decimal import DivisionByZero
def imprimirmatriz(matriz):
    numren = len(matriz)
    numcol = len(matriz[0])
    for i in range (numren):
        for j in range(numcol):
            if (matriz[i][j] == -0.0):
                matriz[i][j] = 0.0
        print("[",matriz[i],"]")
A = [[1,2,3],
     [4,5,6],  
     [7,8,2]]
numrencol = len(A)
for i in range (numrencol):
    for j in range(numrencol):
        if (i==j):
            valor = 1
        else:
            valor = 0
        A[i].append(valor)
for i in range(numrencol): #Procedimiento Gauss-Jordan (Eliminación)
    pivote = A[i][i]
    for j in range(numrencol*2):
        try:
            A[i][j] = A[i][j]/pivote #Dividimos renglon pivote entre su pivote
        except ZeroDivisionError or DivisionByZero:
            A[i][j] = 0
    print("\nMATRIZ DE REFERENCIA")
    imprimirmatriz(A)
    for l in range(numrencol):
        if (l != i):
            multiplo = A[l][i]
            print(f"R{l+1} - R{i+1} x {multiplo} => R{l+1}")
            for k in range(numrencol*2):
                A[l][k] = A[l][k]-(A[i][k]*multiplo)
imprimirmatriz(A)