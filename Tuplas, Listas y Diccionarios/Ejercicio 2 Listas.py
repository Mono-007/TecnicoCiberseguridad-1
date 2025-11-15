# Creación de la lista
puertos_abiertos = [22, 80, 443, 8080]

# a) Agregar puerto 21
puertos_abiertos.append(21)

# b) Eliminar puerto 8080
puertos_abiertos.remove(8080)

# c) Mostrar la lista ordenada
print("Lista ordenada:", sorted(puertos_abiertos))
