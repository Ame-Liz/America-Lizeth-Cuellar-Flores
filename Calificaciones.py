dato1= int(input("Ingresa un calificacion (0-100): "))

if 90<= dato1 <=100:
    print ("Clasificacion A")
elif 80<= dato1 <=89:
    print ("Clasificacion B")
elif 70<= dato1 <=79:
    print ("Clasificacion C")
elif 60<= dato1 <=69:
    print ("Clasificacion D")
elif 0<= dato1 <=59:
    print ("Clasificacion F")
else:
    print ("\n...EL DATO INGRESADO NO HA SIDO VALIDO...")
