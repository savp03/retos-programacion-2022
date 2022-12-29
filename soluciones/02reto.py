#Reto #2: LA SUCESIÓN DE FIBONACCI

#  * Escribe un programa que imprima los 50 primeros números de la sucesión
#  * de Fibonacci empezando en 0.
#  * - La serie Fibonacci se compone por una sucesión de números en
#  *   la que el siguiente siempre es la suma de los dos anteriores.
#  *   0, 1, 1, 2, 3, 5, 8, 13...

def run():
    
    var1 = 0
    var2 = 1
    print (var1)    

    for x in range(50):      
        fib = var1 + var2
        var2 = var1
        var1 = fib
        print(fib)

if __name__ == ("__main__"):
    run()

