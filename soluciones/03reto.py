#Reto #3: ¿ES UN NÚMERO PRIMO?

# * Escribe un programa que se encargue de comprobar si un número es o no primo.
# * Hecho esto, imprime los números primos entre 1 y 100.

def run():
    
    i = 1

    while i<100:
        if i == 2 or i == 3 or i == 5 or i ==7:
            print(i)
        elif i == 1 or i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
            pass
        else:
            print(i)
        i += 1

if __name__ == "__main__":
    run()