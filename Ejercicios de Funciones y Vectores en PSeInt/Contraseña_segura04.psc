Funcion resultado <- ValidarPassword(pass)
    Si Longitud(pass) > 8 Entonces
        resultado = Verdadero
    Sino
        resultado = Falso
    FinSi
FinFuncion

Proceso Principal
    Definir password Como Cadena
	
    Escribir "Ingrese una contraseña: "
    Leer password
	
    Si ValidarPassword(password) Entonces
        Escribir "La contraseña es VÁLIDA."
    Sino
        Escribir "La contraseña es NO válida (debe tener más de 8 caracteres)."
    FinSi
	
FinProceso
