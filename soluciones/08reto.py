# Reto #8: DECIMAL A BINARIO

#  * Crea un programa se encargue de transformar un número
#  * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.

def run():
    
    def convertir_binario(numero):  

        lista = [] 
 
        while True:

            if numero == 1 or numero == 0:
                    print(numero)
                    break

            if numero >= 2:            

                if numero == 2:
                    division = numero // 2
                    residuo = numero % 2
                    lista.append(residuo)
                    numero = division
                    lista.append(1)
                    lista=reversed(lista)
                    lista_cadena = "".join(str(i) for i in lista)
                    print(lista_cadena)
                    break
                
                if numero == 3:
                    division = numero // 2
                    residuo = numero % 2
                    lista.append(residuo)
                    lista.append(division)
                    lista_cadena = "".join(str(i) for i in lista)
                    print(lista_cadena)      
                    break

                else:
                    division = numero // 2
                    residuo = numero % 2
                    lista.append(residuo)
                    numero = division

            else:
                break

    convertir_binario(99)

if __name__=="__main__":
    run()