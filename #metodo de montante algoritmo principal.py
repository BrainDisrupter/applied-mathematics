#Metodo de montante para solución de S.E.L
def imprimirmatriz(A):
    numren = len(A)
    numcol = len(A[0])
    for i in range (numren):
        for j in range(numcol):
            if (A[i][j] == -0.0):
                A[i][j] = 0.0
        print("[",A[i],"]")

A=[[0,4,3,4,0],
   [23,2,4,1,-1],
   [3,1,4,1,3],
   [-1,2,4,5,2]]

numfil = len(A)
numcol = len(A[0])
i=0
if (A[0][0] == 0):
    while (i<=numfil):
        if (A[i][0] != 0):
            A[0],A[i] = A[i],A[0]
            break
        i+=1
print("\nMETODO DE MONTANTE PARA SOLUCIÓN DE SISTEMAS DE ECUACIONES LINEALES.\n")
print("************MATRIZ INICIAL************")
imprimirmatriz(A)
for i in range(numfil):#Recorrido pivotes
    pivote = 1 #pivote default
    if i!=0:
        pivote=A[i-1][i-1] #pivote anterior
    print(f"\nPivote: {pivote}\n")
    for j in range(numcol):#Recorrido columnas
        for k in range(numfil):#Recorrido filas
            if (j!=i and k!=i):
                try:
                    print(f"A[{k+1}][{j+1}] = {A[i][i]} x {A[k][j]} - {A[k][i]} x {A[i][k]} = ",(A[i][i]*A[k][j]-A[k][i]*A[i][k])/pivote)
                    A[k][j] = (A[i][i]*A[k][j]-A[k][i]*A[i][j])/pivote
                except ZeroDivisionError:
                    A[k][j] = 0
    for m in range(numfil):#Recorrido filas para ubicar 0s
        if (m!=i):
            A[m][i] = 0
    if (i < numfil-1):
        print("\n************MATRIZ NUEVA************")
    elif (i == numfil-1):
        print("\n************MATRIZ FINAL************")
    imprimirmatriz(A)    