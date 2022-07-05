#Determinante de una matriz por eliminación con Gauss-Jordan (fors) (código final).
def imprimirmatriz(matriz):
    numren = len(matriz)
    numcol = len(matriz[0])
    for i in range (numren):
        for j in range(numcol):
            if (matriz[i][j] == -0.0):
                matriz[i][j] = 0.0
        print("[",matriz[i],"]")
recorrido = int(input("Número de renglones y columnas (Matriz cuadrada): "))
opc = 1
while opc==1:
    vecsolu = [] #Vector solucion
    A = []
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
    if (A[0][0] == 0): #Dado que hubiera un 0 en A1,1 en el primer renglon, lo intercambiamos por uno que tenga un valor diferente de 0 en su primera columna.
        i=1
        while i<recorrido:
            if (A[i][0]!=0):
                A[0],A[i] = A[i],A[0]
                break
            i+=1
        imprimirmatriz(A)
        print(f"************************************************\nINTERCAMBIAMOS RENGLON 1 POR RENGLON {i+1} DEBIDO AL CERO INICIAL")
        imprimirmatriz(A)
    for i in range(recorrido): #Procedimiento Gauss-Jordan (Eliminación)
        print("\nMATRIZ DE REFERENCIA")
        imprimirmatriz(A)
        for l in range(i,recorrido):
            if (l != i):
                multiplo = A[l][i]/A[i][i]*(-1)
                print(f"R{l+1} - R{i+1} x {multiplo} => R{l+1}")
                for k in range(i,recorrido):
                    A[l][k] = A[i][k]*multiplo + A[l][k]
    sumdet = 1
    for i in range(recorrido):
        sumdet = sumdet*A[i][i]
    if (sumdet == -0.0):
       sumdet = 0.0
    print(f"La determinante es: {sumdet}")
    opc = int(input("\n¿Deseas calcular la determinante de otra matriz? \n1. Sí 2. No: "))