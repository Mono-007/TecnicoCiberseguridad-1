import re 

# 1. Vectores (Listas)
usuarios = []           
contraseñas = []        
fuerza_contraseñas = [] 

# 2. Funciones
# --- Función 1: VerificarContraseña
def VerificarContraseña(password: str) -> str:
    """Verifica la fuerza de una contraseña basada en la longitud, mayúsculas, minúsculas, números y símbolos."""
    
    # Tipo de dato: Lógico (Booleanos)
    es_larga = len(password) >= 12
    tiene_mayuscula = bool(re.search(r'[A-Z]', password))
    tiene_minuscula = bool(re.search(r'[a-z]', password))
    tiene_numero = bool(re.search(r'[0-9]', password))
    tiene_simbolo = bool(re.search(r'[^A-Za-z0-9]', password)) 

    # Condicionales: Lógica de clasificación
    if es_larga and tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_simbolo:
        return "Fuerte"
    elif (tiene_mayuscula or tiene_minuscula) and tiene_numero and len(password) >= 8:
        return "Media"
    else:
        return "Débil"

# --- Función 2: RegistrarUsuario
def RegistrarUsuario(nuevo_usuario: str, nueva_contraseña: str) -> bool:
    """Registra un nuevo usuario y su contraseña si el usuario no existe."""
    
    # Bucle: Comprueba la existencia del usuario en la lista
    if nuevo_usuario in usuarios:
        print(f"\nError: El usuario '{nuevo_usuario}' ya existe.")
        return False
    
    # Tipo de dato: Cadena
    fuerza = VerificarContraseña(nueva_contraseña)
    
    # Almacenamiento en los vectores (listas)
    usuarios.append(nuevo_usuario)
    contraseñas.append(nueva_contraseña)
    fuerza_contraseñas.append(fuerza)
    
    print(f"\nUsuario '{nuevo_usuario}' registrado con éxito. Fuerza: {fuerza}")
    return True

# --- Función 3: GenerarAlertas
def GenerarAlertas():
    """Genera una alerta para todos los usuarios con contraseñas clasificadas como 'Débiles'."""
    print("\n--- ALERTA DE SEGURIDAD ---")
    
    alerta_encontrada = False
    
    # Bucle: Iterar sobre la lista de fuerza_contraseñas para identificar débiles
    for i, fuerza in enumerate(fuerza_contraseñas):
        # Condicional: Identificar contraseñas débiles
        if fuerza == "Débil":
            print(f"Alerta para usuario **{usuarios[i]}**: Su contraseña es **DÉBIL**!")
            print("Recomendación: Cambie su contraseña a una que cumpla los requisitos de fuerza (12+ caracteres, mayúsculas, minúsculas, números y símbolos).")
            alerta_encontrada = True
            
    if not alerta_encontrada:
        print("Todas las contraseñas son de fuerza Media o Fuerte.")
    print("---------------------------")


# 3. Programa Principal (Demo)
if __name__ == "__main__":
    
    print("--- INICIO DEL GESTOR DE CONTRASEÑAS ---")
    
    # Registro de usuarios de prueba
    RegistrarUsuario("admin", "123456") 
    RegistrarUsuario("usuario_media", "PasoSecreto8") 
    RegistrarUsuario("juangarcia", "PasswordSegura!2025$") 
    RegistrarUsuario("otro_usuario", "MiClave2") 
    
    # Intento de registro duplicado
    RegistrarUsuario("admin", "NuevaClave")

    # Mostrar el estado actual
    print("\n## Estado del Gestor ##")
    # Bucle: Imprimir todos los usuarios y su fuerza
    for i in range(len(usuarios)):
        print(f"Usuario: {usuarios[i]} | Contraseña (Oculta): {'*' * len(contraseñas[i])} | Fuerza: {fuerza_contraseñas[i]}")
        
    # Generar alertas de seguridad
    GenerarAlertas()
    
    print("\n--- FIN DEL GESTOR DE CONTRASEÑAS ---")