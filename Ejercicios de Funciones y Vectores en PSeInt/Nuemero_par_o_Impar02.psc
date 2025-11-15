Funcion resultado <- EsPar(num)
    Si num % 2 = 0 Entonces
        resultado = Verdadero
    Sino
        resultado = Falso
    FinSi
FinFuncion

Proceso Principal
    Definir numero Como Entero
	
    Escribir "Ingrese un número: "
    Leer numero
	
    Si EsPar(numero) Entonces
        Escribir "El número es PAR."
    Sino
        Escribir "El número es IMPAR."
    FinSi
	
FinProceso