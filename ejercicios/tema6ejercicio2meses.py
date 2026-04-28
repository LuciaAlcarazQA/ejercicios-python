#1 Crea una lista con los 12 meses del año.
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

#2 Pide a la usuaria un número del 1 al 12.
numero = float(input("Introduce un numero del 1 al 12: "))

# Muestra el mes correspondiente.
if numero >= 1 and numero <= 12:
    mes = meses[numero - 1]
    print("el mes es:", mes)

    # Si el mes es junio, muestra además el mensaje: EL MEJOR MES.
    if mes == "junio":
        print("EL MEJOR MES")
else:
    print("numero invalido")
