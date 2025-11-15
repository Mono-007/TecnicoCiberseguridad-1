Proceso SumarVector
    Dimension vector[10]
    Definir i, suma Como Entero
	
    suma = 0
	
    // Cargar los 10 números
    Para i = 1 Hasta 10 Con Paso 1
        Escribir "Ingrese un número para la posición ", i, ": "
        Leer vector[i]
    FinPara
	
    // Sumar los elementos
    Para i = 1 Hasta 10 Con Paso 1
        suma = suma + vector[i]
    FinPara
	
    Escribir "La suma total de los elementos es: ", suma
	
FinProceso
