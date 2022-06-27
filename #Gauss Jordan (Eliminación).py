#Solución de sistemas de ecuaciones lineales por Gauss-Jordan por eliminación
from decimal import DivisionByZero
from re import X
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
    if (fil == col-1 or fil == col): #Para que un sistema de ecuaciones lineales sea resuelto, solo puede haber una diferencia maxima de 1 entre los renglones y columnas y únicamente la cant. de renglones puede ser menor.
        for i in range(fil):
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
        while True:
            for i in range(fil):
                pivote = A[i][i]
                for j in range(col):
                    try:
                        A[i][j] = A[i][j]/pivote #Dividimos renglon pivote entre su pivote
                    except ZeroDivisionError or DivisionByZero:
                            A[i][j] = 0.0
                print("\nMATRIZ DE REFERENCIA")
                imprimirmatriz(A)
                print(f"RENGLÓN PIVOTE: R{i+1}. DIVIDIDO ENTRE {pivote}")
                for l in range(fil):
                    if (l != i):
                        multiplo = A[l][i]
                        print(f"R{i+1} x {multiplo} - R{l+1}")
                        for k in range(col):
                            A[l][k] = A[l][k]-(A[i][k]*multiplo)
                print("MATRIZ NUEVA")
                imprimirmatriz(A)
                print("*****************")
            if (A[fil-1][col-2]==1): #Si a la izquierda hay un 1 hasta la parte inferior, decimos que tiene solución única.
                print("\nEste S.E.L tiene solución única.")
            elif(A[fil-1][col-2]==0 and A[fil-1][col-1]==0): #Si los 2 ultimos valores de la parte inferior son 0, decimos que tiene soluciones infinitas.
                print("\nEste S.E.L tiene soluciones infinitas.")
            elif(A[fil-1][col-2]==0 and A[fil-1][col-1]!=0): #Si el último valor del último renglón es diferente de 0, pero el izquierdo es igual a 0, decimos que el S.E.L no tiene solución.
                print("\nEste S.E.L no tiene solución.")
            break
        print("INCÓGNITAS: ")
        for i in range(fil):
            vecsolu.append(A[i][fil])
            print(f"X1: {A[i][fil]}")
        print("VECTOR SOLUCION: ")
        print(vecsolu)
        print("MATRIZ RESUELTA")
        imprimirmatriz(A)
    else:
        opc = int(input("La diferencia entre renglones y columnas no es adecuada, el S.E.L sería irresoluble. \n¿Desea volver a introducir los datos? \n1.Sí 2.No: "))
        continue
    break