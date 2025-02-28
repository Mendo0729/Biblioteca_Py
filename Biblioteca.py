from Funciones import Funciones as fn
from Funciones import Usuarios as user
import sys

USUARIO_FILE = 'usuarios.json'
usuarios = fn.cargar_datos(USUARIO_FILE)


def crear_admin_por_defecto():
    """Crea un administrador por defecto si no existe."""
    if "admin" in usuarios and usuarios['admin']:
        return  # ✅ Si ya existe, no hace nada

    print("No existe administrador.")
    try:
        while True:
            nombre = input("Ingresa el nombre del administrador: ").strip()
            if not nombre:
                print("El campo 'nombre' no puede estar vacío.")
                continue

            cedula = input("Ingresa la cédula para el administrador: ").strip()
            if not cedula or not fn.validar_cedula(cedula):
                print("Cédula inválida. Inténtalo nuevamente.")
                continue

            correo = input("Ingresa el correo del administrador: ").strip()
            if not correo or not fn.validar_correo(correo):
                print(fn.validar_correo(correo))
                print("Correo inválido. Inténtalo nuevamente.")
                continue

            contraseña = input("Ingresa la contraseña para el administrador: ").strip()
            if not contraseña:
                print("El campo 'contraseña' no puede estar vacío.")
                continue

            sexo = input("Ingresa el sexo M(masculino) - F(femenino): ").capitalize()
            if not sexo:
                print("El campo 'sexo' no puede estar vacio")
                continue

            usuarios["admin"] = {
                1: {
                    'nombre': nombre,
                    'cedula': cedula,
                    'correo': correo,
                    'sexo': sexo,
                    'contrasena': fn.encriptar_contraseña(contraseña)
                }
            }
            fn.guardar_datos(usuarios, USUARIO_FILE)  # ✅ Guardar cambios en el JSON
            print("\n✅ Administrador creado exitosamente.")
            break

    except KeyboardInterrupt:
        print("\nProceso interrumpido. Saliendo del programa...")

def iniciar_sesion(usuarios):
    """Permite a los usuarios iniciar sesión."""
    intentos = 0
    while intentos < 3:
        try:
            correo = input("Ingresa el correo: ").strip()
            if not correo or not fn.validar_correo(correo):
                print("Correo inválido. Inténtalo nuevamente.")
                continue

            contrasena = input("Ingresa la contraseña: ").strip()
            if not contrasena:
                print("El campo 'contraseña' no puede estar vacío.")
                continue

            contrasena_encriptada = fn.encriptar_contraseña(contrasena)

            usuario_encontrado = False
            for rol, usuario_rol in usuarios.items():
                for usuario_id, usuario_info in usuario_rol.items():
                    if usuario_info['correo'] == correo:
                        usuario_encontrado = True
                        if usuario_info['contrasena'] == contrasena_encriptada:
                            print(f"\n✅ Bienvenido {usuario_info['nombre']}!")
                            if rol == 'admin':
                                user.Menu_administrador(usuarios, USUARIO_FILE)
                            elif rol == 'usuario':
                                user.Menu_usuario()
                            return True
                        else:
                            print("❌ Contraseña incorrecta.")
            if not usuario_encontrado:
                print("❌ Correo incorrecto.")
            intentos += 1

        except KeyboardInterrupt:
            print("\nSaliendo del programa...")
            exit()

    print("⚠️ Has excedido el número de intentos. Intenta más tarde.")

def sign_up(usuarios):
    try:
        # Verificar si la clave 'usuario' existe en el diccionario
        if "usuario" not in usuarios:
            usuarios["usuario"] = {}

        while True:
            nombre = input("Ingresa el nombre: ").strip()
            if not nombre:
                print("El campo 'nombre' no puede estar vacío.")
                continue

            cedula = input("Ingresa la cédula: ").strip()
            if not cedula or not fn.validar_cedula(cedula):
                print("Cédula inválida. Inténtalo nuevamente.")
                continue

            correo = input("Ingresa el correo: ").strip()
            if not correo or not fn.validar_correo(correo):
                print(fn.validar_correo(correo))
                print("Correo inválido. Inténtalo nuevamente.")
                continue
            usuario_encontrado = False
            for rol, usuario_rol in usuarios.items():
                for usuario_id, usuario_info in usuario_rol.items():
                    if usuario_info['correo'] == correo:
                        usuario_encontrado = True
                        print("El correo ya existe")
                    break

            contraseña = input("Ingresa la contraseña: ").strip()
            if not contraseña:
                print("El campo 'contraseña' no puede estar vacío.")
                continue

            sexo = input("Ingresa el sexo M(masculino) - F(femenino): ").capitalize()
            if not sexo:
                print("El campo 'sexo' no puede estar vacio")
                continue

            # Obtener el último ID y asignar el siguiente número
            ultimo_id = max(usuarios["usuario"].keys(), default=0)
            nuevo_id = int(ultimo_id) + 1

            usuarios["usuario"][nuevo_id] = {
                'nombre': nombre,
                'cedula': cedula,
                'correo': correo,
                'sexo': sexo,
                'contrasena': fn.encriptar_contraseña(contraseña)
            }

            fn.guardar_datos(usuarios, USUARIO_FILE)  # ✅ Guardar cambios en el JSON
            print("\n✅ Usuario creado exitosamente con ID:", nuevo_id)
            break
    except KeyboardInterrupt:
        print("\nProceso interrumpido. Saliendo del programa...")

def menu_principal():
    while True:
        try:
            print("\nMenú principal:")
            print("1. Iniciar sesión")
            print("2. Sign up")
            print("3. Salir")
            opcion = int(input("Elige una opción: "))
            try:
                if opcion not in [1, 2, 3]:
                    print("Por favor, selecciona una opción válida.\n")
                    continue  # Vuelve a mostrar el menú si la opción no es válida.
            except ValueError:
                print("Por favor, ingresa un número válido.")


            if opcion == 1:
                iniciar_sesion(usuarios)
            elif opcion == 2:
                sign_up(usuarios)
            elif opcion == 3:
                sys.exit()
            else:
                print("Opción no válida. Intenta nuevamente.")

        except KeyboardInterrupt:
            print("\nProceso interrumpido. Saliendo del programa...")
            exit()

if __name__ == "__main__":
    try:
        crear_admin_por_defecto()
        menu_principal()
    except KeyboardInterrupt:
        print("\nSaliendo del programa...")
        exit()
