import datetime
import re

clientes = [{"nombre": "Mateo", "apellido": "Cardenas", "email": "mateo12@hotmail.com", "telefono": "3124567890", "documento": "123456789"},
            {"nombre": "Natalia", "apellido": "Lopez", "email": "naty@gmail.com", "telefono": "3204328899", "documento": "987654321"}]
paquetes = []
reservas = []

menu = {
    "1": "Registrar cliente",
    "2": "Crear paquete de viaje",
    "3": "Realizar reserva",
    "4": "Cancelar reserva",
    "5": "Mostrar reservas",
    "6": "Mostrar reservas de un cliente",
    "7": "Mostrar clientes",
    "8": "Mostrar paquetes",
    "9": "Eliminar paquete",
    "10": "Modificar paquete",
    "0": "Salir"
}

# Paquetes de viaje predeterminados
paquetes_preset = [
    {
        "nombre": "Escapada a la Playa",
        "descripcion": "Disfruta de un fin de semana en la playa con todo incluido.",
        "fecha_salida": "01-10-2024",
        "fecha_llegada": "04-10-2024",
        "precio": 300.0
    },
    {
        "nombre": "Aventura en la Montaña",
        "descripcion": "Un emocionante viaje de senderismo y campamento.",
        "fecha_salida": "10-11-2024",
        "fecha_llegada": "15-11-2024",
        "precio": 450.0
    },
    {
        "nombre": "Tour Cultural",
        "descripcion": "Descubre la historia y cultura de nuestra ciudad.",
        "fecha_salida": "20-09-2024",
        "fecha_llegada": "22-09-2024",
        "precio": 200.0
    },
    {
        "nombre": "Safari en África",
        "descripcion": "Un increíble safari para ver la fauna salvaje en su hábitat natural.",
        "fecha_salida": "05-12-2024",
        "fecha_llegada": "15-12-2024",
        "precio": 1200.0
    },
    {
        "nombre": "Crucero por el Caribe",
        "descripcion": "Relájate en un crucero de lujo por las islas del Caribe.",
        "fecha_salida": "15-01-2025",
        "fecha_llegada": "25-01-2025",
        "precio": 1500.0
    },
    {
        "nombre": "Escapada a París",
        "descripcion": "Descubre la ciudad del amor con un paquete romántico.",
        "fecha_salida": "10-02-2025",
        "fecha_llegada": "15-02-2025",
        "precio": 800.0
    },
    {
        "nombre": "Exploración en Machu Picchu",
        "descripcion": "Una aventura inolvidable en el corazón de los Andes.",
        "fecha_salida": "01-03-2025",
        "fecha_llegada": "10-03-2025",
        "precio": 950.0
    },
    {
        "nombre": "Tour Gastronómico en Italia",
        "descripcion": "Degusta los mejores platillos en un recorrido por Italia.",
        "fecha_salida": "15-04-2025",
        "fecha_llegada": "30-04-2025",
        "precio": 1200.0
    },
    {
        "nombre": "Aventura en Nueva Zelanda",
        "descripcion": "Explora los paisajes únicos de Nueva Zelanda con actividades al aire libre.",
        "fecha_salida": "01-05-2025",
        "fecha_llegada": "15-05-2025",
        "precio": 1100.0
    },
    {
        "nombre": "Escapada a las Montañas Rocosas",
        "descripcion": "Relájate en un hermoso resort de montaña.",
        "fecha_salida": "10-06-2025",
        "fecha_llegada": "20-06-2025",
        "precio": 700.0
    }
]

paquetes.extend(paquetes_preset)

def validar_nombre(nombre):
    patron = re.compile(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ]+$')
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

def realizar_reserva():
    nombre_cliente = input("Ingrese nombre del cliente: ")
    apellido_cliente = input("Ingrese apellido del cliente: ")

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
            return
    print("Cliente no encontrado.")

def cancelar_reserva():
    nombre_cliente = input("Ingrese nombre del cliente: ")
    apellido_cliente = input("Ingrese apellido del cliente: ")
    nombre_paquete = input("Ingrese nombre del paquete: ")
    
    for reserva in reservas:
        if reserva["cliente"]["nombre"] == nombre_cliente and reserva["cliente"]["apellido"] == apellido_cliente and reserva["paquete"]["nombre"] == nombre_paquete:
            reservas.remove(reserva)
            print("Reserva cancelada con éxito.")
            return
    print("Reserva no encontrada.")

def mostrar_reservas():
    print("Reservas:")
    for reserva in reservas:
        print(f"Cliente: {reserva['cliente']['nombre']} {reserva['cliente']['apellido']}")
        print(f"Paquete: {reserva['paquete']['nombre']}")
        print(f"Fecha de salida: {reserva['paquete']['fecha_salida']}")
        print(f"Fecha de llegada: {reserva['paquete']['fecha_llegada']}")
        print(f"Precio: {reserva['paquete']['precio']}")
        print("---------")

def mostrar_reservas_cliente():
    nombre_cliente = input("Ingrese nombre del cliente: ")
    apellido_cliente = input("Ingrese apellido del cliente: ")
    print(f"Reservas de {nombre_cliente} {apellido_cliente}:")
    
    reservas_encontradas = False
    for reserva in reservas:
        if reserva["cliente"]["nombre"] == nombre_cliente and reserva["cliente"]["apellido"] == apellido_cliente:
            print(f"Paquete: {reserva['paquete']['nombre']}")
            print(f"Fecha de salida: {reserva['paquete']['fecha_salida']}")
            print(f"Fecha de llegada: {reserva['paquete']['fecha_llegada']}")
            print(f"Precio: {reserva['paquete']['precio']}")
            print("---------")
            reservas_encontradas = True
            
    if not reservas_encontradas:
        print("No se encontraron reservas para este cliente.")

def mostrar_clientes():
    print("Clientes:")
    for cliente in clientes:
        print(f"Nombre: {cliente['nombre']} {cliente['apellido']}")
        print(f"Email: {cliente['email']}")
        print(f"Teléfono: {cliente['telefono']}")
        print(f"Documento: {cliente['documento']}")
        print("---------")

def mostrar_paquetes_numerados():
    print("Paquetes:")
    for index, paquete in enumerate(paquetes, start=1):
        print(f"{index}. {paquete['nombre']}")
        print(f"   Descripción: {paquete['descripcion']}")
        print(f"   Fecha de salida: {paquete['fecha_salida']}")
        print(f"   Fecha de llegada: {paquete['fecha_llegada']}")
        print(f"   Precio: {paquete['precio']}")
        print("---------")

def eliminar_paquete():
    nombre_paquete = input("Escriba el nombre del paquete a eliminar: ")
    for paquete in paquetes:
        if paquete["nombre"] == nombre_paquete:
            confirmar = input(f"¿Está seguro de eliminar el paquete {nombre_paquete}? [SI o NO]: ").upper()
            if confirmar == "SI":
                paquetes.remove(paquete)
                print("Paquete eliminado exitosamente.")
            else:
                print("Operación cancelada.")
                return
    print("Paquete no encontrado.")

def modificar_paquete():
    cambiar_paquete = input("Escriba el nombre del paquete a modificar: ")
    for paquete in paquetes:
        if paquete["nombre"] == cambiar_paquete:
            print("Ingrese nuevos datos (deje en blanco si va a mantener el dato actual): ")
            nuevo_nombre = input("Nombre: ") or paquete["nombre"]
            nueva_descripcion = input("Descripción: ") or paquete["descripcion"]
            nueva_fecha_salida = input("Fecha de salida (dd-mm-aaaa): ") or paquete["fecha_salida"]
            nueva_fecha_llegada = input("Fecha de llegada (dd-mm-aaaa): ") or paquete["fecha_llegada"]
            nuevo_precio = input("Precio: ") or paquete["precio"]

            paquete["nombre"] = nuevo_nombre
            paquete["descripcion"] = nueva_descripcion
            paquete["fecha_salida"] = nueva_fecha_salida
            paquete["fecha_llegada"] = nueva_fecha_llegada
            paquete["precio"] = float(nuevo_precio) if nuevo_precio else paquete["precio"]

            print("Paquete modificado con éxito.")
            return
    print("Paquete no encontrado.")

while True:
    print("Agencia de Viajes Global")
    print("Bienvenido a la Agencia de Viajes Global")
    print("Tu puerta de entrada a aventuras inolvidables.")
    print("Estamos aquí para ayudarte a planificar el viaje de tus sueños.")
    print("Por favor, elige una opción del menú para comenzar.")
    
    for opcion, descripcion in menu.items():
        print(f"{opcion}. {descripcion}")

    opcion = input("Ingrese opción: ").strip()
    if opcion == "1":
        registrar_cliente()
    elif opcion == "2":
        crear_paquete()
    elif opcion == "3":
        realizar_reserva()
    elif opcion == "4":
        cancelar_reserva()
    elif opcion == "5":
        mostrar_reservas()
    elif opcion == "6":
        mostrar_reservas_cliente() 
    elif opcion == "7":
        mostrar_clientes()
    elif opcion == "8":
        mostrar_paquetes_numerados()
    elif opcion == "9":
        eliminar_paquete()
    elif opcion == "10":
        modificar_paquete()
    elif opcion == "0":
        print("Gracias por utilizar nuestra agencia de viajes.")
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")