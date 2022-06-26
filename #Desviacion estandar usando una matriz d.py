#Desviaciones estandar usando los numeros de cada columna de una matriz generada (usando la formula para muestras de datos no agrupados)
matrizA=[]
def llenado(A):
    numren = int(input("Introduce la cantidad de renglones de tu matriz a formar: "))
    numcol = int(input("Introduce la cantidad de columnas de tu matriz a formar: "))
    for x in range (numren):
        lista=[]
        for y in range (numcol):
            valor = int(input(f"Introduce el valor de la celda [{x+1}][{y+1}]: "))
            lista.append(valor)
        A.append(lista)
    imprimirmatriz(A)
    return(A)
def imprimirmatriz(B):
    numren = len(B)
    for x in range (numren):
        print(B[x])
def desvest(C):
    numren = len(C)
    numcol = len(C[0])
    promedios=[]
    for x in range (numcol):
        sum = 0
        for y in range(numren):
            num = C[y][x]
            sum = sum + num
        prom = sum/numren
        promedios.append(prom)
    sum2=0
    for x in range (numcol):
        sum2=0
        for y in range(numren):
            parentesis=(C[y][x]-promedios[x])**2
            sum2=sum2+parentesis
        desvest=(sum2/(numren-1))**(1/2)
        print(f"La desviación estandar de la columna {x} es: {desvest}")
d = llenado(matrizA)
desvest(d)
