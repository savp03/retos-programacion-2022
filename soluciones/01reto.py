#Reto #1: ¿ES UN ANAGRAMA?

#  * Escribe una función que reciba dos palabras (String) y retorne
#  * verdadero o falso (Bool) según sean o no anagramas.
#  * - Un Anagrama consiste en formar una palabra reordenando TODAS
#  *   las letras de otra palabra inicial.
#  * - NO hace falta comprobar que ambas palabras existan.
#  * - Dos palabras exactamente iguales no son anagrama.

def run():

    def es_anagrama(palabra_uno , palabra_dos):
        lista_uno = list(palabra_uno)
        lista_dos = list(palabra_dos)
        if palabra_uno == palabra_dos:
            print("Las palabras son iguales")
        elif set(lista_uno)==set(lista_dos):
            print("Las palabras son acronimo")
        else:
            print("Las palabras no son acronimo")
        
    es_anagrama("roma" , "amor")

if __name__=="__main__":
    run()