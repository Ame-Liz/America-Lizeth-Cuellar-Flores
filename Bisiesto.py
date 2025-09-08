año = int(input("Ingresa el año quieres saber si es o no bisiesto: "))
if año %4==0 and año%100!=0:
        print("Año... ",año, " SI sera bisiesto")
if año %400 ==0:
        print("Año... ",año, " SI sera bisiesto")
else:
        print("El año ", año," no sera bisiesto")
