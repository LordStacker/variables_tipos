"""
una variables es un contenedor de informacion
que dentro guardara un dato x, se pueden crear
n numeros de variables y que cada una tenga un dato 
distinto.
"""
#crear variables y asignar valor

texto = "Master en python"
texto_2 = "con victor robles"
numero = 45
decimal = 6.7
#mostrar valores de variables asignadas

print(texto)
print(texto_2)
print (numero)
print (decimal)

print("---------")
#sustituir el valor de algunas variables / reasignar variables

numero = 77
decimal = 8.9
print (numero)
print (decimal)
#concatenacion
"""Unir dos variables o dos string"""

nombre = "Nicola"
apellidos = "Clemente"
web = "nicolaweb.ve"
print(nombre + " " + apellidos + " - " + web)
# f antes de ingresar en print hace interpolacion (cualquier string)
print(f"{nombre} {apellidos} - {web}")
#metodo format
print("Hola me llamo {} {} y mi web es: {}".format(nombre, apellidos, web))
#print(nombre, apellidos, web) aqui no se concatena solo se usa variables a print



