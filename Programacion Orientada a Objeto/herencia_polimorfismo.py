# Ejercicios de Herencia y Polimorfismo en Python

# 1. Animal, Perro, Gato
class Animal:
    def hablar(self):
        return "El animal hace un sonido"

class Perro(Animal):
    def hablar(self):
        return "Guau!"

class Gato(Animal):
    def hablar(self):
        return "Miau!"


# 2. Empleado, Gerente, Técnico
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def calcular_bono(self):
        return 0

class Gerente(Empleado):
    def calcular_bono(self):
        return self.salario * 0.20

class Tecnico(Empleado):
    def calcular_bono(self):
        return self.salario * 0.10


# 3. Figura, Círculo, Cuadrado
import math

class Figura:
    def area(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2


# 4. Vehiculo, Carro, Bicicleta
class Vehiculo:
    def mover(self):
        return "El vehículo se mueve"

class Carro(Vehiculo):
    def mover(self):
        return "El carro está avanzando"

class Bicicleta(Vehiculo):
    def mover(self):
        return "La bicicleta está pedaleando"


# 5. Dispositivo, Laptop, Teléfono
class Dispositivo:
    def encender(self):
        return "Encendiendo dispositivo"

class Laptop(Dispositivo):
    def encender(self):
        return "Laptop encendida"

class Telefono(Dispositivo):
    def encender(self):
        return "Teléfono encendido"
