# Ejercicio 10
#  Escribir un programa que permita gestionar la base de datos de clientes de una empresa.
#
#  Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, 
#  y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente),
#  donde preferente tendrá el valor True si se trata de un cliente preferente.
# 
#  El programa debe preguntar al usuario por una opción del siguiente menú:
#   (1) Añadir cliente,
#   (2) Eliminar cliente, 
#   (3) Mostrar cliente, 
#   (4) Listar todos los clientes, 
#   (5) Listar clientes preferentes,
#   (6) Terminar.
#
#  En función de la opción elegida el programa tendrá que hacer lo siguiente:
#   1. Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
#   2. Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
#   3. Preguntar por el NIF del cliente y mostrar sus datos.
#   4.Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
#   5.Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
#   6.Terminar el programa.

# cliente = {"NIF": {"Nombre":"Kevin Conde", "Direccion": "Cerro del potosi 1241", "Telefono": 8121523309, "Correo": "conde.jimenez@hotmail.com", "Preferente":True}}
cliente = {}
datos = {}
# datos = {"Nombre": "", "Direccion": "", "Telefono": 0, "Correo": "", "Preferente":False}
menu = 0

while menu != 6:
    print()
    print("Elige una de las siguientes opciones.")
    print("""
    Presiona 1 para Añadir Cliente.
    Presiona 2 para Eliminar Cliente.
    Presiona 3 para Mostrar Cliente.
    Presiona 4 para Listar todos los Clientes.
    Presiona 5 para Listar Clientes Preferentes.
    Presiona 6 para Terminar. 
    """)
    print()
    menu = int(input("Elige una opcion: "))
    print()

    if menu == 1:
        print("Añadir Cliente")
        nif = input("Agrega tu NIF: ")
        nombre = input("Cual es su nombre: ")
        direccion = input("Escribe la  direccion: ")
        telefono = input("Escribe un telefono: ")
        correo = input("¿Cual es su correo?: ")
        preferente = input("¿Es cliente preferente?(Si/No): ")
        datos = {"Nombre": nombre, "Direccion": direccion, "Telefono": telefono, "Correo": correo, "Preferente": preferente == "Si"}
        cliente[nif] = datos

    elif menu == 2:
        print("Eliminar Cliente")
        nif = input("Cual es el NIF: ")
        if nif in cliente:
            print(f"Se elimino el cliente {cliente[nif]}")
            del cliente[nif]
        else:
            print("El cliente no existe")
        
    elif menu == 3:
        print("Mostrar Cliente")
        nif = input("Escribe el NIF del Cliente: ")
        for clave, valor in cliente[nif].items():
            print(f"{clave}: {valor}")
        
    elif menu == 4:
        print("Listar Clientes")
        for clave in cliente.keys():
            print(f"NIF: {clave}")
            for claveCliente, valorCliente in cliente[clave].items():
                print(f"{claveCliente}: {valorCliente}")
            print()
        
    elif menu == 5:
        print("Listar Clientes Preferentes")
        for clave in cliente:
            if cliente[clave]["Preferente"] == True:
                print(f"NIF:{clave}")
                for claveCliente, valorCliente in cliente[clave].items():
                    print(f"{claveCliente}: {valorCliente}")
                print()