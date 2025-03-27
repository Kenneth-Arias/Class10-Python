# estadisticas.py
def media(datos):
    media_aritmetica = sum(datos) / 5
    return media_aritmetica

def mediana(datos):
    #Mediana

    datos = sorted(datos)

    #Cantidad

    n = len(datos)

    mitad = n // 2

#   0     1     2     3
#(1000, 2000, 3000, 4000)

    if n % 2 == 0:
        mediana = (datos[mitad -1] + datos [mitad]) / 2 
    else:
        mediana = datos[mitad]

    print("La mediana de la compra es de: ", mediana)