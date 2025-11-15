# 1. Mayor o menor de edad
print("\n--- 1. Mayor o Menor de Edad ---")
edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# ------------------------------------------------------------------

# 2. Positivo, negativo o cero
print("\n--- 2. Positivo, Negativo o Cero ---")
num = float(input("Ingresa un número: "))

if num > 0:
    print("El número es positivo.")
elif num < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")

# ------------------------------------------------------------------

# 3. Par o impar
print("\n--- 3. Par o Impar ---")
num_entero = int(input("Ingresa un número entero: "))

# El operador % (módulo) da el residuo de la división. Si es 0, es par.
if num_entero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

# ------------------------------------------------------------------

# 4. Clasificación de notas
print("\n--- 4. Clasificación de Notas ---")
nota = int(input("Ingresa una nota (0-100): "))

if nota >= 90:
    print("Aprobado con A")
elif nota >= 70:
    print("Aprobado")
else:
    print("Reprobado")

# ------------------------------------------------------------------

# 5. Descuento en compra
print("\n--- 5. Descuento en Compra ---")
monto_compra = float(input("Ingresa el monto de la compra: "))

if monto_compra > 500:
    descuento = monto_compra * 0.10
    total = monto_compra - descuento
    print(f"¡Tienes un 10% de descuento! Descuento: {descuento:.2f}")
    print(f"Total a pagar: {total:.2f}")
else:
    print(f"No aplica descuento. Total a pagar: {monto_compra:.2f}")