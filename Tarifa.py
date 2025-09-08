while True:
    dato1= int (input("Ingresa tu edad: "))

    if 120< dato1 > 0:
        print ("No puedes ingresar el 0 o mayor a 120")    
    elif 0<= dato1 <=12:
        print ("Tarifa $50")
    elif 13<= dato1 <=17:
        print ("Tarida $80")
    elif 18<= dato1 <=120:
        print ("Tarifa $120")
    else:
        print ("\n...EL DATO INGRESADO NO HA SIDO VALIDO...")
