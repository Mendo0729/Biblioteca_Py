import hashlib
import json
import re
import time


def inicializar_archivo(archivo):
    try:
        with open(archivo, 'x') as file:
            json.dump({}, file)
    except FileExistsError:
        pass

def cargar_datos(archivo):
    try:
        with open(archivo, 'r') as file:
            contenido = file.read().strip()
            return json.loads(contenido) if contenido else {}
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def guardar_datos(data, archivo):
    with open(archivo, 'w') as file:
        json.dump(data, file, indent=4)

def encriptar_contraseña(contraseña):
    return hashlib.sha256(contraseña.encode()).hexdigest()

def comparar_contraseña(contraseña_almacenada, contraseña_introducida):
    return encriptar_contraseña(contraseña_introducida) == contraseña_almacenada

def validar_cedula(cedula):
    patron = r"^[1-9]{1,2}-\d{2,4}-\d{2,5}$"
    return re.match(patron,cedula) is not None

def validar_correo(correo):
    patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(patron, correo) is not None

def barra_carga():
    print("Cargando", end="", flush=True)
    for _ in range(3):  # Añadir puntos suspensivos
        time.sleep(0.5)
        print(".", end="", flush=True)

def borrar_barra():
    print("\r" + " " * 20, end="", flush=True)  # Borrar la línea con la barra de carga
    print("\r", end="", flush=True)