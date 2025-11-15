# Creación de la tupla
vulnerabilidades = ('SQL Injection', 'Cross-Site Scripting', 'Buffer Overflow', 'Denegación de Servicio')

# a) Mostrar el segundo elemento
print("Segundo elemento:", vulnerabilidades[1])

# b) Mostrar los dos últimos elementos
print("Dos últimos elementos:", vulnerabilidades[-2:])

# c) Intentar modificar un elemento
try:
    vulnerabilidades[0] = 'Inyección SQL'
except TypeError as e:
    print("Error al modificar la tupla:", e)
