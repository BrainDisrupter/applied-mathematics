#Metodo por Gauss Jordan. Sólo matrices cuadráticas o de una columna o renglon de más. (No. de columnas y renglones diferidos dan normalmente soluciones infinitas o incógnitas)
while True:
    try:
        ren = int(input("Solución de sistemas de ecuaciones lineales por método de Gauss Jordan. Introduce tu número de renglones: "))
        col = int(input("Introduce tu número de columnas: "))
        if (ren<=col-2 or ren>=col+2):
            print("Tanto el número de renglones como de columnas deben ser iguales o deben tener una diferencia de 1. Vuelve a introducir tu cantidad de renglones y columnas.")
            continue
        break
    except ValueError:
        print("Introduciste un dato no numérico, vuelve a introducir un número")
        continue
matrix=[]
for r in range (ren):
    nren = []
    for c in range(col):
        while True:
            try:
                num = int(input(f"Introduce el número de la celda [{r+1}][{c+1}]: "))
                nren.append(num)
                break
            except ValueError:
                print("Introduciste un dato no numérico, vuelve a introducir un número")
                continue
    matrix.append(nren)
def imprimirmatriz(matrix):
    nomren = len(matrix)
    for x in range (nomren):
        print(matrix[x])
def acomododerenglones(matrix):
    bool = False
    matrix2 = []
    #sum1s = 0 #Cantidad de 1s o -1s
    #sumneg1s = 0
    r=0
    sumneg1s = 0
    sum1s = 0
    #Sorteamos los renglones de menor a mayor segun la primera celda, o séase, checamos todos los A[r][0]
    while (r<=ren-1): #Primero buscamos los valores de -1 y 1, si sólo hay un -1 en la columna, se ubica su renglón como el primero, 
        if (matrix[r][0] == -1): #pero si hay un 1 se toma el renglón de este otro (se prioriza el 1 para facilitar el método de Gauss Jordan,
            matrix2.append(matrix[r]) #esto lo podrá ver el usuario)
            r2 = r #r2 es el valor del no. de renglon donde se ubica el primer o unico 1 (Es el valor que se evitará, no queremos introducirlo 2 veces en la matriz)
            bool = True
            sumneg1s += 1
        elif (matrix[r][0] == 1):
            matrix2.clear()
            matrix2.append(matrix[r])
            r2 = r
            bool = True
            sum1s += 1
            break
        r+=1    
    r=0
    lista=[]
    while(r<=ren-1):
        if (bool == True): #Dado que r2 está definido
            if (r != r2):
                lista.append(matrix[r][0]) #Agregamos todos los valores de la columna evitando r2.
        else: #Dado que r2 no esta definido
            lista.append(matrix[r][0])
        r+=1
    lista.sort() #La sorteamos en orden ascendente
    print("***************LISTA SORTEADA***************")
    print(lista) #Lista impresa para verificar que esta parte va bien.
    print("***************PRIMER RENGLÓN PARA HACER PIVOTE***************")
    print(matrix2) #Lista impresa para verificar que esta parte va bien.
    r=0
    if (bool == True): #Dado que r2 está definido
        while(r<=ren-2): #Vamos acomodando cada renglón en la nueva matriz según el sort, checamos los valores de la primera columna de la matriz original
            check = 0 # y comparamos uno a uno si es igual al de la posición actual de la lista sorteada en orden ascendente
            while (check<=ren-1):
                if (lista[r]==matrix[check][0]):
                    matrix2.append(matrix[check])
                    break
                check += 1
            r+=1
    else: #Dado que r2 no esta definido
        r=0
        while(r<=ren-1): #Vamos acomodando cada renglón en la nueva matriz según el sort, checamos los valores de la primera columna de la matriz original
            check = 0 # y comparamos uno a uno si es igual al de la posición actual de la lista sorteada en orden ascendente
            while (check<=ren-1):
                if (lista[r]==matrix[check][0]):
                    matrix2.append(matrix[check])
                check += 1
            r+=1
    print("**************MATRIZ NUEVA SORTEADA****************")
    imprimirmatriz(matrix2)
    if ((sum1s+sumneg1s) > 2): #Fuck it, lo dejamos como está. XD
        matrix2 = matrix
    return matrix2

def gaussjordan(matrix):
    matrix3 = []
    for r in range(ren-1): #ren-1 nos ubica la posición máxima, según el número de renglones
        nvren2 = [] #Eje.: Usuario introduce 4, entonces tenemos hasta la posición 3
        pivote = matrix[r][r] 
        


print("**************MATRIZ ORIGINAL****************")
imprimirmatriz(matrix)
acomododerenglones(matrix)
#Normalmente si uno ordena de forma descendente una matriz será más facil de resolver, en la práctica común tomamos primero los renglones con 1
#para acelerar el desarrollo, podemos poner en orden descendente los demás renglones según la primera columna.

