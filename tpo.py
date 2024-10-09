from datetime import date, datetime

# Crear una fecha de nacimiento
# fecha_nacimiento = date(1994, 5, 22)

# Crear una fecha y hora de declaración
# fecha_declaracion = datetime(2024, 10, 6, 14, 30)
 
# Mostrar las fechas en diferentes formatos
# print(f"Fecha de nacimiento: {fecha_nacimiento}")
# print(f"Fecha de declaración: {fecha_declaracion.strftime('%d/%m/%Y %H:%M')}")



dni = None
apellido = None
nombre = None
edad = None
fechaDeNacimiento = None
profesion = None
monto = None
fechaDeclarar = None
origen = None

class Persona:
    def __init__(self, dni, apellido, nombre, edad, fechaDeNacimiento, profesion, monto, fechaDeclarar, origen):
        self.dni = dni
        self.apellido = apellido
        self.nombre = nombre
        self.edad = edad
        self.fechaDeNacimiento = fechaDeNacimiento
        self.profesion = profesion
        self.monto= monto
        self.fechaDeclarar = fechaDeclarar
        self.origen = origen

    def mostrar_info(self):
        print(f"DNI: {self.dni}, Apellido: {self.apellido}, Nombre: {self.nombre}, Edad: {self.edad}, Fecha de nacimiento: {self.fechaDeNacimiento}, Profesión: {self.profesion}, Monto declarado: {self.monto}, Fecha de declaración: {self.fechaDeclarar}, Origen de los fondos: {self.origen}")

lista_personas = []

def registrardatos():
    dni = input("Ingrese su DNI: ")
    apellido = input("Ingrese su apellido: ")
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    fechaDeNacimiento = input("Ingrese su fecha de nacimiento (DD/MM/YY): ")
    fechaDeNacimiento = datetime.strptime(fechaDeNacimiento, "%d/%m/%Y")
    profesion = input("Indique su profesión: ")
    monto = int(input("Indique el monto a declarar (en dolares): $"))
    fechaDeclarar = input("Indique la fecha en la cual está declarando sus fondos (DD/MM/YY): ")
    fechaDeclarar = datetime.strptime(fechaDeclarar, "%d/%m/%Y")
    origen = input("Indique el origen de sus fondos: ")

    return dni, apellido, nombre, edad, fechaDeNacimiento, profesion, monto, fechaDeclarar, origen


while True:
    # Llamar a la función y obtener los datos
    dni, apellido, nombre, edad, fechaDeNacimiento, profesion, monto, fechaDeclarar, origen = registrardatos()

    # Crear un objeto Persona y agregarlo a la lista
    persona = Persona(dni, apellido, nombre, edad, fechaDeNacimiento, profesion, monto, fechaDeclarar, origen)
    persona.mostrar_info()
    
    valid1 = input("¿Desea declarar estos datos? (si/no): ").lower()
    if valid1 == "si":
        lista_personas.append(persona)
        respuesta1 = input("Piensa invertir el dinero en alguna colocacion emitida por el Ministerio de Economia? (si/no): ").lower()
        if respuesta1 == "si":
            continue
        elif respuesta1 == "no":
            respuesta2 = input("Hasta cuando piensa mantener el dinero en el sistema financiero?: (DD/MM/YY) ")
            respuesta2 = datetime.strptime(respuesta2, "%d/%m/%Y")
            if respuesta2 > datetime(2025, 12, 31):
                print("Usted no puede realizar el blanqueo de fondos")
            else:
                fin = input("¿Quiere realizar otra declaración? (Ingrese 'si' para continuar o 'no' para finalizar): ").lower()
                if fin == "no":
                    break
                elif fin == "si":
                    continue
    elif valid1 == "no":
        continue  # Vuelve a solicitar los datos para corregirlos

    fin = input("¿Quiere realizar otra declaración? (Ingrese 'si' para continuar o 'no' para finalizar): ").lower()
    if fin == "no":
        break



print("Personas registradas:")
for persona in lista_personas:
    persona.mostrar_info()
