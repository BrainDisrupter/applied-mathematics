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

def matrizinversa(A):
    recorrido = int(input("Número de renglones y columnas (Matriz cuadrada): "))
    for i in range(recorrido): #Llenado de matriz
        renglon = []
        for j in range(recorrido):
            while True:    
                try:
                    num = float(input(f"introduce el numero dentro de la celda [{i+1}][{j+1}]: "))
                    break
                except ValueError:
                    print("Introduciste un carácter inválido.\nVuelve a introducir el número.")
                    continue
            renglon.append(num)
        A.append(renglon)

    numrencol = len(A)

    for i in range (numrencol):
        for j in range(numrencol):
            if (i==j):
                valor = 1
            else:
                valor = 0
            A[i].append(valor)
    print("MATRIZ INICIAL")
    imprimirmatriz(A)
    for i in range(numrencol): #Procedimiento Gauss-Jordan (Eliminación)
        pivote = A[i][i]
        print(f"\nR{i+1}/{pivote}=R{i+1}")
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

        print("\nMATRIZ DE REFERENCIA")

        imprimirmatriz(A)
        Ainversa=[]

    for i in range(numrencol):
        renglon=[]
        for l in range(numrencol):
            renglon.append(A[i][l+numrencol])
        Ainversa.append(renglon)
    print("\n*************MATRIZ INVERSA*************")
    imprimirmatriz(Ainversa)

A=[]
matrizinversa(A)