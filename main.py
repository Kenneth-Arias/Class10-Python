# Proyecto: [Nombre del Proyecto]
# Estudiante: [Nombre del Estudiante]
# Fecha de Inicio: [dd/mm/aaaa]
# Fecha de Entrega: [dd/mm/aaaa]
# Descripción: Este archivo contiene el punto de entrada principal del proyecto.
# Recuerda incluir tu nombre completo, la fecha en la que iniciaste el proyecto y la fecha estimada de entrega.
# Esto ayuda a mantener un registro claro del trabajo realizado.

from analisis_datos import *

lista_compra = generar_lista_compras()

#Antes del for se analiza lo que se quiere a la hora de analizar diccionarios o tuplas
precios = [precio for producto, precio in lista_compra]

print(precios)

print(lista_compra)

print(media)

print(mediana)
