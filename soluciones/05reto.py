# Reto #5: ASPECT RATIO DE UNA IMAGEN

#  * Crea un programa que se encargue de calcular el aspect ratio de una
#  * imagen a partir de una url.
#  * - Url de ejemplo: https://raw.githubusercontent.com/mouredev/
#  *   mouredev/master/mouredev_github_profile.png
#  * - Por ratio hacemos referencia por ejemplo a los "16:9" de una
#  *   imagen de 1920*1080px.

import urllib.request
import io
from io import BytesIO
from PIL import Image
from fractions import Fraction

def run():
    
    # Descarga la imagen desde la URL
    with urllib.request.urlopen('https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png') as url:
        image_data = url.read()

    # Carga la imagen en memoria
    image = Image.open(io.BytesIO(image_data))

    # Obtiene el ancho y alto de la imagen
    width, height = image.size

    # Calcula el ratio de aspecto
    relacion_aspecto = Fraction(width, height)

    # Imprime el ratio de aspecto en la consola    
    print("El ratio de aspecto de la imagen es", relacion_aspecto)

if __name__=="__main__":
    run()