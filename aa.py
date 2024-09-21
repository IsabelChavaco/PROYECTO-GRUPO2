import datetime
import re

clientes = [
    {"nombre": "Mateo", "apellido": "Cardenas", "email": "mateo12@hotmail.com", "telefono": "3124567890", "documento": "123456789"},
    {"nombre": "Natalia", "apellido": "Lopez", "email": "naty@gmail.com", "telefono": "3204328899", "documento": "987654321"}
]
paquetes = []
reservas = []

# Menú para cada tipo de usuario
menu_cliente = {
    "1": "Realizar reserva",
    "2": "Mostrar reservas",
    "3": "Mostrar paquetes",
    "4": "Editar reserva",
    "0": "Salir"
}

# Contraseña administrador: 12345
menu_administrador = {
    "1": "Registrar cliente",
    "2": "Crear paquete de viaje",
    "3": "Cancelar reserva",
    "4": "Mostrar reservas de un cliente",
    "5": "Mostrar clientes",
    "6": "Eliminar paquete",
    "7": "Modificar paquete",
    "8": "Editar cliente",
    "0": "Salir"
}

# Paquetes de viaje predeterminados
paquetes_preset = [
    {"nombre": "Escapada a la Playa", "descripcion": "Disfruta de un fin de semana en la playa con todo incluido.", "fecha_salida": "01-10-2024", "fecha_llegada": "04-10-2024", "precio": 300.0},
    {"nombre": "Aventura en la Montaña", "descripcion": "Un emocionante viaje de senderismo y campamento.", "fecha_salida": "10-11-2024", "fecha_llegada": "15-11-2024", "precio": 450.0},
    {"nombre": "Tour Cultural", "descripcion": "Descubre la historia y cultura de nuestra ciudad.", "fecha_salida": "20-09-2024", "fecha_llegada": "22-09-2024", "precio": 200.0},
    {"nombre": "Safari en África", "descripcion": "Un increíble safari para ver la fauna salvaje en su hábitat natural.", "fecha_salida": "05-12-2024", "fecha_llegada": "15-12-2024", "precio": 1200.0},
    {"nombre": "Crucero por el Caribe", "descripcion": "Relájate en un crucero de lujo por las islas del Caribe.", "fecha_salida": "15-01-2025", "fecha_llegada": "25-01-2025", "precio": 1500.0},
    {"nombre": "Escapada a París", "descripcion": "Descubre la ciudad del amor con un paquete romántico.", "fecha_salida": "10-02-2025", "fecha_llegada": "15-02-2025", "precio": 800.0},
    {"nombre": "Exploración en Machu Picchu", "descripcion": "Una aventura inolvidable en el corazón de los Andes.", "fecha_salida": "01-03-2025", "fecha_llegada": "10-03-2025", "precio": 950.0},
    {"nombre": "Tour Gastronómico en Italia", "descripcion": "Degusta los mejores platillos en un recorrido por Italia.", "fecha_salida": "15-04-2025", "fecha_llegada": "30-04-2025", "precio": 1200.0},
    {"nombre": "Aventura en Nueva Zelanda", "descripcion": "Explora los paisajes únicos de Nueva Zelanda con actividades al aire libre.", "fecha_salida": "01-05-2025", "fecha_llegada": "15-05-2025", "precio": 1100.0},
    {"nombre": "Escapada a las Montañas Rocosas", "descripcion": "Relájate en un hermoso resort de montaña.", "fecha_salida": "10-06-2025", "fecha_llegada": "20-06-2025", "precio": 700.0}
]

paquetes.extend(paquetes_preset)

# Validaciones de clientes
def validar_nombre(nombre):
    patron = re.compile(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')
    return bool(patron.fullmatch(nombre))

def validar_email(email):
    patron1 = re.compile(r'^[a-zA-Z0-9.%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    return bool(patron1.fullmatch(email))

def validar_telefono(telefono):
    numero = re.compile(r'^\d{10}$')
    return bool(numero.fullmatch(telefono))

def validar_documento(documento):
    numero = re.compile(r'^\d+$')
    return bool(numero.fullmatch(documento))

def registrar_cliente():
    while True:
        nombre = input("Ingrese nombre del cliente: ")
        if validar_nombre(nombre):
            break
        else:
            print("Nombre inválido, NO puede contener números. Digite nuevamente.")
    
    while True:
        apellido = input("Ingrese apellido del cliente: ")
        if validar_nombre(apellido):
            break
        else:
            print("Apellido inválido, NO se admiten números. Digite nuevamente.")

    while True:
        email = input("Ingrese email del cliente: ")
        if validar_email(email):
            break
        else:
            print("Email NO Válido. Digíta nuevamente")

    while True:
        telefono = input("Ingrese teléfono del cliente: ")
        if validar_telefono(telefono):
            break
        else:
            print("Teléfono NO Válido. Deben ser 10 dígitos")

    while True:
        documento = input("Ingrese documento de identidad del cliente (solo números): ")
        if validar_documento(documento):
            break
        else:
            print("Documento inválido, debe contener solo números. Digite nuevamente.")

    clientes.append({"nombre": nombre, "apellido": apellido, "email": email, "telefono": telefono, "documento": documento})
    print("Cliente registrado con éxito.")

# Crear paquetes
def crear_paquete():
    nombre = input("Ingrese nombre del paquete: ")
    descripcion = input("Ingrese descripcion del paquete: ")
    fecha_salida = input("Ingrese fecha de salida del paquete (dd-mm-aaaa): ")
    fecha_llegada = input("Ingrese fecha de llegada del paquete (dd-mm-aaaa): ")
    
    while True:
        try:
            precio = float(input("Ingrese precio del paquete: "))
            break
        except ValueError:
            print("Error: El precio debe ser un número.")

    paquetes.append({"nombre": nombre, "descripcion": descripcion, "fecha_salida": fecha_salida, "fecha_llegada": fecha_llegada, "precio": precio})
    print("Paquete creado con éxito.")

# Verificar si el cliente está registrado
def cliente_registrado(nombre_cliente, apellido_cliente):
    for cliente in clientes:
        if cliente["nombre"] == nombre_cliente and cliente["apellido"] == apellido_cliente:
            return True
    return False

# Para que el cliente realice una reserva
def realizar_reserva():
    nombre_cliente = input("Ingrese nombre del cliente: ")
    apellido_cliente = input("Ingrese apellido del cliente: ")

    if not cliente_registrado(nombre_cliente, apellido_cliente):
        print("Cliente no registrado. Por favor registrese antes de realizar una reserva.")
        return

    print("Paquetes disponibles para reservar:")
    mostrar_paquetes_numerados()

    while True:
        try:
            seleccion = int(input("Ingrese el número del paquete que desea reservar: "))
            if 1 <= seleccion <= len(paquetes):
                nombre_paquete = paquetes[seleccion - 1]["nombre"]
                break
            else:
                print("Selección inválida. Intente nuevamente.")
        except ValueError:
            print("Error: Debe ingresar un número.")

    for cliente in clientes:
        if cliente["nombre"] == nombre_cliente and cliente["apellido"] == apellido_cliente:
            for paquete in paquetes:
                if paquete["nombre"] == nombre_paquete:
                    reservas.append({"cliente": cliente, "paquete": paquete})
                    print("Reserva realizada con éxito.")
                    return
    print("Paquete no encontrado.")

# Editar reserva
def editar_reserva():
    nombre_cliente = input("Ingrese nombre del cliente: ")
    apellido_cliente = input("Ingrese apellido del cliente: ")

    if not cliente_registrado(nombre_cliente, apellido_cliente):
        print("Cliente no registrado. No puede editar reservas.")
        return

    mostrar_reservas_cliente(nombre_cliente, apellido_cliente)

    while True:
        try:
            seleccion = int(input("Ingrese el número de la reserva que desea editar: "))
            if 1 <= seleccion <= len(reservas):
                reserva_actual = reservas[seleccion - 1]
                print("Paquetes disponibles para seleccionar un nuevo paquete:")
                mostrar_paquetes_numerados()

                while True:
                    try:
                        nuevo_seleccion = int(input("Ingrese el número del nuevo paquete: "))
                        if 1 <= nuevo_seleccion <= len(paquetes):
                            nuevo_paquete = paquetes[nuevo_seleccion - 1]
                            reserva_actual["paquete"] = nuevo_paquete
                            print("Reserva editada con éxito.")
                            return
                        else:
                            print("Selección inválida. Intente nuevamente.")
                    except ValueError:
                        print("Error: Debe ingresar un número.")
                return
            else:
                print("Selección inválida. Intente nuevamente.")
        except ValueError:
            print("Error: Debe ingresar un número.")

# Mostrar reservas de un cliente
def mostrar_reservas_cliente(nombre_cliente, apellido_cliente):
    print(f"Reservas de {nombre_cliente} {apellido_cliente}:")
    
    reservas_encontradas = False
    for index, reserva in enumerate(reservas, start=1):
        if reserva["cliente"]["nombre"] == nombre_cliente and reserva["cliente"]["apellido"] == apellido_cliente:
            print(f"{index}. Paquete: {reserva['paquete']['nombre']}")
            print(f"   Fecha de salida: {reserva['paquete']['fecha_salida']}")
            print(f"   Fecha de llegada: {reserva['paquete']['fecha_llegada']}")
            print(f"   Precio: {reserva['paquete']['precio']}")
            print("---------")
            reservas_encontradas = True
            
    if not reservas_encontradas:
        print("No se encontraron reservas para este cliente.")

# Mostrar paquetes numerados
def mostrar_paquetes_numerados():
    print("Paquetes disponibles:")
    for index, paquete in enumerate(paquetes, start=1):
        print(f"{index}. {paquete['nombre']} - {paquete['descripcion']} - Precio: {paquete['precio']}")

# Mostrar clientes
def mostrar_clientes():
    print("Clientes registrados:")
    for cliente in clientes:
        print(f"Nombre: {cliente['nombre']} {cliente['apellido']} - Email: {cliente['email']} - Teléfono: {cliente['telefono']} - Documento: {cliente['documento']}")

# Modificar paquete
def modificar_paquete():
    mostrar_paquetes_numerados()
    while True:
        try:
            seleccion = int(input("Ingrese el número del paquete que desea modificar: "))
            if 1 <= seleccion <= len(paquetes):
                paquete = paquetes[seleccion - 1]
                print(f"Modificando paquete: {paquete['nombre']}")
                
                # Aquí puedes modificar los campos que desees
                nombre = input("Ingrese nuevo nombre del paquete (deje vacío para no cambiar): ")
                if nombre:
                    paquete['nombre'] = nombre

                descripcion = input("Ingrese nueva descripcion del paquete (deje vacío para no cambiar): ")
                if descripcion:
                    paquete['descripcion'] = descripcion

                fecha_salida = input("Ingrese nueva fecha de salida del paquete (dd-mm-aaaa, deje vacío para no cambiar): ")
                if fecha_salida:
                    paquete['fecha_salida'] = fecha_salida

                fecha_llegada = input("Ingrese nueva fecha de llegada del paquete (dd-mm-aaaa, deje vacío para no cambiar): ")
                if fecha_llegada:
                    paquete['fecha_llegada'] = fecha_llegada

                while True:
                    try:
                        precio = input("Ingrese nuevo precio del paquete (deje vacío para no cambiar): ")
                        if precio:
                            paquete['precio'] = float(precio)
                        break
                    except ValueError:
                        print("Error: El precio debe ser un número.")

                print("Paquete modificado con éxito.")
                return
            else:
                print("Selección inválida. Intente nuevamente.")
        except ValueError:
            print("Error: Debe ingresar un número.")

# Menú principal
def menu_principal():
    while True:
        print("Bienvenido al sistema de reservas de viajes")
        print("Seleccione una opción:")
        print("1. Cliente")
        print("2. Administrador")
        print("0. Salir")
        
        opcion = input("Opción: ")

        if opcion == "1":
            while True:
                print("\nMenú Cliente:")
                for key, value in menu_cliente.items():
                    print(f"{key}. {value}")
                opcion_cliente = input("Seleccione una opción: ")

                if opcion_cliente == "1":
                    realizar_reserva()
                elif opcion_cliente == "2":
                    nombre_cliente = input("Ingrese nombre del cliente: ")
                    apellido_cliente = input("Ingrese apellido del cliente: ")
                    mostrar_reservas_cliente(nombre_cliente, apellido_cliente)
                elif opcion_cliente == "3":
                    mostrar_paquetes_numerados()
                elif opcion_cliente == "4":
                    editar_reserva()
                elif opcion_cliente == "0":
                    print("Saliendo del menú cliente...")
                    break
                else:
                    print("Opción inválida. Intente nuevamente.")

        elif opcion == "2":
            contrasena = input("Ingrese contraseña de administrador: ")
            if contrasena == "12345":
                while True:
                    print("\nMenú Administrador:")
                    for key, value in menu_administrador.items():
                        print(f"{key}. {value}")
                    opcion_admin = input("Seleccione una opción: ")

                    if opcion_admin == "1":
                        registrar_cliente()
                    elif opcion_admin == "2":
                        crear_paquete()
                    elif opcion_admin == "3":
                        # Aquí va la lógica para cancelar reserva
                        pass
                    elif opcion_admin == "4":
                        nombre_cliente = input("Ingrese nombre del cliente: ")
                        apellido_cliente = input("Ingrese apellido del cliente: ")
                        mostrar_reservas_cliente(nombre_cliente, apellido_cliente)
                    elif opcion_admin == "5":
                        mostrar_clientes()
                    elif opcion_admin == "6":
                        # Aquí va la lógica para eliminar paquete
                        pass
                    elif opcion_admin == "7":
                        modificar_paquete()
                    elif opcion_admin == "8":
                        # Aquí va la lógica para editar cliente
                        pass
                    elif opcion_admin == "0":
                        print("Saliendo del menú administrador...")
                        break
                    else:
                        print("Opción inválida. Intente nuevamente.")
            else:
                print("Contraseña incorrecta.")

        elif opcion == "0":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

menu_principal()
