Algoritmo  verificarContrase�a
	
	Definir contrase�aCorrecta Como Cadena
	Definir  contrase�aIngresada Como Cadena
	Definir Intentos Como Entero
	Definir accesoPermitido Como Logico
	
	//contase�a Correcta
	contrase�aCorrecta = "1234"
	Intentos <- 0
	
	Mientras intentos < 3 y accesoPermitido = falso Hacer
		Escribir  "ingrese su contrase�a: "
		Leer  contrase�aIngresada
		
		Si contrase�aIngresada = contrase�aCorrecta Entonces
			accesoPermitido = Verdadero
		SiNo
			intentos <- intentos + 1
			Escribir  "contrase�a incorrecta. Intentos", intentos, "de 3."
		Finsi
	FinMientras
	si accesoPermitido = falsp Entonces
		Escribir  "cuenta suspendida temporalmente. Ha excedido el numero de intentos"
	SiNo
		Escribir  "Acceso permitido al sistema"
	FinSi
FinAlgoritmo
	