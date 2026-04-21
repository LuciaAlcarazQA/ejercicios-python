#1. Define los siguientes precios:

camiseta = 10
sudadera = 20.5
gorra = 5.5

#2.Pide a la usuaria la cantidad de cada artículo.
cantidad_camisetas = float (input("¿cuantas camisetas necesitas comprar?: "))
cantidad_sudaderas = float (input("¿cuantas sudaderas necesitas comprar?: "))
cantidad_gorras = float (input("¿cuantas gorras necesitas comprar?: "))

#3. Calcula el total de la compra.
total_de_la_compra = (camiseta*cantidad_camisetas) + (sudadera*cantidad_sudaderas) + (gorra*cantidad_gorras)

#4 Añade el 21% de IVA al total
IVA = (total_de_la_compra*21) / 100

#5. Muestra el precio final
precio_final = (total_de_la_compra + IVA)

#imprimir resultados
print("total de la compra",precio_final)
