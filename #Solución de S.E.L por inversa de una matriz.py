#Solución de S.E.L por inversa de una matriz
from decimal import DivisionByZero

def imprimirmatriz(matriz):
    numren = len(matriz)
    numcol = len(matriz[0])
    for i in range (numren):
        for j in range(numcol):
            if (matriz[i][j] == -0.0):
                matriz[i][j] = 0.0
        print("[",matriz[i],"]")

def llenadomatriz(matriz):
    while True:    
        try:
            fil = int(input("Introduce el número de incógnitas: "))
            if (fil<1):
                print("Introduciste una cantidad no válida de incógnitas, vuelve a introducir el dato.")
                continue
            col = fil+1
            for i in range(fil): #Llenado de matriz
                renglon = []
                for j in range(col):
                    while True:    
                        try:
                            num = float(input(f"introduce el numero dentro de la celda [{i+1}][{j+1}]: "))
                            break
                        except ValueError:
                            print("Introduciste un carácter inválido, vuelve a introducir el número.")
                            continue
                    renglon.append(num)
                matriz.append(renglon)
            break
        except ValueError:
            print("Introduciste un carácter inválido, vuelve a introducir el dato.")
            continue
    if matriz[0][0] == 0:
        i = 1
        while i<fil:
            if matriz[i][0] != 0:
                matriz[0],matriz[i] = matriz[i],matriz[0]
                print(f"Intercambiamos renglón 1 por renglón {i+1} debido al cero inicial en el primero.")
            break
    print("\nMatriz inicial.")
    imprimirmatriz(matriz)
    return matriz

def matrizinversa(matriz):
    vecindep = []
    numren = len(matriz)
    for i in range (numren):
        vecindep.append(matriz[i][numren])
        matriz[i].pop()
        for j in range(numren):
            if (i==j):
                valor = 1
                matriz[i].append(valor)
            else:
                valor = 0
                matriz[i].append(valor)
    print(f"\nVector de valores independientes:\n",vecindep)
    for i in range(numren): #Procedimiento Gauss-Jordan (Eliminación)
        pivote = matriz[i][i]
        print(f"\nR{i+1}/{pivote}=R{i+1}")
        for j in range(numren*2):
            try:
                matriz[i][j] = matriz[i][j]/pivote #Dividimos renglon pivote entre su pivote
            except ZeroDivisionError or DivisionByZero:
                matriz[i][j] = 0
        print("\nMATRIZ DE REFERENCIA")
        imprimirmatriz(matriz)
        for l in range(numren):
            if (l != i):
                multiplo = matriz[l][i]
                print(f"\nR{l+1} - R{i+1} x {multiplo} => R{l+1}")
                for k in range(numren*2):
                    matriz[l][k] = matriz[l][k]-(matriz[i][k]*multiplo)
        print("\nMATRIZ NUEVA")
        imprimirmatriz(matriz)

    Ainversa=[]
    for i in range(numren):
        renglon=[]
        for l in range(numren):
            renglon.append(matriz[i][l+numren])
        Ainversa.append(renglon)
    print("\n************MATRIZ INVERSA************")
    imprimirmatriz(Ainversa)
    print("\nINCÓGNITAS")
    for i in range(numren): #Algoritmo matemático
        sum = 0
        for j in range(numren): #Numero de columnas de la nueva matriz
            sum = sum + (Ainversa[i][j])*(vecindep[j])
            print(f"{Ainversa[i][j]} x [{vecindep[j]}] = {sum}")
        print(f"\nLa suma de los anteriores resultados nos da: X{i+1} = {sum}\n")

opc = 1
while opc == 1:
    A=[]
    matrizinversa(llenadomatriz(A))
    try:    
        opc = int(input("¿Desea volver a resolver otro sistema de ecuaciones lineales? 1. Sí 2. No: "))
        if (opc<1 or opc>2):
            print("Introduciste una opción no reconocida, vuelve a elegir una opción.")
    except ValueError:
        print('Ingresaste un carácter inválido, vuelve a introducir el dato.')
