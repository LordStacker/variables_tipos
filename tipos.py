#tipo de dato que signigica nada
nada = None
cadena = "hola soy nicola martinez clemente"
entero = 99
flotante = 4.2
booleano = False
lista = [10, 20 , 30 , 100, 200]
listaString = [10, "treinta", 30, "cuatenta"]
tuplaNoCambia = ("master", "en", "python")
diccionario = {
    "nombre" : "Nicola",
    "apellido": "Martinez",
    "curso": "Master en python"
}
rango = range(9)
dato_byte = b"Probando"

#imprimir variable
print(dato_byte)

#mostrar tipo de dato
print(type(dato_byte))
#como convertir datos
texto = "Hola soy un texto"
numerito = str(762)
print(type(numerito))
#no puedo concatenar texto con int
print(texto + " " + numerito) 

numerito = int(762)
print(type(numerito))
numerito = float(762)
print(type(numerito))