clientes = [] 
paquetes = []
reservas = []

menu = {
    "1": "Registrar cliente",
    "2": "Crear paquete de viaje",
    "3": "Realizar reserva",
    "4": "Cancelar reserva",
    "5": "Mostrar reservas",
    "6": "Mostrar clientes",
    "7": "Mostrar paquetes",
    "8": "Eliminar paquete",
    "9": "Modificar paquete",
    "0": "Salir"
}


def registrar_cliente():
    nombre = input("Ingrese nombre del cliente: ")
    apellido = input("Ingrese apellido del cliente: ")
    email = input("Ingrese email del cliente: ")
    telefono = input("Ingrese teléfono del cliente: ")
    clientes.append({"nombre": nombre, "apellido": apellido, "email": email, "telefono": telefono})
    print("Cliente registrado con éxito.")


def crear_paquete():
    nombre = input("Ingrese nombre del paquete: ")
    descripcion = input("Ingrese descripcion del paquete: ")
    fecha_salida = input("Ingrese fecha de salida del paquete (aaaa-mm-dd): ")
    fecha_llegada = input("Ingrese fecha de llegada del paquete (aaaa-mm-dd): ")
    
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
    nombre_paquete = input("Ingrese nombre del paquete: ")
    
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

        
def mostrar_clientes():
    print("Clientes:")
    for cliente in clientes:
        print(f"Nombre: {cliente['nombre']} {cliente['apellido']}")
        print(f"Email: {cliente['email']}")
        print(f"Teléfono: {cliente['telefono']}")
        print("---------")

        
def mostrar_paquetes():
    print("Paquetes:")
    for paquete in paquetes:
        print(f"Nombre: {paquete['nombre']}")
        print(f"Descripcion: {paquete['descripcion']}")
        print(f"Fecha de salida: {paquete['fecha_salida']}")
        print(f"Fecha de llegada: {paquete['fecha_llegada']}")
        print(f"Precio: {paquete['precio']}")
        print("---------")

def eliminar_paquete():
    nombre_paquete = input("Escriba el nombre del paquete a eliminar: ")
    for paquete in paquetes:
        if paquete["nombre"] == nombre_paquete:
            confirmar =input(f"¿Está seguro de eliminar el paquete {nombre_paquete}? [SI o NO]: ").upper()
            if confirmar == "SI":
                paquetes.remove(paquete)
                print("Paquete eliminado exitosamente.")
            else:
                print("Operación cancelada")
                return
    print("Paquete no encontrado")

def modificar_paquetes():
    cambiar_paquete = input("Escriba el nombre del paquete a modificar: ")
    for paquete in paquetes:
        if paquete["nombre"] == cambiar_paquete:
            print ("Ingrese nuevos datos (deje en blanco si va a mantener el dato actual): ")
            nuevo_nombre = input("Nombre: ") or paquete["nombre"]
            nueva_descripcion = input("Descripción: ") or paquete["descripcion"]
            nueva_fecha_salida = input("Fecha de salida(dd-mm-aaaa): ") or paquete["fecha_salida"]
            nueva_fecha_llegada = input("Fecha de llegada(dd-mm-aaaa): ") or paquete["fecha_llegada"]
            nuevo_precio = input("Precio: ") or paquete["precio"]

            paquete["nombre"] = nuevo_nombre
            paquete["descripcion"] = nueva_descripcion
            paquete["fecha_salida"] = nueva_fecha_salida
            paquete["fecha_llegada"] = nueva_fecha_llegada
            paquete["precio"] = nuevo_precio

            print("Paquete modificado con éxito.")
            return
    print("Paquete no encontrado.")

        
while True:
    print("Agencia de Viajes Global")
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
        mostrar_clientes()
    elif opcion == "7":
        mostrar_paquetes()
    elif opcion == "8":
        eliminar_paquete()
    elif opcion == "9":
        modificar_paquetes()
    elif opcion == "0":
        print("Gracias por utilizar nuestra agencia de viajes.")
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")