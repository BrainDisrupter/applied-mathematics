#Lo hice yo, claudio : P
def imprimirmatriz(matriz):
    nomren = len(matriz)
    for x in range (nomren):
        print(matriz[x])
#Multiplicacion de matrices
    #Regla principal: El numero de columnas de la matriz izquierda debe ser igual al de filas de la matriz derecha y viceversa.
opc = 1
while (opc == 1):
    A = []
    B = [] 
    C = []    
    while True:
        try:
            filasA = int(input("Numero de filas de la matriz A: "))
            colA = int(input("Numero de columnas de la matriz A: "))
            for i in range(filasA):
                lista = []
                for j in range(colA):
                    valor = float(input(f"introduce datos dentro de la celda [{i+1}][{j+1}]: "))
                    lista.append(valor)
                A.append(lista)
            imprimirmatriz(A)
            filasB = int(input("Numero de filas de la matriz B: "))
            if (colA != filasB):
                print("El número de columnas de la matriz A no es igual al de renglones de la matriz B")
                continue
            colB = int(input("Numero de columnas de la matriz B: "))
            for i in range(filasB):
                lista = []
                for j in range(colB):
                    valor = float(input(f"introduce datos dentro de la celda [{i+1}][{j+1}]: "))
                    lista.append(valor)
                B.append(lista)
            imprimirmatriz(B)
            False
        except ValueError:
            print("Introduciste un dato no numérico, vuelve a introducir un número")
            continue
        break
        ####################################################################
    for i in range(filasA): #Numero de arreglos o filas de la nueva matriz
        arreglo = []
        for j in range(colB): #Numero de columnas de la nueva matriz
            sum = 0
            for k in range(filasB): 
                sum = sum + (A[i][k])*(B[k][j])
            arreglo.append(sum)
        C.append(arreglo)
        print("***********************************")
    imprimirmatriz(C)
    try: 
        opc = int(input("¿Deseas realizar otra multiplicación?\n1. Sí 2. No: "))
        if (opc > 2 or opc < 1):
            print("Introduciste una opción no válida, vuelve a introducir el número.")
            continue
    except ValueError:
        print("Introduciste un número no válido.")