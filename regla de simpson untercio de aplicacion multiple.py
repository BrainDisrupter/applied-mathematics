def f(x):
    #Función principal
   return ((x**5)-(2*x**3)+4)
def metodosimpson13(a,b):
    #Obtenemos el valor de x
    while True:
        try:
            x = float(input("Introduce el valor de 'x': "))
            break
        except ValueError:
            print("Introduciste un dato no numérico, vuelve a introducir un número")
            continue
    #Obtenemos el numero de intervalos
    while True:
        #Iteracion para validar los datos introducidos del usuario
        try:
            n = int(input("¿Cuántos intervalos quieres formar? Sólo cantidades pares."))
            if (n%2 == 0):
                break
            else:
                print("Tu número es impar, reintroduce un número.")
        except ValueError:
            print("Haz introducido un carácter inválido o un número decimal, reintroduce el dato.")
            continue
    amplitud = (b-a)/n
    #Evaluacion de f en 'x' inicial
    primerev = f(a)
    #Suma de ordenadas impares
    i=1
    sum1=0
    while (i <= n-1):
        evaluar = f(a+i*amplitud)
        sum1 += evaluar
        i+=2
    #Suma de ordenadas pares
    j=2
    sum2 = 0
    while(j <= n-2):
        evaluar = f(a+j*amplitud)
        sum2+= evaluar
        j+=2
    #Evaluacion de f en 'x' final
    ultimaev = f(b)
    #Resultado final
    intdefaprox = (b-a)*(primerev + 4*sum1 + 2*sum2 + ultimaev)/(3*n)
    print(f"Nuestra integral aproximada es de: {intdefaprox:.8f}")
while True:
    try:
        print("Metodo de Simpson 1/3 en aplicación múltiple para calcular la integral definida de una función.")
        a = float(input("Dame el primer limite: "))
        b = float(input("Dame el segundo limite: "))
        if (a>b):
            a, b = b, a
            #Volteamos los valores si acaso el usuario se equivoca poniendo el primer limite como el mayor :)
        resultado = metodosimpson13(a,b)
    except ValueError:
        print("Haz introducido un carácter inválido.")
        continue
    break