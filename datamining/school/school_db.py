import sqlite3

# Crear conexión a la base de datos
conexion = sqlite3.connect('school.db')

# Crear cursor
cursor = conexion.cursor()

# Crear tabla students
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code VARCHAR(50) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    id_identification_type INTEGER NOT NULL,
    identification_number VARCHAR(15) NOT NULL,
    id_city INTEGER NOT NULL,
    address VARCHAR(150) NOT NULL,
    mobile VARCHAR(50) NOT NULL,
    status BOOLEAN NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    deleted_at DATETIME NULL
);
""")

# Crear tabla users
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(100) NOT NULL,
    password VARCHAR(250) NOT NULL,
    id_person INTEGER NOT NULL,
    status BOOLEAN NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    deleted_at DATETIME NULL
);
""")

# Crear tabla countries
cursor.execute("""
CREATE TABLE IF NOT EXISTS countries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    deleted_at DATETIME NULL
);
""")

# Crear tabla cities
cursor.execute("""
CREATE TABLE IF NOT EXISTS cities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    id_country INTEGER NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    deleted_at DATETIME NULL
);
""")

# Crear tabla departments
cursor.execute("""
CREATE TABLE IF NOT EXISTS departments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    description VARCHAR(100) NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    deleted_at DATETIME NULL
);
""")

# Crear tabla identification_types
cursor.execute("""
CREATE TABLE IF NOT EXISTS identification_types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) NOT NULL,
    abbreviation VARCHAR(10) NOT NULL,
    description VARCHAR(100) NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    deleted_at DATETIME NULL
);
""")

# Crear tabla persons
cursor.execute("""
CREATE TABLE IF NOT EXISTS persons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    id_identification_type INTEGER NOT NULL,
    identification_number VARCHAR(15) NOT NULL,
    id_city INTEGER NOT NULL,
    address VARCHAR(150) NOT NULL,
    mobile VARCHAR(50) NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    deleted_at DATETIME NULL
);
""")

# Cerrar conexión a la base de datos
conexion.close()

