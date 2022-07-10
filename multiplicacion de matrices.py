def imprimirmatriz(matriz):
    nomren = len(matriz)
    for x in range (nomren):
        print(matriz[x])
#Multiplicacion de matrices
#Regla principal: El numero de columnas de la matriz izquierda debe ser igual al de filas de la matriz derecha.
opc = 1
while (opc == 1):
    A = []
    B = [] 
    C = []    
    while True: #Llenado matrices A y B
        while True: #cantidad de filas y renglones
            try:
                filasA = int(input("Numero de filas de la matriz A: "))
                colA = int(input("Numero de columnas de la matriz A: "))
                break
            except ValueError:
                print("Introduciste un número no válido.")
                continue
        for i in range(filasA): #Llenado de Matriz A
            lista = []
            for j in range(colA):
                while True:
                    try:
                        valor = float(input(f"introduce datos dentro de la celda [{i+1}][{j+1}]: "))
                        break
                    except ValueError:
                        print("Introduciste un número no válido.")
                        continue
                lista.append(valor)
            A.append(lista)
        imprimirmatriz(A)
        while True: #cantidad de filas y renglones
            try:
                filasB = int(input("Numero de filas de la matriz B: "))
                if (colA != filasB):
                    print("El número de columnas de la matriz A no es igual al de renglones de la matriz B")
                    continue
                colB = int(input("Numero de columnas de la matriz B: "))
                break
            except ValueError:
                print("Introduciste un número no válido.")
                continue
        for i in range(filasB): #Llenado de Matriz B
            lista = []
            for j in range(colB):
                while True:
                    try:
                        valor = float(input(f"introduce datos dentro de la celda [{i+1}][{j+1}]: "))    
                        break
                    except ValueError:
                        print("Introduciste un número no válido.")
                        continue
                lista.append(valor)
            B.append(lista)
        imprimirmatriz(B)
        break #Cerramos llenado de Matrices A y B
        ####################################################################
    for i in range(filasA): #Algoritmo matemático
        arreglo = []
        for j in range(colB): #Numero de columnas de la nueva matriz
            sum = 0
            for k in range(filasB): 
                sum = sum + (A[i][k])*(B[k][j])
            arreglo.append(sum)
        C.append(arreglo)
    print("***********************************\nMatriz resultado:") 
    imprimirmatriz(C)
    try: #Validamos si el usuario desea volver a usar el programa
        opc = int(input("¿Deseas realizar otra multiplicación?\n1. Sí 2. No: "))
        if (opc > 2 or opc < 1):
            print("Introduciste una opción no válida, vuelve a introducir el número.")
            continue
    except ValueError:
        print("Introduciste un número no válido.")