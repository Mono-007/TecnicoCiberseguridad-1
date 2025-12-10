class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")


class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura


class Coche:
    def __init__(self, marca, velocidad=0):
        self.marca = marca
        self.velocidad = velocidad

    def aumentar_velocidad(self, incremento):
        self.velocidad += incremento


class CuentaBancaria:
    def __init__(self, titular, balance=0):
        self.titular = titular
        self.balance = balance

    def depositar(self, cantidad):
        self.balance += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.balance:
            self.balance -= cantidad
        else:
            print("Fondos insuficientes")


class Estudiante:
    def __init__(self, nombre, calificaciones):
        self.nombre = nombre
        self.calificaciones = calificaciones

    def calcular_promedio(self):
        return sum(self.calificaciones) / len(self.calificaciones)


def menu():
    while True:
        print("\n========= MENÚ PRINCIPAL =========")
        print("1. Crear y mostrar Usuario")
        print("2. Calcular área de un Rectángulo")
        print("3. Aumentar velocidad de un Coche")
        print("4. Operaciones de Cuenta Bancaria")
        print("5. Calcular promedio de un Estudiante")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            u = Usuario(nombre, edad)
            u.mostrar_datos()

        elif opcion == "2":
            base = float(input("Base: "))
            altura = float(input("Altura: "))
            r = Rectangulo(base, altura)
            print("Área del rectángulo:", r.calcular_area())

        elif opcion == "3":
            marca = input("Marca del coche: ")
            c = Coche(marca)
            inc = int(input("¿Cuánto aumentar la velocidad?: "))
            c.aumentar_velocidad(inc)
            print("Nueva velocidad:", c.velocidad)

        elif opcion == "4":
            titular = input("Titular: ")
            cuenta = CuentaBancaria(titular, 0)

            while True:
                print("\n--- Cuenta Bancaria ---")
                print("1. Depositar")
                print("2. Retirar")
                print("3. Ver balance")
                print("4. Volver al menú principal")

                op = input("Opción: ")

                if op == "1":
                    cantidad = float(input("Cantidad a depositar: "))
                    cuenta.depositar(cantidad)

                elif op == "2":
                    cantidad = float(input("Cantidad a retirar: "))
                    cuenta.retirar(cantidad)

                elif op == "3":
                    print("Balance actual:", cuenta.balance)

                elif op == "4":
                    break

        elif opcion == "5":
            nombre = input("Nombre del estudiante: ")
            notas = input("Ingresa las calificaciones separadas por coma: ")
            lista_notas = [float(n) for n in notas.split(",")]
            e = Estudiante(nombre, lista_notas)
            print("Promedio:", e.calcular_promedio())

        elif opcion == "6":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intenta de nuevo.")


menu()
