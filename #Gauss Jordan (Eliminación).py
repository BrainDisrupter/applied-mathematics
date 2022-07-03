#Solución de sistemas de ecuaciones lineales por Gauss-Jordan por eliminación
from decimal import DivisionByZero
def imprimirmatriz(matriz):
    numren = len(matriz)
    numcol = len(matriz[0])
    for i in range (numren):
        for j in range(numcol):
            if (matriz[i][j] == -0.0):
                matriz[i][j] = 0.0
        print("[",matriz[i],"]")
opc = 1
while opc==1:
    vecsolu = [] #Vector solucion
    A = []
    fil = int(input("Introduce el número de renglones: "))
    col = int(input("Introduce el número de columnas: "))
    if (fil == col-1): #Para que un sistema de ecuaciones lineales sea resuelto, debe haber una diferencia maxima de 1 entre los renglones y columnas y únicamente la cant. de renglones puede ser menor.
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
        #for i in range(fil):
        print("\nMATRIZ INICIAL:")
        imprimirmatriz(A)
        print("************************************")
        if (A[0][0] == 0): #Dado que hubiera un 0 en A1,1 en el primer renglon, lo intercambiamos por uno que tenga un valor diferente de 0 en su primera columna.
            i=1
            while i<fil:
                if (A[i][0]!=0):
                    A[0],A[i] = A[i],A[0]
                    break
                i+=1
            print(f"\nINTERCAMBIAMOS RENGLON 1 POR RENGLON {i+1} DEBIDO AL CERO INICIAL")
            imprimirmatriz(A)
        for i in range(fil): #Procedimiento Gauss-Jordan (Eliminación)
            pivote = A[i][i]
            for j in range(col):
                try:
                    A[i][j] = A[i][j]/pivote #Dividimos renglon pivote entre su pivote
                except ZeroDivisionError or DivisionByZero:
                    A[i][j] = 0
            print("\nMATRIZ DE REFERENCIA")
            imprimirmatriz(A)
            for l in range(fil):
                if (l != i):
                    multiplo = A[l][i]
                    print(f"R{l+1} - R{i+1} x {multiplo} => R{l+1}")
                    for k in range(col):
                        A[l][k] = A[l][k]-(A[i][k]*multiplo)
            print("\nMATRIZ NUEVA")
            imprimirmatriz(A)
            print("************************************")
        if (A[fil-1][col-2]==1): #Si a la izquierda hay un 1 hasta la parte inferior, decimos que tiene solución única.
            print("\nEste S.E.L tiene solución única.")
        elif(A[fil-1][col-2]==0 and A[fil-1][col-1]==0): #Si los 2 ultimos valores de la parte inferior son 0, decimos que tiene soluciones infinitas.
            print("\nEste S.E.L tiene soluciones infinitas.")
        elif(A[fil-1][col-2]==0 and A[fil-1][col-1]!=0): #Si el último valor del último renglón es diferente de 0, pero el izquierdo es igual a 0, decimos que el S.E.L no tiene solución.
            print("\nEste S.E.L no tiene solución.")
        print("\nINCÓGNITAS: ")
        for i in range(fil): #Llenado de vector solución
            vecsolu.append(A[i][fil])
            print(f"X{i+1}: {A[i][fil]}")
        print("\nVECTOR SOLUCION: ")
        print(vecsolu)
        print("\nMATRIZ RESUELTA")
        imprimirmatriz(A)
    else:
        opc = int(input("La diferencia entre renglones y columnas no es adecuada, el S.E.L sería irresoluble. \n¿Desea volver a introducir los datos? \n1.Sí 2.No: "))
        continue
    break