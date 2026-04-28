#1 Crea una lista con los 8 planetas del sistema solar.
planetas = ["mercurio", "venus", "tierra", "marte", "jupiter", "saturno", "urano", "neptuno"]

#2 Pide a la usuaria un número del 1 al 8.
numero = float(input("Introduce un número del 1 al 8: "))

#3 Muestra el planeta correspondiente. 4 Comprobar si el número es válido
if numero >= 1 and numero <= 8:
    print("El planeta es:", planetas[numero - 1])
else:
    print("Número inválido")