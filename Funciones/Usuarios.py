# archivo que contendras las funciones de los usuarios
import Funciones.Admin as ad

import sys


def Menu_usuario():
    """Menú principal para el usuario."""
    print("\n===== MENÚ DE USUARIO =====")
    print("1. Ver mis libros alquilados")
    print("2. Buscar libros")
    print("3. Alquilar un libro")
    print("4. Devolver un libro")
    print("5. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        print()
    elif opcion == "2":
        print()
    elif opcion == "3":
        print()
    elif opcion == "4":
        print()
    elif opcion == "5":
        print("\n¡Hasta luego!")
        sys.exit()
    else:
        print("Opción inválida, intenta nuevamente.")
        #Menu()


def Menu_administrador(usuarios,file):
    """Menú principal para el administrador."""
    print("\n===== MENÚ DE ADMINISTRADOR =====")
    print("1. Ver todos los libros")
    print("2. Agregar un libro")
    print("3. Eliminar un libro")
    print("4. Ver usuarios registrados")
    print("5. Agregar Usuario")
    print("6. Eliminar Usuario")
    print("7. Ver alquileres de libros")
    print("8. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        print()
    elif opcion == "2":
        print()
    elif opcion == "3":
        print()
    elif opcion == "4":
        ad.mostrar_usuarios(usuarios)
        print()
    elif opcion == "5":
        ad.agregar_usuario(usuarios,file)
        print()
    elif opcion == "6":
        print()
    elif opcion == "7":
        print()
    elif opcion == "8":
        print("\n¡Hasta luego!")
        sys.exit()
    else:
        print("Opción inválida, intenta nuevamente.")
        #Menu()