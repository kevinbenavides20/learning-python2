import sqlite3

# Conectar a la base de datos
conexion = sqlite3.connect('school.db')
cursor = conexion.cursor()

# Función para mostrar el menú principal
def mostrar_menu():
    print("-" * 20)
    print(" CRUD School ")
    print("-" * 20)
    print("[1] Crear usuario")
    print("[2] Crear estudiante")
    print("[3] Crear tipo de identificación")
    print("[4] Crear persona")
    print("[5] Crear ciudad")
    print("[6] Crear departamento")
    print("[7] Salir")
    print("-" * 20)

# Función para crear un usuario
def crear_usuario(username, password, id_persona):
    try:
        cursor.execute("""
            INSERT INTO users (
                username,
                password,
                id_person
            ) VALUES (?, ?, ?)
        """, (username, password, id_persona))
        conexion.commit()
        print("Usuario creado con éxito.")
    except sqlite3.Error as error:
        print("Error al crear usuario:", error)

# Función para crear un estudiante
def crear_estudiante(codigo, nombre, apellido, id_tipo_identificacion, numero_identificacion, id_ciudad, direccion, telefono):
    try:
        cursor.execute("""
            INSERT INTO students (
                code,
                first_name,
                last_name,
                id_identification_type,
                identification_number,
                id_city,
                address,
                mobile
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (codigo, nombre, apellido, id_tipo_identificacion, numero_identificacion, id_ciudad, direccion, telefono))
        conexion.commit()
        print("Estudiante creado con éxito.")
    except sqlite3.Error as error:
        print("Error al crear estudiante:", error)

# Función para crear un tipo de identificación
def crear_tipo_identificacion(nombre, abreviatura, descripcion):
    try:
        cursor.execute("""
            INSERT INTO identification_types (
                name,
                abbreviation,
                description
            ) VALUES (?, ?, ?)
        """, (nombre, abreviatura, descripcion))
        conexion.commit()
        print("Tipo de identificación creado con éxito.")
    except sqlite3.Error as error:
        print("Error al crear tipo de identificación:", error)

# Función para crear una persona
def crear_persona(nombre, apellido, id_tipo_identificacion, numero_identificacion, id_ciudad, direccion, telefono):
    try:
        cursor.execute("""
            INSERT INTO persons (
                first_name,
                last_name,
                id_identification_type,
                identification_number,
                id_city,
                address,
                mobile
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (nombre, apellido, id_tipo_identificacion, numero_identificacion, id_ciudad, direccion, telefono))
        conexion.commit()
        print("Persona creada con éxito.")
    except sqlite3.Error as error:
        print("Error al crear persona:", error)

# Función para crear una ciudad
def crear_ciudad(nombre, id_departamento):
    try:
        cursor.execute("""
            INSERT INTO cities (
                name,
                id_country
            ) VALUES (?, ?)
        """, (nombre, id_departamento))
        conexion.commit()
        print("Ciudad creada con éxito.")
    except sqlite3.Error as error:
        print("Error al crear ciudad:", error)

# Función para crear un departamento
def crear_departamento(nombre, descripcion):
    try:
        cursor.execute("""
            INSERT INTO departments (
                name,
                description
            ) VALUES (?, ?)
        """, (nombre, descripcion))
        conexion.commit()
        print("Departamento creado con éxito.")
    except sqlite3.Error as error:
        print("Error al crear departamento:", error)

# Bucle principal
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        username = input("Ingrese el nombre de usuario: ")
        password = input("Ingrese la contraseña: ")
        id_persona = input("Ingrese el ID de la persona: ")
        crear_usuario(username, password, id_persona)

    elif opcion == "2":
        codigo = input("Ingrese el código del estudiante: ")
        nombre = input("Ingrese el nombre del estudiante: ")
        apellido = input("Ingrese el apellido del estudiante: ")
        id_tipo_identificacion = input("Ingrese el ID del tipo de identificación: ")
        numero_identificacion = input("Ingrese el número de identificación: ")
        id_ciudad = input("Ingrese el ID de la ciudad: ")
        direccion = input("Ingrese la dirección del estudiante: ")
        telefono = input("Ingrese el teléfono del estudiante: ")
        crear_estudiante(codigo, nombre, apellido, id_tipo_identificacion, numero_identificacion, id_ciudad, direccion, telefono)

    elif opcion == "3":
        nombre = input("Ingrese el nombre del tipo de identificación: ")
        abreviatura = input("Ingrese la abreviatura del tipo de identificación: ")
        descripcion = input("Ingrese la descripción del tipo de identificación: ")
        crear_tipo_identificacion(nombre, abreviatura, descripcion)

    elif opcion == "4":
        nombre = input("Ingrese el nombre de la persona: ")
        apellido = input("Ingrese el apellido de la persona: ")
        id_tipo_identificacion = input("Ingrese el ID del tipo de identificación: ")
        numero_identificacion = input("Ingrese el número de identificación: ")
        id_ciudad = input("Ingrese el ID de la ciudad: ")
        direccion = input("Ingrese la dirección de la persona: ")
        telefono = input("Ingrese el teléfono de la persona: ")
        crear_persona(nombre, apellido, id_tipo_identificacion, numero_identificacion, id_ciudad, direccion, telefono)

    elif opcion == "5":
        nombre = input("Ingrese el nombre de la ciudad: ")
        id_departamento = input("Ingrese el ID del departamento: ")
        crear_ciudad(nombre, id_departamento)

    elif opcion == "6":
        nombre = input("Ingrese el nombre del departamento: ")
        descripcion = input("Ingrese la descripción del departamento: ")
        crear_departamento(nombre, descripcion)

    elif opcion == "7":
        print("¡Hasta la próxima!")
        break

    else:
        print("Opción no válida.")

# Cerrar conexión a


