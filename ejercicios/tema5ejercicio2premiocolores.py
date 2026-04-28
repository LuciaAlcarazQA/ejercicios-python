#1. Pide a la usuaria 5 veces que introduzca un color.
#2. Si la usuaria introduce el color azul, muestra que el premio ha sido conseguido. Si no, dile que pruebe otro color.


for i in range(5):
    color = input("Introduce un color: ")

    if color == "azul":
        print("¡Premio conseguido!")
        premio = True
    else:
        print("Prueba otro color")

if not premio:
    print("No has conseguido el premio")