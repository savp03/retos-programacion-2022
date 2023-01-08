# Reto #4: ÁREA DE UN POLÍGONO

#  * Crea una única función (importante que sólo sea una) que sea capaz
#  * de calcular y retornar el área de un polígono.
#  * - La función recibirá por parámetro sólo UN polígono a la vez.
#  * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
#  * - Imprime el cálculo del área de un polígono de cada tipo.

def run():
    def calcula_area(figura , altura, base=None):
        if figura == "Triangulo":
            area = altura * base  / 2
            print(area)
        elif figura == "Cuadrado":
            area = altura * altura
            print(area)
        elif figura == "Rectangulo":
            area = base * altura 
            print(area)
        else:
            print("La figura no es valida. ")
            exit()

    calcula_area("Triangulo" , 20 , 47)
    calcula_area("Cuadrado" , 4)
    calcula_area("Rectangulo" , 20 , 2)
    calcula_area("Circulo" , 20 , 2)

if __name__ == "__main__":
    run()