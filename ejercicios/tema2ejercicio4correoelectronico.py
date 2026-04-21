#1. Pide a la usuaria que introduzca una dirección de correo electrónico.
correo_electronico = input ("introduce una direccion de correo electronico:")

#2. Muestra: la longitud del correo, el correo en mayúsculas, el correo en minúsculas
longitud = len (correo_electronico)
correo_electronicomayusculas = correo_electronico.upper()
correo_electronicominusculas = correo_electronico.lower()

print(correo_electronico)
print("la longitud del correo electronico es:", longitud)
print("el correo electronico en mayusculas es:", correo_electronicomayusculas)
print("el correo electronico en minusculas es:", correo_electronicominusculas)
