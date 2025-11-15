Proceso ContarNumerosPares
    Dimension vector[10]
    Definir i, contador Como Entero
	
    contador = 0
	
    // Cargar los 10 números
    Para i = 1 Hasta 10 Con Paso 1
        Escribir "Ingrese un número para la posición ", i, ": "
        Leer vector[i]
    FinPara
	
    // Contar pares
    Para i = 1 Hasta 10 Con Paso 1
        Si vector[i] % 2 = 0 Entonces
            contador = contador + 1
        FinSi
    FinPara
	
    Escribir "La cantidad de números pares es: ", contador
	
Fin Proceso

