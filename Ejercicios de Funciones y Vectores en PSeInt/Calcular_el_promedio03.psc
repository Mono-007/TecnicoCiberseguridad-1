Funcion resultado <- Promedio(n1, n2, n3)
    resultado = (n1 + n2 + n3) / 3
FinFuncion

Proceso Principal
    Definir nota1, nota2, nota3, prom Como Real
	
    Escribir "Ingrese la primera nota: "
    Leer nota1
	
    Escribir "Ingrese la segunda nota: "
    Leer nota2
	
    Escribir "Ingrese la tercera nota: "
    Leer nota3
	
    prom = Promedio(nota1, nota2, nota3)
	
    Escribir "El promedio es: ", prom
	
    Si prom >= 70 Entonces
        Escribir "Resultado: Aprobado"
    Sino
        Escribir "Resultado: Reprobado"
    FinSi
	
FinProceso
