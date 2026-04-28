#1. Pide a la usuaria un número entre 1 y 10.

#2. El número ganador es el 4.
#3. Muestra: Mensaje de victoria si acierta.Mensaje de derrota si falla.

def adivina_numero(numero):
    if numero == 4:
        return "mensaje de victoria: has ganado"
    elif numero in [1,2,3,5,6,7,8,9,10]:
        return "mensaje de derrota: has perdido"
    else:
        return "Número incorrecto"

numero = float(input("pide a la usuaria un numero entre 1 y 10: "))

print(adivina_numero(numero))