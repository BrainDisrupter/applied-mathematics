#Determinante de una matriz por eliminación con Gauss-Jordan (whiles y fors)
def imprimirmatriz(matriz):
    numren = len(matriz)
    numcol = len(matriz[0])
    for i in range (numren):
        for j in range(numcol):
            if (matriz[i][j] == -0.0):
                matriz[i][j] = 0.0
        print("[",matriz[i],"]")
A = [[1,2,3,4,5],
     [6,0,8,0,10],
     [11,-1,13,1,15],
     [0,17,18,19,20],
     [21,1,23,-1,25]]
recorrido = len(A)
recorrido-=1
for i in range(recorrido): #Procedimiento Gauss-Jordan (Eliminación)
    print("\nMATRIZ DE REFERENCIA")
    imprimirmatriz(A)
    l=i
    while (l <= recorrido):
        if (l != i):
            divisor = A[l][i]/A[i][i]*(-1)
            k=i
            while (k <= recorrido):
                A[l][k] = A[i][k]*divisor + A[l][k]
                k+=1
        l+=1
print("*******************")
imprimirmatriz(A)