Proceso PromedioCalificaciones
    Dimension notas[5]
    Definir i Como Entero
    Definir suma, promedio Como Real
	
    suma = 0
	
    // Cargar calificaciones
    Para i = 1 Hasta 5 Con Paso 1
        Escribir "Ingrese la calificación del estudiante ", i, ": "
        Leer notas[i]
    FinPara
	
    // Sumar calificaciones
    Para i = 1 Hasta 5 Con Paso 1
        suma = suma + notas[i]
    FinPara
	
    // Calcular promedio
    promedio = suma / 5
	
    Escribir "El promedio general del grupo es: ", promedio
	
FinProceso

