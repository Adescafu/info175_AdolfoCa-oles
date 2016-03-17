def lineas():
	cadena=input("Ingrese una cadena de caracteres: ")
	linea=""
	while(cadena!=""):
		linea=linea+cadena+"\n" 
		cadena=input("Ingrese una cadena de caracteres: ")
	print(linea.upper())
lineas()