# Reto #7: CONTANDO PALABRAS **INCOMPLETO**

#  * Crea un programa que cuente cuantas veces se repite cada palabra
#  * y que muestre el recuento final de todas ellas.
#  * - Los signos de puntuación no forman parte de la palabra.
#  * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
#  * - No se pueden utilizar funciones propias del lenguaje que
#  *   lo resuelvan automáticamente.

import string

def run(): 

    def contar_palabras(oracion):
        oracion = oracion.lower()        
        lista = oracion.split()

        cuenta = {}

        for palabra in lista:
            if palabra in cuenta:
                cuenta[palabra] += 1
            else:
                cuenta[palabra] = 1

        print(cuenta)

    contar_palabras("Hola mundo Hola mundo Hola mundo Hola mundo")

if __name__ == "__main__":
    run()