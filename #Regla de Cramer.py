#Solución de S.L.E por regla de Cramer
from decimal import DivisionByZero
A = []
def llenadomatriz(matriz):
    while True:    
        try:
            fil = int(input("Introduce el número de incógnitas: "))
            if (fil<1):
                print("Introduciste una cantidad no válida de incógnitas, vuelve a introducir el dato.")
                continue
            break
        except ValueError:
            print("Introduciste un carácter inválido, vuelve a introducir el dato.")
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
                    print("Introduciste un carácter inválido.\nVuelve a introducir el número.")
                    continue
            renglon.append(num)
        A.append(renglon)
    print("\nMatriz inicial.")
    imprimirmatriz(A)
    return matriz

def imprimirmatriz(matriz):
    numren = len(matriz)
    numcol = len(matriz[0])
    for i in range (numren):
        for j in range(numcol):
            if (matriz[i][j] == -0.0):
                matriz[i][j] = 0.0
        print("[",matriz[i],"]")

def detGaussJordanEli(matriz):
    recorrido = len(matriz[0])
    for i in range(recorrido): #Procedimiento Gauss-Jordan (Eliminación)
        print(f"\nREFERENCIA {i+1}")
        imprimirmatriz(matriz)
        for l in range(i,recorrido):
            if (l != i):
                try:
                    multiplo = matriz[l][i]/matriz[i][i]*(-1)
                except ZeroDivisionError:
                    multiplo = 0.0
                print(f"R{l+1} - R{i+1} x {multiplo} => R{l+1}")
                for k in range(i,recorrido):
                    matriz[l][k] = matriz[i][k]*multiplo + matriz[l][k]
    sumdet = 1
    for i in range(recorrido):
        sumdet = sumdet*matriz[i][i]
    if (sumdet == -0.0):
        sumdet = 0.0
    return sumdet

def solucRegCramer(A):
    recorrido = len(A[0]) #Cantidad de filas = Cantidad de columnas en cada determinante
    determinantes = []
    for i in range (recorrido): #Cantidad de determinantes
        B=[]
        if i == 0:
            m = recorrido-1
        for j in range(recorrido-1): #Cantidad de filas
            lista = []
            for k in range(recorrido-1): #Cantidad de renglones
                if (k!=m):
                    lista.append(A[j][k])
                else:
                    lista.append(A[j][recorrido-1])
            B.append(lista)
        m = i
        print(f"\nDETERMINANTE A{i+1}")
        imprimirmatriz(B)
        determinantes.append(detGaussJordanEli(B))
        if (i==0):    
            print(f"\nResultado de determinante principal: {determinantes[i]}")
        else:
            print(f"\nResultado de determinante A{i+1}: {determinantes[i]}")
    for i in range(recorrido-1):
        solucion = determinantes[i+1]/determinantes[0]
        print(f"Solución X{i+1}: ",solucion)

opc = 1

while opc == 1:
    llenadomatriz(A)
    solucRegCramer(A)
    try:    
        opc = int(input("¿Desea volver a resolver otro sistema de ecuaciones lineales? 1. Sí 2. No: "))
        if (opc!=1 or opc!=2):
            print("Introduciste una opción no reconocida, vuelve a elegir una opción.")
    except ValueError:
        print('Ingresaste un carácter inválido, vuelve a introducir el dato.')