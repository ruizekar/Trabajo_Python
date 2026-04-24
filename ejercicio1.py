adulto = 790
adultom = 390
estudiante = 490 
print("------Bienvenido al METRO TREN------")
usuario = input("Ingrese usuario: ")
tarifa = input("Ingrese horario, (NORMAL - PUNTA): ")
if usuario == "Adulto" and tarifa == "Normal":
    print(f"{adulto} es la tarifa de su pasaje")
elif usuario == "Adulto" and tarifa == "Punta":
    print(f"{adulto+100} es la tarida de su pasaje en hora punta")
if usuario == "Estudiante" and tarifa == "Normal":
    print(f"{estudiante} es la tarifa de su pasaje")
elif usuario == "Estudiante" and tarifa == "Punta":
    print(f"{estudiante+100} es la tarifa de su pasaje en hora punta")
if usuario == "Adulto Mayor" and tarifa == "Normal":
    print(f"{adultom} es la tarifa de su pasaje")
elif usuario == "Adulto Mayor" and tarifa == "Punta":
    print(f"{adultom+100} es la tarifa de su pasaje en hora punta")
print("Gracias por viajar con nosotros!")
