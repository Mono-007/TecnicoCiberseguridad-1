Proceso BuscarNumeroEnVector
    Dimension vector[8]
    Definir i, numBuscado Como Entero
    Definir encontrado Como Logico
	
    encontrado = Falso
	
    // Cargar los 8 números
    Para i = 1 Hasta 8 Con Paso 1
        Escribir "Ingrese un número para la posición ", i, ": "
        Leer vector[i]
    FinPara
	
    // Pedir número a buscar
    Escribir "Ingrese el número que desea buscar: "
    Leer numBuscado
	
    // Búsqueda lineal
    Para i = 1 Hasta 8 Con Paso 1
        Si vector[i] = numBuscado Entonces
            encontrado = Verdadero
        FinSi
    FinPara
	
    // Resultado
    Si encontrado Entonces
        Escribir "El número SI se encuentra en el vector."
    Sino
        Escribir "El número NO se encuentra en el vector."
    FinSi
	
FinProceso
