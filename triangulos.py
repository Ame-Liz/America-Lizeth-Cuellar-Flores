while True:
    dato1= int (input("Ingresa dato 1 de el triangulo: "))
    dato2= int (input("Ingresa dato 2 de el triangulo: "))
    dato3= int (input("Ingresa dato 3 de el triangulo: "))

    if dato1 <= 0 or dato2 <= 0 or dato3 <= 0:
        print ("No puedes ingresar el 0 o menor a este")    

    elif dato1 == dato2 == dato3:
        print("\nLos datos ingresados coinciden con un triangulo equilatero")
    elif dato1 == dato2 or dato2 == dato3 or dato3 == dato1:
        print("\nEs isoceles pues dos datos son coinciden") 
    else:
        print("\nNingun lado coincide por lo que es Triangulo Escaleno"    
