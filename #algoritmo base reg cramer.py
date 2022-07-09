def solucRegCramer(A):
    recorrido = len(A[0]) #Cantidad de columnas y de determinantes
    determinantes = []
    #Ciclo para formar las diferentes determinantes
    for i in range (recorrido): #Cantidad de determinantes
        B=[]
        if i == 0:
            m = recorrido-1
        for j in range(recorrido-1): #Cantidad de filas
            lista = []
            for k in range(recorrido-1): #Cantidad de columnas
                if (k!=m):
                    lista.append(A[j][k]) #Introducimos el valor respetando el orden
                else:
                    lista.append(A[j][recorrido-1]) #Ignoramos el valor correspondiente a dicho renglon y columna e introducimos el 
            B.append(lista)                         #que corresponde al mismo renglon pero que está ubicado en la ultima columna
        m = i
        determinantes.append(detGaussJordanEli(B)) #Calculo de las determinantes(Uso el método de Gauss-Jordan por eliminación)
    for i in range(recorrido-1):
        solucion = determinantes[i+1]/determinantes[0] #Obtenemos las soluciones dividiendo cada determinante entre el principal
        solucion = 0
        print(f"Solución X{i+1}: ",solucion)