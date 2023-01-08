# Reto #6: INVIRTIENDO CADENAS *o*

#  * Crea un programa que invierta el orden de una cadena de texto
#  * sin usar funciones propias del lenguaje que lo hagan de forma automática.
#  * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"

def run():

    def invertir_cadena(cadena):
        reves = cadena[::-1]
        print(reves)

    invertir_cadena("Hola mundo")

if __name__=="__main__":
    run()
