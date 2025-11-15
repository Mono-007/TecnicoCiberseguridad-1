# 1. Muestra los números del 1 al 10
print("\n--- 1. Mostrar del 1 al 10 (While) ---")
i = 1
while i <= 10:
    print(i)
    i += 1 # Incrementamos el contador

# ------------------------------------------------------------------

# 2. Suma de números hasta que se ingrese 0
print("\n--- 2. Suma hasta Cero (While) ---")
suma_total = 0
numero = -1 # Inicializamos con un valor diferente de 0 para entrar al bucle

while numero != 0:
    try:
        numero = int(input("Ingresa un número para sumar (0 para terminar): "))
        suma_total += numero
    except ValueError:
        print("Entrada inválida. Ingresa un número entero.")

print(f"La suma total es: {suma_total}")

# ------------------------------------------------------------------

# 3. Adivina el número secreto
print("\n--- 3. Adivina el Número Secreto (While) ---")
numero_secreto = 7
intento = 0

while intento != numero_secreto:
    try:
        intento = int(input("Adivina el número secreto (1-10): "))
        if intento < numero_secreto:
            print("El número es mayor. Intenta de nuevo.")
        elif intento > numero_secreto:
            print("El número es menor. Intenta de nuevo.")
    except ValueError:
        print("Entrada inválida.")

print(f"¡Correcto! El número secreto era {numero_secreto}.")

# ------------------------------------------------------------------

# 4. Valida una contraseña
print("\n--- 4. Validar Contraseña (While) ---")
clave_correcta = "1234"
contrasena = ""

while contrasena != clave_correcta:
    contrasena = input("Ingresa la contraseña ('1234' para pasar): ")
    if contrasena != clave_correcta:
        print("Contraseña incorrecta. Intenta de nuevo.")

print("Acceso concedido.")

# ------------------------------------------------------------------

# 5. Contador regresivo
print("\n--- 5. Contador Regresivo (While) ---")
try:
    inicio = int(input("Ingresa un número para iniciar la cuenta regresiva: "))
    
    contador_regresivo = inicio
    while contador_regresivo >= 1:
        print(contador_regresivo)
        contador_regresivo -= 1 # Decrementamos el contador
    print("¡Despegue!")

except ValueError:
    print("Entrada inválida. Ingresa un número entero.")