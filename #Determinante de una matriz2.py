#Determinante de una matriz por eliminación con Gauss-Jordan (fors) (código final)
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
    for i in range(recorrido): #Procedimiento Gauss-Jordan (Eliminación)
        print("\nMATRIZ DE REFERENCIA")
        imprimirmatriz(A)
        for l in range(i,recorrido):
            if (l != i):
                divisor = A[l][i]/A[i][i]*(-1)
                for k in range(i,recorrido):
                    A[l][k] = A[i][k]*divisor + A[l][k]
    sumdet = 1
    for i in range(recorrido):
        sumdet = sumdet*A[i][i]
    if (sumdet == -0.0):
       sumdet = 0.0
    print(f"La determinante es: {sumdet}")
    opc = int(input("\n¿Deseas calcular la determinante de otra matriz? \n1. Sí 2. No"))
print("*******************")
imprimirmatriz(A)