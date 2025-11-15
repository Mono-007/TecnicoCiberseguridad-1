Proceso CargarYMostrarVector
    Dimension vector[5]
    Definir i Como Entero
	
    // Cargar los 5 números
    Para i = 1 Hasta 5 Con Paso 1
        Escribir "Ingrese un número para la posición ", i, ": "
        Leer vector[i]
    FinPara
	
    // Mostrar valores
    Escribir "Los valores ingresados son:"
    Para i = 1 Hasta 5 Con Paso 1
        Escribir vector[i]
    FinPara
FinProceso
