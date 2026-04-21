#1. Pide a la usuaria que introduzca una frase.
frase = input ("introduce una frase:")

#1.Muestra: la longitud de la frase, la frase en mayúsculas, la frase en minúsculas
longitud = len (frase)
frasemayusculas = frase.upper()
fraseminusculas = frase.lower()

print(frase)
print("la longitud de la frase es:", longitud)
print("la frase en mayusculas es:", frasemayusculas)
print("la frase en minusculas es:", fraseminusculas)