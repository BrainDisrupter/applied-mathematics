#Metodo de montante para solución de S.E.L
def imprimirmatriz(A):
    numren = len(A)
    numcol = len(A[0])
    for i in range (numren):
        for j in range(numcol):
            if (A[i][j] == -0.0):
                A[i][j] = 0.0
        print("[",A[i],"]")

def llenadomatriz(A):
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
                A.append(renglon)
            break
        except ValueError:
            print("Introduciste un carácter inválido, vuelve a introducir el dato.")
            continue
    if A[0][0] == 0:
        i = 1
        while i<fil:
            if A[i][0] != 0:
                A[0],A[i] = A[i],A[0]
                print(f"Intercambiamos renglón 1 por renglón {i+1} debido al cero inicial en el primero.")
            break
    print("\nMatriz inicial.")
    imprimirmatriz(A)
    return A

A = []

def metMontante(A):
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
    print("************A INICIAL************")
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
            print("\n************A NUEVA************")
        elif (i == numfil-1):
            print("\n************A FINAL************")
        imprimirmatriz(A)    

opc = 1

while opc == 1:
    metMontante(llenadomatriz(A))
    try:    
        opc = int(input("¿Desea volver a resolver otro sistema de ecuaciones lineales? 1. Sí 2. No: "))
        if (opc!=1 or opc!=2):
            print("Introduciste una opción no reconocida, vuelve a elegir una opción.")
    except ValueError:
        print('Ingresaste un carácter inválido, vuelve a introducir el dato.')