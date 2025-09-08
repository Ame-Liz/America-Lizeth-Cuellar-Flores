dato1 = int(input("Dato 1: "))
dato2 = int(input("Dato 2: "))
dato3 = int(input("Dato 3: "))

if (dato1 > dato2 and dato1 < dato3) or (dato1 < dato2 and dato1 > dato3):
    print("El número", dato1, "es mayor que", min(dato2, dato3), "y menor que", max(dato2, dato3))
elif (dato2 > dato1 and dato2 < dato3) or (dato2 < dato1 and dato2 > dato3):
    print("El número", dato2, "es mayor que", min(dato1, dato3), "y menor que", max(dato1, dato3))
elif (dato3 > dato1 and dato3 < dato2) or (dato3 < dato1 and dato3 > dato2):
    print("El número", dato3, "es mayor que", min(dato1, dato2), "y menor que", max(dato1, dato2))
else:
    print("\n...EL DATO INGRESADO NO HA SIDO VALIDO...")
