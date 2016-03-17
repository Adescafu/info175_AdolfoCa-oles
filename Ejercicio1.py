def numeritos():
    x=raw_input("ingrese el primer numero: ")
    y=raw_input("ingrese el segundo numero: ")
    
    if(x>y):
        print("El mayor es: "+x)
        print("El menor es: "+y)
    
    elif(x<y):
        print("El mayor es: "+y)
    	print("El menor es: "+x)
    	
    else:
        print("Los numeros son iguales")
    	    
numeritos()