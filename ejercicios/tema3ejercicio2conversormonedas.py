#1. Ejercicio 2: Conversor de monedas: pide a la usuaria una cantidad en euros.
cantidad_euros = float (input("escriba una cantidad en euros: "))

#2. Convierte la cantidad a: dólares (1 euro = 1.1 dólares). Libras (1 euro = 0.87 libras).

dolar = cantidad_euros * 1.1
libra = cantidad_euros * 0.87

#Muestra los resultados
print(cantidad_euros, "euros, es igual a", dolar, "dólares.")
print(cantidad_euros, "euros, es igual a", libra, "libras.")