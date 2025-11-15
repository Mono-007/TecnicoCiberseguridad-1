# 1. Muestra la tabla de multiplicar
print("\n--- 1. Tabla de Multiplicar (For) ---")
try:
    num_tabla = int(input("¿De qué número quieres la tabla de multiplicar?: "))
    
    # Recorremos del 1 al 10 (range(1, 11))
    for i in range(1, 11): 
        resultado = num_tabla * i
        print(f"{num_tabla} x {i} = {resultado}")
except ValueError:
    print("Entrada inválida.")

# ------------------------------------------------------------------

# 2. Pide 10 números y calcula la suma total
print("\n--- 2. Suma de 10 Números (For) ---")
suma_10 = 0
cantidad_numeros = 10

# range(cantidad_numeros) va de 0 a 9, 10 veces
for i in range(cantidad_numeros):
    try:
        num_pedido = float(input(f"Ingresa el número #{i + 1}: "))
        suma_10 += num_pedido
    except ValueError:
        print("Entrada inválida. Saltando este número.")

print(f"La suma total de los 10 números es: {suma_10}")

# ------------------------------------------------------------------

# 3. Calcula el factorial de un número
print("\n--- 3. Calcular Factorial (For) ---")
try:
    num_factorial = int(input("Ingresa un número para calcular su factorial: "))
    
    if num_factorial < 0:
        print("El factorial no está definido para números negativos.")
    elif num_factorial == 0:
        factorial = 1
    else:
        factorial = 1
        # Recorremos desde 1 hasta el número ingresado
        for i in range(1, num_factorial + 1):
            factorial *= i # Equivalente a factorial = factorial * i

    print(f"El factorial de {num_factorial} es: {factorial}")

except ValueError:
    print("Entrada inválida. Ingresa un número entero.")

# ------------------------------------------------------------------

# 4. Muestra todos los números pares entre 1 y 50
print("\n--- 4. Pares entre 1 y 50 (For) ---")
print("Números pares:")

# Usamos range con un tercer argumento, el 'paso'
# Empezamos en 2 y vamos de 2 en 2 hasta 50 (no incluye 51)
for par in range(2, 51, 2): 
    print(par, end=" ")
print() # Salto de línea al final

# ------------------------------------------------------------------

# 5. Pide 5 notas, calcula la suma y el promedio final
print("\n--- 5. Promedio de 5 Notas (For) ---")
suma_notas = 0
num_notas = 5

for i in range(num_notas):
    while True: # Bucle para asegurar una entrada válida
        try:
            nota_actual = float(input(f"Ingresa la nota #{i + 1}: "))
            suma_notas += nota_actual
            break # Sale del bucle while si la entrada es válida
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")

promedio_final = suma_notas / num_notas
print(f"\nLa suma de las notas es: {suma_notas:.2f}")
print(f"El promedio final es: {promedio_final:.2f}")