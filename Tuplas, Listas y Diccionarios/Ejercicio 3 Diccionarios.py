# Creación del diccionario
dispositivo_red = {
    'IP': '192.168.1.10',
    'Hostname': 'Firewall-Corp',
    'Estado': 'Activo'
}

# a) Mostrar 'Hostname'
print("Hostname:", dispositivo_red['Hostname'])

# b) Agregar nueva clave 'Ubicación'
dispositivo_red['Ubicación'] = 'Centro de Datos'

# c) Cambiar valor de 'Estado'
dispositivo_red['Estado'] = 'Inactivo'

# d) Mostrar diccionario actualizado
print("Diccionario actualizado:", dispositivo_red)
