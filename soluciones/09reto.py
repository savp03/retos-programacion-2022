# /*
#  * Crea un programa que sea capaz de transformar texto natural a código
#  * morse y viceversa.
#  * - Debe detectar automáticamente de qué tipo se trata y realizar
#  *   la conversión.
#  * - En morse se soporta raya "—", punto ".", un espacio " " entre letras
#  *   o símbolos y dos espacios entre palabras "  ".
#  * - El alfabeto morse soportado será el mostrado en
#  *   https://es.wikipedia.org/wiki/Código_morse.
#  */
import re

def run():

    def transformar_cadena(cadena):

        cadena_transformada = ""

        dicccionario_letra_morse={
            "a": ".-",
            "b": "-...",
            "c": "-.-.",
            "ch": "----",
            "d": "-..",
            "e": ".",
            "f": "..-.",
            "g": "--.",
            "h": "....",
            "i": "..",
            "j": ".---",
            "k": "-.-",
            "l": ".-..",
            "m": "--",
            "n": "-.",
            "ñ": "——·——",
            "o": "---",
            "p": ".--.",
            "q": "--.-",
            "r": ".-.",
            "s": "...",
            "t": "-",
            "u": "..-",
            "v": "...-",
            "w": ".--",
            "x": "-..-",
            "y": "--..",
            "z": "--..",
            "0": "—————",
            "1": ".----",
            "2": "..---",
            "3": "...--",
            "4": "...._",
            "5": ".....",
            "6": "-....",
            "7": "--...",
            "8": "---..",
            "9": "----.",
            ".": ".-.-.-",
            ",": "--..--",
            "?": "..--..",
            "/": "-..-."
            }

        dicccionario_morse_letra = {value: key for key, value in dicccionario_letra_morse.items()}

        if bool(re.search("[a-zA-Z]", cadena)) == True or bool(re.search("[0-9]", cadena)) == True:
            for letra in cadena:
                if letra.lower() in dicccionario_letra_morse:
                    cadena_transformada = cadena_transformada +  dicccionario_letra_morse[letra.lower()] + " " 
                if letra == " ":
                    letra = "  "
                    cadena_transformada = cadena_transformada + letra

        else:
            cadena_morse = cadena.split(" ")
            for palabra in cadena_morse:
                if palabra in dicccionario_morse_letra:
                    cadena_transformada += dicccionario_morse_letra[palabra]
                else:
                    cadena_transformada += " "
                    
        print(cadena_transformada)

    transformar_cadena("Martes de Modo Guerra")    
    transformar_cadena("-- .- .-. - . ...   -.. .   -- --- -.. ---   --. ..- . .-. .-. .-")

if __name__ =="__main__":
    run()
