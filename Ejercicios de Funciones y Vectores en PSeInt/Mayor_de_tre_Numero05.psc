Funcion resultado <- MayorNumero(a, b, c)
    Si a >= b Y a >= c Entonces
        resultado = a
    Sino
        Si b >= a Y b >= c Entonces
            resultado = b
        Sino
            resultado = c
        FinSi
    FinSi
FinFuncion


Proceso Principal
    Definir n1, n2, n3, mayor Como Real
	
    Escribir "Ingrese el primer número: "
    Leer n1
	
    Escribir "Ingrese el segundo número: "
    Leer n2
	
    Escribir "Ingrese el tercer número: "
    Leer n3
	
    mayor = MayorNumero(n1, n2, n3)
	
    Escribir "El número mayor es: ", mayor
	
FinProceso

