#1. Pide a la usuaria que elija un color
def pedir_color():
    color = input("Elige un color (rojo, verde, azul, amarillo, morado): ")
    return color

#2. Muestra un mensaje según el color elegido:

def mostrar_mensaje(color):
    if color == "rojo":
        mensaje = "rojo: pasion y energia"
    elif color == "verde":
        mensaje = "verde: esperanza y crecimiento"
    elif color == "azul":
        mensaje = "azul: calma y serenidad"
    elif color == "amarillo":
        mensaje = "amarillo: felicidad y optimismo"
    elif color == "morado":
        mensaje = "morado: sabiduria y creatividad"
    else:
        mensaje = "color no valido"
